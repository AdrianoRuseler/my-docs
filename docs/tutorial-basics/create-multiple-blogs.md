---
id: multiple-blogs
title: Create Multiple Blogs
slug: /multiple-blogs
---


Just like with multiple docs folders, Docusaurus allows you to create multiple blogs by leveraging multiple instances of the `@docusaurus/plugin-content-blog` plugin. This is incredibly useful if you want to have distinct blog sections on your site, for example:

  * A main company blog
  * A developer blog
  * A product updates blog
  * A news or announcements section

Here's how to set it up:

### 1\. Create your additional blog folders

First, create the directories for your new blogs. Let's say you have the default `blog` folder, and you want to add `dev-blog` and `news`. Your project structure might look like this:

```
my-docusaurus-site/
├── blog/
│   ├── 2023-01-01-hello.md
│   └── ...
├── dev-blog/
│   ├── 2024-03-15-tech-update.md
│   └── ...
├── news/
│   ├── 2024-07-20-company-announcement.md
│   └── ...
├── src/
├── static/
├── docusaurus.config.js
└── ...
```

### 2\. Configure `docusaurus.config.js`

You'll modify your `docusaurus.config.js` to add multiple instances of the `@docusaurus/plugin-content-blog`. Each instance will point to a different blog folder and have a unique `id`.

```javascript
// docusaurus.config.js

/** @type {import('@docusaurus/types').Config} */
const config = {
  // ... other configurations

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          // Default docs configuration
          path: 'docs',
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          // This is for your primary 'blog' folder
          path: './blog', // The default 'blog' folder
          routeBasePath: 'blog', // Base URL for this blog (e.g., yoursite.com/blog/...)
          showReadingTime: true,
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-content-blog',
      /** @type {import('@docusaurus/plugin-content-blog').Options} */
      {
        id: 'devBlog', // Unique ID for this blog instance
        path: './dev-blog', // Path to your developer blog folder
        routeBasePath: 'dev-blog', // Base URL for these blog posts (e.g., yoursite.com/dev-blog/...)
        showReadingTime: true,
        blogTitle: 'Developer Blog',
        blogDescription: 'Updates and articles for developers.',
        // You can add more options specific to this blog, like:
        // postsPerPage: 5,
        // feedOptions: { type: 'all' },
      },
    ],
    [
      '@docusaurus/plugin-content-blog',
      /** @type {import('@docusaurus/plugin-content-blog').Options} */
      {
        id: 'news', // Unique ID for this blog instance
        path: './news', // Path to your news blog folder
        routeBasePath: 'news', // Base URL for news posts (e.g., yoursite.com/news/...)
        showReadingTime: false, // Maybe you don't need reading time for news
        blogTitle: 'Company News',
        blogDescription: 'Latest announcements and company updates.',
      },
    ],
  ],
  // ... rest of your config
};

module.exports = config;
```

**Key points in the configuration:**

  * **`plugins` array:** This is where you add additional instances of the blog plugin.
  * **`id`:** **Crucial\!** Each blog instance *must* have a unique `id`. This is how Docusaurus distinguishes between them. The default blog instance (configured within `preset-classic`) has an implicit `id` of `default`.
  * **`path`:** Points to the directory where the Markdown files for that specific blog are located.
  * **`routeBasePath`:** Defines the URL segment for that blog. For example, if `routeBasePath: 'dev-blog'`, your posts will be at `yoursite.com/dev-blog/my-post`.
  * **Other options:** You can customize options like `blogTitle`, `blogDescription`, `postsPerPage`, `showReadingTime`, etc., independently for each blog instance.

### 3\. Add Blog Posts

Create Markdown files in your newly created blog directories. Remember to follow Docusaurus's blog post naming conventions (e.g., `YYYY-MM-DD-your-post-title.md`) or use front matter to specify the date.

Example `dev-blog/2024-03-15-tech-update.md`:

```markdown
---
title: "Latest Tech Update"
description: "An overview of recent technical improvements."
authors: ["dev-team"]
tags: ["engineering", "release"]
---

# Latest Tech Update

This is a technical blog post about our recent system changes...
```

Example `news/2024-07-20-company-announcement.md`:

```markdown
---
title: "New Partnership Announced!"
description: "Exciting news about our collaboration."
authors: ["pr-team"]
tags: ["company", "partnerships"]
---

# New Partnership Announced!

We are thrilled to announce our new partnership with...
```

### 4\. Link in your Navbar

Finally, update your `docusaurus.config.js` to add links to these new blog sections in your navbar:

```javascript
// docusaurus.config.js

navbar: {
    title: 'My Site',
    // ...
    items: [
      {
        to: '/blog', // Link to your default blog
        label: 'Main Blog',
        position: 'left',
        activeBaseRegex: `/blog/`,
      },
      {
        to: '/dev-blog', // Link to your developer blog
        label: 'Developer Blog',
        position: 'left',
        activeBaseRegex: `/dev-blog/`,
      },
      {
        to: '/news', // Link to your news blog
        label: 'News',
        position: 'left',
        activeBaseRegex: `/news/`,
      },
      // ... other navbar items (docs, etc.)
    ],
  },
```

Now, when you run Docusaurus (`npm run start` or `yarn start`), you'll have distinct URLs and sections for each of your blogs\!