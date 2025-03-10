def validateEMail(email):
    domain = email.split('@')[-1]
    address = email.split('@')[0]
    address = str.lower(address)
    # print(domain,address)
    if domain != "gmail.com":
        return (False , email)
    email = address+"@"+domain
    return (True, email)


def validatePhone(phoneNumber):
    
    if len(phoneNumber)<10 or len(phoneNumber)>10 :
        return False
    return True