import re
email = input("Enter your email address : ").strip().lower()#take input in lower cae 
if re.search(r"^[^@]+@[^@]+\.edu$", email) or re.search(r"^[^@]+@gmail\.com$", email):
    print("valid")
else :
    print("invalid")
    
email = input("Enter your email address : ").strip()
if re.search(r"^\w+\w\.edu$", email, re.IGNORECASE) or re.search(r"^\w+@gmail\.com$", email, re.IGNORECASE):
    print("valid")
else :
    print("invalid")