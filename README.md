# Static Site Generator

A static site generator I built in Python that converts Markdown files into a fully functional HTML website. The live site is a Tolkien fan page deployed on GitHub Pages.

## Live Site

[https://itsYuuuka.github.io/static-site-generator/](https://itsYuuuka.github.io/static-site-generator/)

## Overview

Built entirely from scratch with no third-party libraries. I wrote a custom Markdown parser, an HTML renderer, and a recursive page generator that takes raw .md files all the way to a deployed website.

## How It Works

1. Static files (CSS, images) are copied from `static/` to the output directory
2. Markdown files in `content/` are recursively converted to HTML pages
3. Each page is generated using `template.html` as the base layout
4. The output is written to the `docs/` directory and deployed via GitHub Pages

## Features

- Custom Markdown parser supporting headings, bold, italic, code, links, images, blockquotes, and lists
- Recursive page generation that mirrors the content directory structure
- Configurable base path for subdirectory hosting (e.g. GitHub Pages)
- 64 unit tests covering all parsing and rendering logic

## Tech Stack

- Python
- No third-party dependencies

## Running Locally

```bash
./main.sh
```

Then open `http://localhost:8888` in your browser.

## Running Tests

```bash
./test.sh
```

## Building for Production

```bash
./build.sh
```
