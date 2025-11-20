import os
import json

def pascal_case(name: str) -> str:
    return "".join(part.capitalize() for part in name.replace("_", " ").split())

def clean_filename(filename: str) -> str:
    """Remove extension and leading td_ prefix."""
    name = filename.replace(".dart", "")
    if name.startswith("td_"):
        name = name[3:]
    return name

def generate_tdesign_json(root_path: str):
    """
    root_path → path to TDesign-Flutter folder
    Returns JSON structure:
    {
      "TDesign": {
        "ActionSheet": {
            "action_sheet": "...code...",
            "action_sheet_item": "...code..."
        },
        ...
      }
    }
    """
    result = {"TDesign": {}}

    # Iterate over component folders
    for component_folder in os.listdir(root_path):
        folder_path = os.path.join(root_path, component_folder)
        if not os.path.isdir(folder_path):
            continue

        component_name = pascal_case(component_folder)
        result["TDesign"][component_name] = {}

        # Process all .dart files in the folder
        for file in os.listdir(folder_path):
            if not file.endswith(".dart"):
                continue

            key_name = clean_filename(file)
            file_path = os.path.join(folder_path, file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()
            except Exception as e:
                code = f"/* Error reading file: {e} */"

            result["TDesign"][component_name][key_name] = code

    return result


# ---- RUN EXAMPLE ----
if __name__ == "__main__":
    TDESIGN_PATH = r"C:\Users\ramka\Documents\Flutter-codeGenerationTool\Template-Serialization\TDesign-Flutter"

    json_data = generate_tdesign_json(TDESIGN_PATH)

    output_path = "tdesign_flutter_serialized.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)

    print(f"TDesign Flutter JSON serialization completed → {output_path}")
