import os
import json

def pascal_case(name: str) -> str:
    return "".join(part.capitalize() for part in name.replace("_", " ").split())

def generate_forui_json(root_path: str):
    """
    root_path → path to /forui directory
    Returns JSON structure:
    {
      "forui": {
        "Accordion": {
          "accordion_controller": "...code...",
          "accordion_item": "...code...",
          "accordion": "...code..."
        },
        "Autocomplete": {
          ...
        }
      }
    }
    """
    result = {"forui": {}}

    # Iterate over all subdirectories inside forui/
    for component_folder in os.listdir(root_path):
        folder_path = os.path.join(root_path, component_folder)

        # Only process directories (components)
        if not os.path.isdir(folder_path):
            continue

        component_name = pascal_case(component_folder)  # e.g. "accordion" → "Accordion"
        result["forui"][component_name] = {}

        # Collect all .dart files inside this component folder
        for file in os.listdir(folder_path):
            if not file.endswith(".dart"):
                continue

            file_path = os.path.join(folder_path, file)

            # Remove extension → key name in JSON
            key_name = file.replace(".dart", "")

            # Read file contents
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()
            except Exception as e:
                code = f"/* Error reading file: {e} */"

            result["forui"][component_name][key_name] = code

    return result


# ---- RUN EXAMPLE ----
if __name__ == "__main__":
    FORUI_PATH = r"C:\Users\ramka\Documents\Flutter-codeGenerationTool\Template-Serialization\forui"

    json_data = generate_forui_json(FORUI_PATH)

    output_path = "forui_serialized.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)

    print(f"JSON serialization completed → {output_path}")
