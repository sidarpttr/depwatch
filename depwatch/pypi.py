import requests

def get_latest_version(package_name):
    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return data["info"]["version"]
        
        return None
    except Exception:
        return None