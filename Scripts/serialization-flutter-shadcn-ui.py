import os
import re
import json

# ---------------------------------------------
# CONFIG
# ---------------------------------------------
ROOT = r"C:\Users\ramka\Documents\Flutter-codeGenerationTool\Template-Serialization\flutter-shadcn-ui"

# Special mapping groups
FORM_FOLDER = "form"
FORM_FIELDS_FOLDER = "fields"


# ---------------------------------------------
# HELPERS
# ---------------------------------------------
def extract_classes_and_enums(dart_code: str):
    """
    Extract public class names, enums, and their full definitions.
    Returns: dict { name: code_block }
    """
    pattern = r"\b(class|enum)\s+([A-Z][A-Za-z0-9_]*)[\s\S]*?\{[\s\S]*?\}"
    matches = re.findall(pattern, dart_code)

    result = {}

    for m in re.finditer(pattern, dart_code):
        full_block = m.group(0)
        kind = m.group(1)
        name = m.group(2)

        # store block
        result[name] = full_block.strip()

    return result


def load_dart_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------
# MAIN EXTRACTION
# ---------------------------------------------
def build_json_structure(root):
    output = {"shadcn_flutter": {}}

    for dirpath, dirs, files in os.walk(root):
        rel = os.path.relpath(dirpath, root).replace("\\", "/")

        # ---------------------------------------------------------------
        # 1. Top-level files
        # ---------------------------------------------------------------
        if rel == ".":
            for f in files:
                if not f.endswith(".dart"):
                    continue

                comp_name = os.path.splitext(f)[0]
                dart = load_dart_file(os.path.join(dirpath, f))
                extracted = extract_classes_and_enums(dart)

                output["shadcn_flutter"][comp_name.capitalize()] = extracted

        # ---------------------------------------------------------------
        # 2. form/ folder
        # ---------------------------------------------------------------
        elif rel == FORM_FOLDER:
            for f in files:
                if not f.endswith(".dart"):
                    continue

                name = os.path.splitext(f)[0]  # form.dart → form
                comp_name = name.capitalize()  # Form / Field

                dart = load_dart_file(os.path.join(dirpath, f))
                extracted = extract_classes_and_enums(dart)

                output["shadcn_flutter"][comp_name] = extracted

        # ---------------------------------------------------------------
        # 3. form/fields/ folder → FormFields group
        # ---------------------------------------------------------------
        elif rel == f"{FORM_FOLDER}/{FORM_FIELDS_FOLDER}":
            if "FormFields" not in output["shadcn_flutter"]:
                output["shadcn_flutter"]["FormFields"] = {}

            for f in files:
                if not f.endswith(".dart"):
                    continue

                name = os.path.splitext(f)[0]  # checkbox
                comp_name = name.capitalize()

                dart = load_dart_file(os.path.join(dirpath, f))
                extracted = extract_classes_and_enums(dart)

                output["shadcn_flutter"]["FormFields"][comp_name] = extracted

    return output


# ---------------------------------------------
# EXECUTION
# ---------------------------------------------
result = build_json_structure(ROOT)

# export to JSON file
out_path = "shadcn_flutter_serialized.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

print("DONE →", out_path)
