---
id: vscode-setup
title: How to Setup VScode
slug: /vscode-setup
---

# How to Setup VScode

### 4\. Workspace Setup (.vscode folder)

For project-specific settings, create a `.vscode` folder at the root of your Docusaurus project.

  * **`.vscode/settings.json`:** Place any settings here that you want to apply only to this specific Docusaurus project. This is where you'd put the `files.exclude` and `search.exclude` settings mentioned above, or any formatter overrides.

    Example `settings.json`:

my-website/.vscode/settings.json
```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "terminal.integrated.defaultProfile.windows": "Command Prompt",
  "files.exclude": {
    "**/.git": true,
    "**/node_modules": true,
    "**/.docusaurus": true,
    "**/build": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/.docusaurus": true,
    "**/build": true
  }
}
```

my-website/.vscode/extensions.json

```json
{
  "recommendations": [
    "streetsidesoftware.code-spell-checker",
    "dbaeumer.vscode-eslint",
    "tomasdahlqvist.markdown-admonitions",
    "yzhang.markdown-all-in-one",
    "bierner.markdown-footnotes",
    "bierner.markdown-mermaid",
    "bierner.markdown-yaml-preamble",
    "pkief.material-icon-theme",
    "esbenp.prettier-vscode"
    // Add other relevant extensions
  ]
}
```


## Gemini response
Setting up VS Code for Docusaurus involves configuring extensions, settings, and potentially some workspace-specific configurations to enhance your development experience. Here's a comprehensive guide:

### 1\. Essential VS Code Extensions

These extensions will significantly improve your Docusaurus development workflow:

  * **ESLint:**

      * **Purpose:** Lints your JavaScript/TypeScript code to catch errors, enforce coding styles, and ensure best practices. Docusaurus projects typically come with ESLint configured.
      * **Installation:** Search for "ESLint" by Dirk Baeumer in the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X`).
      * **Configuration:** Make sure the extension is enabled for your workspace. If you encounter issues, you might need to specify the ESLint path in your VS Code settings (rare for standard Docusaurus setups).

  * **Prettier - Code formatter:**

      * **Purpose:** Automatically formats your code (JavaScript, JSX, TypeScript, CSS, Markdown, etc.) to maintain consistent style across your project.
      * **Installation:** Search for "Prettier - Code formatter" by Esben Petersen.
      * **Configuration:**
          * **Format on Save:** Highly recommended. Go to `File > Preferences > Settings` (or `Code > Settings` on macOS). Search for "Format On Save" and enable it.
          * **Default Formatter:** Search for "Default Formatter" and set it to "Prettier - Code formatter".
          * **Prettier in Docusaurus:** Docusaurus projects often include a `.prettierrc` file at the root, which Prettier will automatically pick up.

  * **Markdown All in One:**

      * **Purpose:** Essential for working with Docusaurus documentation, which is primarily written in Markdown. Provides features like:
          * Table of Contents
          * Auto-completion
          * Math support
          * List editing
          * Preview (side-by-side or full)
          * Keybindings for formatting (bold, italic, etc.)
      * **Installation:** Search for "Markdown All in One" by Yuya Tanaka.

  * **MDX:**

      * **Purpose:** Docusaurus uses MDX (Markdown + JSX) for many components and pages. This extension provides syntax highlighting for MDX files, which is not natively supported by VS Code.
      * **Installation:** Search for "MDX" by Unifiedjs.

  * **React Native Tools (or specific React extensions):**

      * **Purpose:** While Docusaurus isn't React Native, this extension (or others like "Simple React Snippets" by burkeholland) can provide useful React-specific features like JSX syntax highlighting, Emmet support for React, and sometimes intelligent auto-completion for React components.
      * **Installation:** Search for "React Native Tools" by Microsoft or "Simple React Snippets".

### 2\. Recommended VS Code Settings

You can configure these globally (User Settings) or specifically for your Docusaurus project (Workspace Settings: `.vscode/settings.json`). Workspace settings are preferred for project-specific configurations.

  * **Format on Save (if not already set via Prettier setup):**

    ```json
    {
      "editor.formatOnSave": true
    }
    ```

  * **Default Formatter (if not already set via Prettier setup):**

    ```json
    {
      "editor.defaultFormatter": "esbenp.prettier-vscode"
    }
    ```

  * **Files Exclude (Optional, but good for performance):**
    Exclude `node_modules` and the Docusaurus build output (`.docusaurus`, `build`) from VS Code's file watcher and search.

    ```json
    {
      "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/node_modules": true,
        "**/.docusaurus": true,
        "**/build": true
      },
      "search.exclude": {
        "**/node_modules": true,
        "**/.docusaurus": true,
        "**/build": true
      }
    }
    ```

  * **Path Intellisense:**

      * **Purpose:** Auto-completes filenames for imports (e.g., `import MyComponent from '../components/MyComponent'`).
      * **Installation:** Search for "Path Intellisense" by Christian Kohler.
      * **No specific setting needed; it usually works out of the box.**

  * **Editor Font Ligatures (Optional, for aesthetics):**
    If you use a font like Fira Code or Cascadia Code, you can enable ligatures for a more visually appealing code experience.

    ```json
    {
      "editor.fontFamily": "Fira Code", // Or your preferred font
      "editor.fontLigatures": true
    }
    ```

### 3\. Integrated Terminal

VS Code's integrated terminal is perfect for running Docusaurus commands:

  * **Open Terminal:** `Ctrl+` or `Cmd+`
  * **Run Docusaurus commands:**
    ```bash
    npm start         # Start the development server
    npm run build     # Build the static site
    npm run swizzle   # Customize theme components
    ```

### 4\. Workspace Setup (.vscode folder)

For project-specific settings, create a `.vscode` folder at the root of your Docusaurus project.

  * **`.vscode/settings.json`:** Place any settings here that you want to apply only to this specific Docusaurus project. This is where you'd put the `files.exclude` and `search.exclude` settings mentioned above, or any formatter overrides.

    Example `settings.json`:

    ```json
    {
      "editor.formatOnSave": true,
      "editor.defaultFormatter": "esbenp.prettier-vscode",
      "files.exclude": {
        "**/.docusaurus": true,
        "**/build": true,
        "**/node_modules": true
      },
      "search.exclude": {
        "**/.docusaurus": true,
        "**/build": true,
        "**/node_modules": true
      }
    }
    ```

  * **`.vscode/extensions.json` (Recommended for teams):**
    This file allows you to recommend extensions to other developers working on the same project. When someone opens the project, VS Code will suggest installing these extensions.

    Example `extensions.json`:

    ```json
    {
      "recommendations": [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "yzhang.markdown-all-in-one",
        "unifiedjs.vscode-mdx"
        // Add other relevant extensions
      ]
    }
    ```

### 5\. Git Integration (Built-in)

VS Code has excellent built-in Git integration. Docusaurus projects are typically version-controlled, so this is crucial:

  * **Source Control View (`Ctrl+Shift+G` or `Cmd+Shift+G`):** Track changes, stage files, commit, pull, push, etc.
  * **`.gitignore`:** Ensure your Docusaurus project has a proper `.gitignore` file (usually generated by Docusaurus init), which should include `node_modules`, `.docusaurus`, `build`, etc., to keep your repository clean.

### 6\. Troubleshooting Tips

  * **ESLint/Prettier Conflicts:** If ESLint and Prettier seem to conflict, ensure Prettier is running *before* ESLint for formatting, and ESLint is configured to *ignore* formatting rules that Prettier handles. The ESLint Prettier plugin (`eslint-config-prettier`) usually takes care of this automatically in Docusaurus projects.
  * **Performance Issues:** If VS Code feels slow, especially in large `node_modules` folders, ensure your `files.exclude` and `search.exclude` settings are correctly configured.
  * **Restart VS Code:** Sometimes, after installing new extensions or changing settings, a full restart of VS Code can resolve unexpected behavior.

By following these steps, you'll have a highly optimized and efficient VS Code environment for developing your Docusaurus documentation site.


## Doc Writer Profile Template
https://code.visualstudio.com/docs/configure/profiles#_doc-writer-profile-template