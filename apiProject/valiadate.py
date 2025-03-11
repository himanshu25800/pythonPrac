import datetime


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


def validateSalary(salary):

    if salary>=0:
        return True
    return False


def validateGender(gender):
    gender = str.lower(gender)

    if gender == 'male' or gender == 'female':
        return True
    return False

def validateDob(dob):
    dob = datetime.datetime.strptime(dob, "%d/%m/%y")

    if dob > datetime.datetime.now():
        return False
    
    return True

def validateStr(str):
    if len(str)==0:
        return False
    return True