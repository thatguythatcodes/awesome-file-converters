# Awesome File Converters

> A curated and regularly verified directory of file-conversion tools, apps, libraries, APIs, and commands.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Validate data](https://github.com/thatguythatcodes/awesome-file-converters/actions/workflows/validate.yml/badge.svg)](https://github.com/thatguythatcodes/awesome-file-converters/actions/workflows/validate.yml)
[![CC0](https://img.shields.io/badge/data-CC0-blue.svg)](LICENSE)

Finding a converter is easy. Finding the right converter, one that supports your formats, platform, budget, batch size, and privacy needs, is not. This project makes those trade-offs visible.

**25 verified converters · 8 categories · machine-readable data · no affiliate links**

## Contents

- [Quick picks](#quick-picks)
- [Browse by format](#browse-by-format)
- [Converters](#converters)
- [What makes this list different](#what-makes-this-list-different)
- [How entries are evaluated](#how-entries-are-evaluated)
- [Contributing](#contributing)

## Quick picks

| Need | Good starting point | Why |
|---|---|---|
| Free browser conversion | [Crest Convert](https://crestconvert.com/) | Broad format support with no signup or limits |
| Images in a browser | [Squoosh](https://squoosh.app/) | Local processing and detailed compression controls |
| Images on the command line | [ImageMagick](https://imagemagick.org/) | Scriptable and supports many image formats |
| Audio or video | [FFmpeg](https://ffmpeg.org/) | Broad format support and extensive controls |
| Documents and markup | [Pandoc](https://pandoc.org/) | Excellent for converting between document markup formats |
| E-books | [Calibre](https://calibre-ebook.com/) | Mature desktop and command-line e-book tooling |
| General web conversion | [CloudConvert](https://cloudconvert.com/) | Wide format coverage and an API |

## Browse by format

Open the **[full converter catalog](CATALOG.md)** to browse working category tables for images, documents, audio, video, e-books, structured data, presentations, and archives. Every converter links to format evidence and a detailed record.

The canonical, machine-readable index lives in [`data/converters.json`](data/converters.json). A conversion-pair index will be generated from this data as coverage grows.

## Converters

| Converter | Type | Best for | Free option | Local processing | Open source | Batch |
|---|---|---|---:|---:|---:|---:|
| [Squoosh](https://squoosh.app/) | Web app | Image compression and conversion | Yes | Yes | Yes | No |
| [Crest Convert](https://crestconvert.com/) | Web app | Free, no-signup browser conversion | Yes | Yes | No | Yes |
| [VERT](https://vert.sh/) | Web app / self-hosted | Broad browser conversion | Yes | Mixed | Yes | Yes |
| [ConvertX](https://github.com/C4illin/ConvertX) | Self-hosted | Broad Docker-based conversion | Yes | Yes | Yes | Yes |
| [Stirling PDF](https://www.stirlingpdf.com/) | Web / desktop / self-hosted | PDF conversion and workflows | Yes | Yes | Yes | Yes |
| [HandBrake](https://handbrake.fr/) | Desktop / CLI | Video transcoding | Yes | Yes | Yes | Yes |
| [ImageMagick](https://imagemagick.org/) | CLI / library | Automated image workflows | Yes | Yes | Yes | Yes |
| [FFmpeg](https://ffmpeg.org/) | CLI / libraries | Audio and video | Yes | Yes | Yes | Yes |
| [Pandoc](https://pandoc.org/) | CLI / library | Markup and documents | Yes | Yes | Yes | Yes |
| [Calibre](https://calibre-ebook.com/) | Desktop / CLI | E-books | Yes | Yes | Yes | Yes |
| [LibreOffice](https://www.libreoffice.org/) | Desktop / CLI | Office documents | Yes | Yes | Yes | Yes |
| [CloudConvert](https://cloudconvert.com/) | Web app / API | Broad format coverage | Limited | No | No | Yes |
| [Convertio](https://convertio.co/) | Web app | Quick general conversion | Limited | No | No | Yes |
| [VLC](https://www.videolan.org/vlc/) | Desktop / CLI | Common audio and video conversions | Yes | Yes | Yes | Yes |
| [Inkscape](https://inkscape.org/) | Desktop / CLI | Vector and raster graphics | Yes | Yes | Yes | Yes |
| [Transmute](https://transmute.sh/) | Self-hosted / API | Private automated conversion | Yes | Yes | Yes | Yes |
| [File Converter](https://file-converter.io/) | Desktop | Windows context-menu conversion | Yes | Yes | Yes | Yes |
| [XnConvert](https://www.xnview.com/en/xnconvert/) | Desktop | Batch image processing | Limited | Yes | No | Yes |
| [SoX](https://sourceforge.net/projects/sox/) | CLI / library | Audio conversion and processing | Yes | Yes | Yes | Yes |
| [Ghostscript](https://www.ghostscript.com/) | CLI / library | PostScript and PDF workflows | Yes | Yes | Yes | Yes |
| [BentoPDF](https://bentopdf.com/) | Web app / self-hosted | Client-side PDF conversion | Yes | Yes | Yes | Yes |
| [FreeConvert](https://www.freeconvert.com/) | Web app / API | General hosted conversion | Limited | No | No | Yes |
| [Zamzar](https://www.zamzar.com/) | Web app / API | General hosted conversion | Limited | No | No | Yes |
| [MarkItDown](https://github.com/microsoft/markitdown) | CLI / library | Files to Markdown | Yes | Yes | Yes | Yes |
| [OCRmyPDF](https://ocrmypdf.readthedocs.io/) | CLI / library | Searchable scanned PDFs | Yes | Yes | Yes | No |

This table is intentionally concise. See the dataset for formats, platforms, account requirements, pricing notes, and verification dates.

## What makes this list different

- **Evidence-backed:** Every entry links to format documentation, not just a homepage.
- **Decision-friendly:** Compare free access, local processing, batch support, platform, and open-source status.
- **Structured:** The JSON dataset can power scripts, applications, and a future searchable website.
- **Curated:** Affiliate links, referral codes, scraped bulk submissions, and unverifiable claims are rejected.
- **Maintained:** Every record carries a manual verification date and passes automated schema checks.

## How entries are evaluated

Every entry must:

1. Perform a real file conversion, not merely rename an extension.
2. Have a working official product or project page.
3. State its supported formats or link to authoritative documentation.
4. Disclose whether files are processed locally or uploaded.
5. Describe free-tier limits, account requirements, and watermarks when applicable.
6. Include a `last_verified` date.

Inclusion is not an endorsement. “Local processing” means the conversion itself happens on the user's device; it does not make broader claims about analytics or network requests.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md), add or update the structured data, and run:

```bash
python3 scripts/validate.py
python3 scripts/generate_catalog.py
```

Commercial tools are welcome when they are genuinely useful and their limitations are disclosed. Affiliate links, referral codes, keyword-stuffed descriptions, and unverifiable claims are not accepted.

## Roadmap

- Expand the verified seed list
- Generate pages for popular conversion pairs
- Add automated link-health reporting
- Record format-specific caveats and quality notes
- Publish a searchable companion site backed by the same dataset

## Disclaimer

This directory is provided for general informational purposes only and on an **as-is** basis, without warranties of any kind. Listings may be inaccurate, unavailable, unsafe, or subject to changed pricing and terms. The maintainers do not operate or control third-party tools and do not endorse them merely by listing them.

You are responsible for evaluating a tool before using it, protecting sensitive files, keeping backups, and complying with applicable laws and third-party terms. To the fullest extent permitted by law, the maintainers and contributors will not be liable for any loss, damage, data exposure, file corruption, or other consequence arising from use of this directory or any listed tool.

## License

The directory data and documentation are dedicated to the public domain under [CC0 1.0](LICENSE). Product names and trademarks belong to their respective owners.
