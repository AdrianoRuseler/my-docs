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

def create_docusaurus_nested_docs_structure(base_path="my-demo2"):
    """
    Creates a Docusaurus folder structure with nested docs directories:
    my-demo2/
    ├── docs/
    │   ├── intro.md
    │   ├── user-guide/
    │   │   ├── getting-started.md
    │   │   └── features.md
    │   ├── api-reference/
    │   │   ├── endpoints.md
    │   │   └── authentication.md
    │   └── ...
    """
    print(f"Creating Docusaurus nested docs structure in: {base_path}")

    # Create the base site directory
    create_directory(base_path)

    # Docs Folder
    docs_path = os.path.join(base_path, "docs")
    create_directory(docs_path)

    # intro.md
    create_markdown_file(
        os.path.join(docs_path, "intro.md"),
        "# Welcome to our Documentation!\n\nThis is the main introductory page for our Docusaurus site.",
        {"id": "intro", "title": "Introduction", "sidebar_position": 1}
    )

    # user-guide subfolder
    user_guide_path = os.path.join(docs_path, "user-guide")
    create_directory(user_guide_path)
    # _category_.json for user-guide
    create_markdown_file(
        os.path.join(user_guide_path, "_category_.json"),
        '{\n  "label": "User Guide",\n  "position": 2,\n  "link": {\n    "type": "generated-index",\n    "description": "Learn how to use our product."\n  }\n}',
        None
    )
    # getting-started.md
    create_markdown_file(
        os.path.join(user_guide_path, "getting-started.md"),
        "# Getting Started\n\nFollow these steps to quickly set up and start using the product.",
        {"id": "getting-started", "title": "Getting Started", "sidebar_position": 1}
    )
    # features.md
    create_markdown_file(
        os.path.join(user_guide_path, "features.md"),
        "# Key Features\n\nExplore the various features offered by our application.",
        {"id": "features", "title": "Features", "sidebar_position": 2}
    )

    # api-reference subfolder
    api_reference_path = os.path.join(docs_path, "api-reference")
    create_directory(api_reference_path)
    # _category_.json for api-reference
    create_markdown_file(
        os.path.join(api_reference_path, "_category_.json"),
        '{\n  "label": "API Reference",\n  "position": 3,\n  "link": {\n    "type": "generated-index",\n    "description": "Detailed documentation for our API."\n  }\n}',
        None
    )
    # endpoints.md
    create_markdown_file(
        os.path.join(api_reference_path, "endpoints.md"),
        "# API Endpoints\n\nComprehensive list and details of all available API endpoints.",
        {"id": "api-endpoints", "title": "Endpoints", "sidebar_position": 1}
    )
    # authentication.md
    create_markdown_file(
        os.path.join(api_reference_path, "authentication.md"),
        "# API Authentication\n\nInformation on how to authenticate your API requests.",
        {"id": "authentication", "title": "Authentication", "sidebar_position": 2}
    )

    print("\nSimplified Docusaurus nested docs structure created successfully!")
    print(f"You'll find your new structure in the '{base_path}' directory.")

# To run the function and create the structure:
if __name__ == "__main__":
    create_docusaurus_nested_docs_structure()