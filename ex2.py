#Slicing email
email=input("Enter your email")
at=email.find("@")#index=email.index("@")
username= email[:at]
domain=email[at+1:]
print(f"Your username is {username} and domain is {domain}")

