import os
import json

def pascal_case(name: str) -> str:
    return "".join(part.capitalize() for part in name.replace("_", " ").split())

def clean_filename(filename: str) -> str:
    """Remove .dart extension."""
    return filename.replace(".dart", "")

def generate_widgetbook_json(root_path: str):
    """
    Recursively generates JSON structure for Widgetbook:
    {
      "Widgetbook": {
        "Addons": {
          "AccessibilityAddon": {
            "accessibility_addon": "...code...",
            "addon": "...code..."
          },
          ...
        },
        "Fields": { ... },
        "Integrations": { ... }
      }
    }
    """
    result = {"Widgetbook": {}}

    # Iterate over top-level namespace folders
    for namespace_folder in os.listdir(root_path):
        namespace_path = os.path.join(root_path, namespace_folder)
        if not os.path.isdir(namespace_path):
            continue

        namespace_name = pascal_case(namespace_folder)
        result["Widgetbook"][namespace_name] = {}

        # Process each component inside namespace
        for component in os.listdir(namespace_path):
            component_path = os.path.join(namespace_path, component)

            # Single-file component
            if os.path.isfile(component_path) and component.endswith(".dart"):
                component_name = pascal_case(component.replace(".dart", ""))
                try:
                    with open(component_path, "r", encoding="utf-8") as f:
                        code = f.read()
                except Exception as e:
                    code = f"/* Error reading file: {e} */"
                result["Widgetbook"][namespace_name][component_name] = {
                    clean_filename(component): code
                }

            # Folder component
            elif os.path.isdir(component_path):
                component_name = pascal_case(component)
                result["Widgetbook"][namespace_name][component_name] = {}

                for file in os.listdir(component_path):
                    if not file.endswith(".dart"):
                        continue
                    file_path = os.path.join(component_path, file)
                    key_name = clean_filename(file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            code = f.read()
                    except Exception as e:
                        code = f"/* Error reading file: {e} */"
                    result["Widgetbook"][namespace_name][component_name][key_name] = code

    return result

# ---- RUN EXAMPLE ----
if __name__ == "__main__":
    WIDGETBOOK_PATH = r"C:\Users\ramka\Documents\Flutter-codeGenerationTool\Template-Serialization\Widgetbook"

    json_data = generate_widgetbook_json(WIDGETBOOK_PATH)

    output_path = "widgetbook_serialized.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)

    print(f"Widgetbook JSON serialization completed → {output_path}")
