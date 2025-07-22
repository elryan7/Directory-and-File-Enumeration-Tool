import requests
from concurrent.futures import ThreadPoolExecutor
import sys

def test_url(base_url, path):
    """Test a URL for existence."""
    url = f"{base_url.rstrip('/')}/{path.strip()}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 404:
            return url, response.status_code
    except requests.RequestException:
        pass
    return None, None

def enumerate_paths(base_url, wordlist):
    """Enumerate directories and files using a wordlist."""
    results = []
    with open(wordlist, 'r') as f:
        paths = f.readlines()
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(test_url, base_url, path) for path in paths]
        for future in futures:
            url, status = future.result()
            if url and status:
                results.append((url, status))
                print(f"Found: {url} (Status: {status})")
    
    with open('enum_report.txt', 'w') as f:
        for url, status in results:
            f.write(f"URL: {url}\nStatus: {status}\n\n")
    
    print("Enumeration complete. Results saved to enum_report.txt")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 dir_enumerator.py <base_url> <wordlist>")
        sys.exit(1)
    
    base_url = sys.argv[1]
    wordlist = sys.argv[2]
    enumerate_paths(base_url, wordlist)