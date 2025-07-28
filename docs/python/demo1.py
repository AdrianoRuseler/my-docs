import os

def create_directory(path):
    """Creates a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    print(f"Created directory: {path}")

def create_markdown_file(path, content, front_matter=None):
    """Creates a Markdown file with optional front matter."""
    with open(path, 'w', encoding='utf-8') as f:
        if front_matter:
            f.write("---\n")
            for key, value in front_matter.items():
                f.write(f"{key}: {value}\n")
            f.write("---\n\n")
        f.write(content)
    print(f"Created file: {path}")

def create_simplified_docusaurus_docs_structure(base_path="my-demo1"):
    """
    Creates a simplified Docusaurus folder structure with custom docs directories.
    """
    print(f"Creating simplified Docusaurus docs structure in: {base_path}")

    # Create the base site directory
    create_directory(base_path)

    # --- Docs Folder ---
    docs_path = os.path.join(base_path, "docs")
    create_directory(docs_path)
    create_markdown_file(
        os.path.join(docs_path, "intro.md"),
        "# Introduction to Docs\n\nThis is the main introduction to your project's documentation.",
        {"id": "intro", "title": "Introduction", "sidebar_position": 1}
    )
    create_markdown_file(
        os.path.join(docs_path, "further-info.md"),
        "# Further Information\n\nFind more details here.",
        {"id": "further-info", "title": "Further Information", "sidebar_position": 2}
    )

    # --- API Docs Folder ---
    api_docs_path = os.path.join(base_path, "api-docs")
    create_directory(api_docs_path)
    create_markdown_file(
        os.path.join(api_docs_path, "getting-started.md"),
        "# API Getting Started\n\nLearn how to get started with our API.",
        {"id": "api-getting-started", "title": "Getting Started", "sidebar_position": 1}
    )
    create_markdown_file(
        os.path.join(api_docs_path, "endpoints.md"),
        "# API Endpoints\n\nDetails about available API endpoints.",
        {"id": "api-endpoints", "title": "Endpoints", "sidebar_position": 2}
    )

    # --- Dev Docs Folder ---
    dev_docs_path = os.path.join(base_path, "dev-docs")
    create_directory(dev_docs_path)
    create_markdown_file(
        os.path.join(dev_docs_path, "setup.md"),
        "# Development Setup\n\nInstructions for setting up your development environment.",
        {"id": "dev-setup", "title": "Setup Guide", "sidebar_position": 1}
    )
    create_markdown_file(
        os.path.join(dev_docs_path, "contributing.md"),
        "# Contributing Guidelines\n\nHow to contribute to the project.",
        {"id": "contributing", "title": "Contributing", "sidebar_position": 2}
    )

    print("\nSimplified Docusaurus docs structure created successfully!")
    print(f"You'll find your new structure in the '{base_path}' directory.")

if __name__ == "__main__":
    create_simplified_docusaurus_docs_structure()