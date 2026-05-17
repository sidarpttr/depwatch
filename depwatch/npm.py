import requests

def get_latest_version(package_name):
    try:
        url = f"https://registry.npmjs.org/{package_name}/latest"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("version")
        
        return None
    except Exception:
        return None
