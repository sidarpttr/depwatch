import requests

def get_latest_version(package_name):
    try:
        url = f"https://pub.dev/api/packages/{package_name}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return data["latest"]["version"]
        
        return None
    except Exception:
        return None