# depwatch

Scan your project dependencies for outdated versions and security vulnerabilities (CVE).

## Features

- Python (`requirements.txt`) support
- Node.js (`package.json`) support
- CVE detection via [OSV.dev](https://osv.dev)
- CVSS severity scoring
- Fast batch vulnerability queries

## Installation

```bash
pip install depwatch
```

## Usage

```bash
cd your-project
depwatch scan
```

## Supported Ecosystems

| Language   | File             | Status |
|------------|------------------|--------|
| Python     | requirements.txt | stable |
| JavaScript | package.json     | stable |
| Dart       | pubspec.yaml     | soon   |
| Rust       | Cargo.toml       | soon   |

## License

MIT