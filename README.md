# Notion VimWiki Markdown Export

A Bash script in combination with a [Panflute](https://github.com/sergiocorreia/panflute/) Pandoc filter to convert Notion exports to a format suitable for [VimWiki](https://github.com/vimwiki/vimwiki/). See [What Does It Do?](#what-does-it-do) for a list of ways it modifies the export.

## Usage

Start by cloning this repository and `cd`'ing into it:

```bash
git clone https://github.com/mtoohey31/notion-vimwiki-export
cd notion-vimwiki-export
```

Then install the required python modules:

```bash
pip3 install -r requirements.txt
```

Then run the script, providing it the path to your unzipped notion export (you will have to replace the variable below with the path):

```bash
./notion-vimwiki-export $PATH_TO_UNZIPPED_NOTION_EXPORT
```

That should be it! It will run without output unless it runs into an issue, like a good command line application, so don't worry if you're not seeing anything happening. If you run into any problems, feel free to open an issue on this repository.

## What Does It Do?

Here's a list of ways the script currently modifies the export:

- Increases the depth of each header by 1, other than the first header.
- Decodes local file links so they're more readable, i.e.: `[A File](./A%20File.pdf)` becomes `[A File](./A File.pdf)`.
- Places properties from databases in YAML front-matter instead of in the markdown text.
- Removes CSV files to reduce clutter.
- Renames folders and files containing non-ascii characters.
- Formats markdown files first with Pandoc (which happens when the filter is being run), then with [prettier](https://prettier.io/).

## What Could It Do?

Here's a list of ways I'd like to improve the script in the future:

- Handle file/folder name collisions.
- Be more selective about which characters are removed from filenames (after testing which characters break prettier).
- Escape local paths.
- Relocate file properties to inside the object folder and fix the path.

## Similar Projects

- [Notion-to-Obsidian-Converter](https://github.com/connertennery/Notion-to-Obsidian-Converter)

- [Notion-2-Obsidan](https://github.com/visualcurrent/Notion-2-Obsidan)
