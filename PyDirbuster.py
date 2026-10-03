import requests
from concurrent.futures import ThreadPoolExecutor

# آدرس هدف را اینجا وارد کن
TARGET_URL = "http://example.com"

# لیست دایرکتوری‌های مهم برای تست
WORDLIST = [
    "admin", "login", "dashboard", "images", "upload", 
    "uploads", "css", "js", "api", "config", "backup", 
    "db", "panel", "user", "robots.txt", ".env", ".git"
]

# هدر مرورگر برای دور زدن بلاک‌های ساده
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def check_directory(directory):
    url = f"{TARGET_URL.rstrip('/')}/{directory}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=4, allow_redirects=False)
        status = response.status_code
        
        if status == 200:
            print(f"[+] [200 OK] -> {url}")
        elif status in [301, 302]:
            location = response.headers.get('Location', '')
            print(f"[>] [{status} Redirect] -> {url} => {location}")
        elif status == 403:
            print(f"[!] [403 Forbidden] -> {url}")
        elif status == 500:
            print(f"[x] [500 Server Error] -> {url}")
        else:
            print(f"[-] [{status}] -> {url}") 
    except requests.RequestException:
        pass

def main():
    print(f"[*] Starting Directory Scan on: {TARGET_URL}")
    print(f"[*] Loaded {len(WORDLIST)} paths to test...\n" + "-"*50)
    
    # اجرای همزمان با ۱۰ رشته‌سیم (Thread) برای سرعت بالا
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(check_directory, WORDLIST)
        
    print("-" * 50 + "\n[*] Scan Completed!")

if __name__ == "__main__":
    main()