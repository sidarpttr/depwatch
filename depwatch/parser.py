import re
import toml
import json

def parse_requirements(filepath="requirements.txt"):
    packages = []
    
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            
            if not line or line.startswith("#"):
                continue
            
            match = re.match(r"^([a-zA-Z0-9_\-]+)==([^\s]+)", line)
            if match:
                packages.append({
                    "name": match.group(1),
                    "version": match.group(2)
                })
            else:
                name = re.match(r"^([a-zA-Z0-9_\-]+)", line)
                if name:
                    packages.append({
                        "name": name.group(1),
                        "version": None
                    })
    
    return packages

def parse_package_json(filepath):
    packages = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            deps = data.get("dependencies", {})
            dev_deps = data.get("devDependencies", {})
            all_deps = {**deps, **dev_deps}
            
            for name, version in all_deps.items():
                version = re.sub(r'^[~^><=]+', '', version)
                packages.append({
                    "name": name,
                    "version": version
                })
    except Exception:
        pass
    return packages

def parse_pubspec_yaml(filepath):
    packages = []
    try:
        import yaml
        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            
            deps = data.get("dependencies", {})
            dev_deps = data.get("dev_dependencies", {})
            all_deps = {**deps, **dev_deps}
            
            for name, version in all_deps.items():
                if name == "flutter" or name == "dart":
                    continue
                if isinstance(version, dict):
                    version = version.get("version", None)
                if isinstance(version, str):
                    version = re.sub(r'^[~^><=^]+', '', version).strip()
                packages.append({
                    "name": name,
                    "version": version or None
                })
    except Exception:
        pass
    return packages

def parse_cargo_toml(filepath):
    packages = []
    try:
        import toml
        with open(filepath, "r", encoding="utf-8") as f:
            data = toml.load(f)
            
            deps = data.get("dependencies", {})
            dev_deps = data.get("dev-dependencies", {})
            all_deps = {**deps, **dev_deps}
            
            for name, version in all_deps.items():
                if isinstance(version, dict):
                    version = version.get("version", None)
                if isinstance(version, str):
                    version = re.sub(r'^[~^><=]+', '', version).strip()
                packages.append({
                    "name": name,
                    "version": version or None
                })
    except Exception:
        pass
    return packages