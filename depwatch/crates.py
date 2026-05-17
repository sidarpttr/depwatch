import requests

def get_latest_version(package_name):
    try:
        url = f"https://crates.io/api/v1/crates/{package_name}"
        headers = {"User-Agent": "depwatch/0.1.0"}
        response = requests.get(url, timeout=5, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data["crate"]["newest_version"]
        
        return None
    except Exception:
        return None