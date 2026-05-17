# depwatch

Scan your project dependencies for outdated versions and security vulnerabilities (CVE).

## Installation

```bash
pip install depwatch
```

## Usage

```bash
cd your-project
depwatch
```

## Supported Ecosystems

| Language   | File             |
|------------|------------------|
| Python     | requirements.txt |
| JavaScript | package.json     |
| Dart       | pubspec.yaml     |
| Rust       | Cargo.toml       |

## How it works

depwatch walks your project directory, detects dependency files, and queries [OSV.dev](https://osv.dev) for known vulnerabilities. Results are displayed as a table with CVE IDs and CVSS severity scores.

## License

MIT
