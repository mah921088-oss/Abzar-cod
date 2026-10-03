import socket


domain = "github.com"
words = ["api" , "pages" , "gits" , "admin", "mail" ,"blog" , "api" , "dev" , "test" , "shop"]

print(f"[*] starting scan for: {domain}\n")
 
 
for word in words:
     
     subdomain = f"{word}.{domain}"
     
     try:
         
         ip = socket.gethostbyname(subdomain)
         print (f"[*] Found: {subdomain}  ip: {ip}")
     except socket.gaierror:
             
             pass
            
print ("\n[*] scan Finished.")     