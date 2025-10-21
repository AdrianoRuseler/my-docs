# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

## Installation

```bash
npx create-docusaurus@latest moodle-docs classic --javascript
```

[Diagrams](https://docusaurus.io/docs/markdown-features/diagrams)

```bash
npm install --save @docusaurus/theme-mermaid
```

[Math Equations](https://docusaurus.io/docs/markdown-features/math-equations)

```bash
npm install --save remark-math@6 rehype-katex@7
```

## Clone repo

```bash
git clone https://github.com/AdrianoRuseler/my-docs.git
cd my-docs
npm i
```

## Local Development

```bash
cd my-docs
npm run start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```bash
npm run build
npm run serve
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Deployment

Using SSH:

```bash
set GIT_USER=AdrianoRuseler
npm run deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

## Upgrade Docusaurus Packages

To upgrade Docusaurus packages with the latest version, run the following command:

```bash
npm i @docusaurus/core@latest @docusaurus/preset-classic@latest @docusaurus/module-type-aliases@latest @docusaurus/types@latest
```
