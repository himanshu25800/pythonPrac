import datetime
import re

#regex use
def validateEmail(email):

    pattern = r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z]+).([a-zA-Z]+)$'
    
    # pattern = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'


    result = bool(re.match(pattern , email))
    return result


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


#age 18+
def validateDob(dob):
    dob = datetime.datetime.strptime(dob, "%d/%m/%Y")
    today = datetime.datetime.today()

    if dob > datetime.datetime.now():
        return False

    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age <18:
        return False

    return True

def validateStr(str):
    if len(str)==0:
        return False
    return True


def validateData(data):
    message = []
    result = True

    id = data['id']

    fname = data['fname']
    status = validateStr(fname)
    if not status:
        result = False
        message.append('First Name Should not be empty')
        
    lname = data['lname']
    status = validateStr(lname)
    if not status:
        result = False
        message.append('Last Name Should not be empty')

    city = data['city']
    status = validateStr(city)
    if not status:
        result = False
        message.append('City Should not be empty')
        
    phonenumber = data['phonenumber']
    status = validatePhone(phonenumber)
    if not status:
        result = False
        message.append('Phone Number must be 10 digit')

    dob = data['dob']
    status = validateDob(dob)
    if not status:
        result = False
        message.append('Invalid date of birth')
        
    dob = datetime.datetime.strptime(dob, "%d/%m/%Y").strftime("%Y-%m-%d")
    email = data['email']
    status  = validateEmail(email)
    if not status:
        result = False
        message.append('Wrong email format')
   
        
    gender = data['gender']
    status = validateGender(gender)
    if not status:
        result = False
        message.append('Invalid Gender')
    

    return result, message