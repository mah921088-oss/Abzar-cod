import socket

# ۱. تعریف هدف و بازه پورت‌ها
target = "scanme.nmap.org"  # می‌توانید آی‌پی سیستم خودت یا دامنه مورد نظر را بگذاری
ports = [21, 22, 80, 443, 8080, 3306]  # پورت‌های رایج برای تست

print(f"[*] Starting port scan for: {target}\n")

# ۲. پیمایش تک‌تک پورت‌ها
for port in ports:
    try:
        # ساخت سوکت TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)  # مهلت ۱ ثانیه‌ای برای پاسخ
        
        # ۳. تست اتصال (Three-Way Handshake)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] Port {port:<5} [OPEN]")
            
        s.close()
    except Exception:
        pass

print("\n[*] Scan Finished.")