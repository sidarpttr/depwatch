import typer
import os
from depwatch.parser import parse_requirements, parse_package_json, parse_pubspec_yaml, parse_cargo_toml
from depwatch.pypi import get_latest_version as pypi_latest
from depwatch.npm import get_latest_version as npm_latest
from depwatch.pub import get_latest_version as pub_latest
from depwatch.crates import get_latest_version as crates_latest
from depwatch.osv import get_vulnerabilities
from depwatch.display import show_results

def scan(
    path: str = typer.Argument(".", help="Directory to scan")
):
    """Scan dependencies for vulnerabilities."""
    
    all_packages = []
    
    for root, dirs, files in os.walk(path):
        for skip in ["node_modules", "venv", ".dart_tool", "target"]:
            if skip in dirs:
                dirs.remove(skip)
            
        for file in files:
            filepath = os.path.join(root, file)
            
            if file == "requirements.txt":
                packages = parse_requirements(filepath)
                for p in packages:
                    p["ecosystem"] = "PyPI"
                all_packages.extend(packages)
                
            elif file == "package.json":
                packages = parse_package_json(filepath)
                for p in packages:
                    p["ecosystem"] = "npm"
                all_packages.extend(packages)
                
            elif file == "pubspec.yaml":
                packages = parse_pubspec_yaml(filepath)
                for p in packages:
                    p["ecosystem"] = "Pub"
                all_packages.extend(packages)
                
            elif file == "Cargo.toml":
                packages = parse_cargo_toml(filepath)
                for p in packages:
                    p["ecosystem"] = "crates.io"
                all_packages.extend(packages)
    
    if not all_packages:
        typer.echo("No packages found.")
        raise typer.Exit()
    
    results = []
    total = len(all_packages)
    print(f"Scanning {total} packages...\n")
    
    ecosystem_map = {
        "PyPI": pypi_latest,
        "npm": npm_latest,
        "Pub": pub_latest,
        "crates.io": crates_latest,
    }
    
    osv_ecosystem_map = {
        "PyPI": "PyPI",
        "npm": "npm",
        "Pub": "Pub",
        "crates.io": "crates.io",
    }
    
    for idx, pkg in enumerate(all_packages, 1):
        print(f"[{idx}/{total}] {pkg['name']}", end="\r")
        
        latest_fn = ecosystem_map.get(pkg["ecosystem"])
        latest = latest_fn(pkg["name"]) if latest_fn else None
        
        osv_eco = osv_ecosystem_map.get(pkg["ecosystem"], pkg["ecosystem"])
        vulns = get_vulnerabilities(pkg["name"], pkg["version"] or "", osv_eco)
        
        results.append({
            "ecosystem": pkg["ecosystem"],
            "name": pkg["name"],
            "version": pkg["version"],
            "latest": latest,
            "vulns": vulns
        })
    
    print(" " * 40, end="\r")
    show_results(results)

def main():
    typer.run(scan)