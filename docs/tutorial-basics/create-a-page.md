---
sidebar_position: 1
---

# Create a Page

Add **Markdown or React** files to `src/pages` to create a **standalone page**:

- `src/pages/index.js` → `localhost:3000/`
- `src/pages/foo.md` → `localhost:3000/foo`
- `src/pages/foo/bar.js` → `localhost:3000/foo/bar`

## Create your first React Page

Create a file at `src/pages/my-react-page.js`:

```jsx title="src/pages/my-react-page.js"
import React from 'react';
import Layout from '@theme/Layout';

export default function MyReactPage() {
  return (
    <Layout>
      <h1>My React page</h1>
      <p>This is a React page</p>
    </Layout>
  );
}
```

A new page is now available at [http://localhost:3000/my-react-page](http://localhost:3000/my-react-page).

## Create your first Markdown Page

Create a file at `src/pages/my-markdown-page.md`:

```mdx title="src/pages/my-markdown-page.md"
# My Markdown page

This is a Markdown page
```

A new page is now available at [http://localhost:3000/my-markdown-page](http://localhost:3000/my-markdown-page).


## Create your first Markdown Page with Front Matter

```mdx title="src/pages/my-markdown-page-front-matter.md"
---
id: learn-more-about-docusaurus
title: Learn More About Docusaurus
description: Explore advanced features and customization options in Docusaurus.
slug: /advanced-concepts/learn-more
keywords: [docusaurus, features, customization, guide, documentation]
image: https://docusaurus.io/img/docusaurus-social-card.jpg
format: mdx
unlisted: false
hide_title: false
---

# Learn More About Docusaurus

Welcome to the advanced section! This document dives deeper into various aspects of Docusaurus, from theming to plugin development.

## Theming

Docusaurus offers robust theming capabilities...

## Plugins

Extend Docusaurus's functionality with custom plugins...

## Deployment

Learn how to deploy your Docusaurus site...

```
