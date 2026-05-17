import requests

def get_vulnerabilities(package_name, version, ecosystem="PyPI"):
    try:
        url = "https://api.osv.dev/v1/query"
        payload = {
            "package": {
                "name": package_name,
                "ecosystem": ecosystem
            },
            "version": version
        }
        
        response = requests.post(url, json=payload, timeout=5)
        
        if response.status_code != 200:
            return []
        
        data = response.json()
        vulns = []
        
        for vuln in data.get("vulns", []):
            cve_id = None
            for alias in vuln.get("aliases", []):
                if alias.startswith("CVE-"):
                    cve_id = alias
                    break
            
            vulns.append({
                "id": vuln.get("id"),
                "cve": cve_id,
                "summary": vuln.get("summary", "No description"),
            })
        
        return vulns
    
    except Exception:
        return []