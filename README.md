# Static Site Generator

A static site generator built in Python that converts Markdown files into a fully functional HTML website, deployed on GitHub Pages.

## Overview

Built from scratch without any third-party libraries. Takes Markdown content files and an HTML template and generates a complete static website ready to be served or deployed.

## How It Works

1. Static files (CSS, images) are copied from `static/` to the output directory
2. Markdown files in `content/` are recursively converted to HTML pages
3. Each page is generated using `template.html` as the base layout
4. The output is written to the `docs/` directory and deployed via GitHub Pages

## Tech Stack

- Python 3
- No third-party dependencies