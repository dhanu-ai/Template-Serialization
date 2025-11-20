Here’s the cleaned-up version of your README with **Usage Instructions removed** and **License section simplified** since you don’t have a license:

````{"variant":"standard","id":"61827","title":"Unified Flutter UI Component Serialization README Cleaned"}
# Unified Flutter UI Component Serialization

## Description
This project collects and serializes Flutter UI components from multiple popular libraries into JSON format for easy integration, code analysis, and automated tooling. The resulting JSON provides a unified, machine-readable registry of components across libraries.

## Libraries / Sources Used
The following Flutter libraries were used to create the serialized component registry:

| Library               | GitHub Repo                                                                                   | What It Provides / Why Use It                                                                                                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **flutter-shadcn-ui** | [nank1ro/flutter-shadcn-ui](https://github.com/nank1ro/flutter-shadcn-ui)                     | Port of the shadcn/ui design system to Flutter; customizable, with many core UI components.                                                                                      |
| **Forui**             | [forus-labs/forui](https://github.com/forus-labs/forui)                                       | Minimalistic, clean widget library (~40+ widgets), good theming + Flutter Hooks support.                                                                                          |
| **TDesign Flutter**   | [Tencent/tdesign-flutter](https://github.com/Tencent/tdesign-flutter)                         | UI components based on **TDesign** system. Theming, icons, and design customization supported.                                                                                   |
| **Widgetbook**        | [widgetbook/widgetbook](https://github.com/widgetbook/widgetbook)                               | Not exactly a component library, but a **widget catalog / sandbox**. Helps you build, test, and showcase isolated widgets—useful for designing and templating.                     |

> **Note:** All original licenses are respected. This project only provides serialized representations of the source code for tooling and analysis.

## Purpose / Motivation
This repository provides a unified JSON registry of Flutter UI components to:

- Facilitate rapid prototyping  
- Enable automated testing  
- Support cross-library component exploration  
- Provide a foundation for code generation or tooling pipelines  

## Folder Structure / JSON Output
The JSON output is organized by library and component:

```
├─ flutter-shadcn-ui
├─ forui
├─ TDesign-Flutter
└─ Widgetbook
```

Each component is mapped as:

```
Library → Component → Files → Source Code
```

Example:

```json
{
  "forui": {
    "Button": {
      "button": "...code...",
      "button_icon": "...code..."
    }
  }
}
```

## Installation Guide
To use the original libraries in your Flutter project, add the corresponding dependency in your `pubspec.yaml` file:

```yaml
dependencies:
  flutter:
    sdk: flutter

  # Flutter Shadcn UI
  flutter_shadcn_ui: ^<latest_version>

  # Forui
  forui: ^<latest_version>

  # TDesign Flutter
  tdesign_flutter: ^<latest_version>

  # Widgetbook
  widgetbook: ^<latest_version>
```

Then run:

```bash
flutter pub get
```

> Replace `<latest_version>` with the version number from the respective library’s pub.dev page.

## Acknowledgements
Special thanks to the authors and contributors of the original libraries:

- flutter-shadcn-ui team  
- Forui team  
- TDesign Flutter team  
- Widgetbook team  

Their work enabled the creation of this unified component registry and serves as inspiration for tooling and prototyping.
````
