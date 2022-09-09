# get email from the user and split it as two parts such as username and domain name using @
# then split the domain name into domain and ext using .

def sliceEmail():    
    inputEmail = input("Enter the email: ")

    (username, domainName) = inputEmail.split("@")
    (domain, extension) = domainName.split(".")

    print("Username     : ", username)
    print("Domain       : ", domain)
    print("Extension    : ", extension)

sliceEmail()