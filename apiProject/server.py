from flask import Flask, jsonify, request
import psycopg2
from datetime import datetime
import valiadate


app = Flask(__name__)
connection = psycopg2.connect(database='Employee', user='postgres', password='thinksys@123', host='localhost', port=5432)
if connection:
    print("Database Connected successfully")


@app.route('/', methods=['GET'])
def greet():
    return jsonify(message="All fine !")

@app.route('/getall', methods=['GET'])
def getAll():
    with connection:
        with connection.cursor() as cursor:
            pageNumber = int(request.args.get('pagenumber',1))
            pageSize = int(request.args.get('pagesize',10))
            limit = pageSize
            offset = pageSize*(pageNumber-1)
            cursor.execute('select * from employee order by employeeId asc limit %s offset %s',(limit,offset))
            result = cursor.fetchall()
            return jsonify(message={'record':cursor.rowcount,'info':result})

@app.route('/getone/', methods=['GET'])
def getById():
    with connection:
        with connection.cursor() as cursor:
            id = request.args.get('id') 
            cursor.execute('select * from employee where employeeId=%s',(id,))
            result = cursor.fetchone()
            return jsonify(message={'record':cursor.rowcount,'info':result})


@app.route('/insert/', methods=['POST'])
def post():
    with connection:
        with connection.cursor() as cursor:
            res = request.get_json()
            # print(res)
            data = res['data']
            # print(len(data))
            # print(data[0],data[1])
            message =[]

            i = 0
            while(i<len(data)):
                id = data[i]['id']
                fname = data[i]['fname']
                status = valiadate.validateStr(fname)
                if not status:
                    message.append({'rowsAffected':0, 'data': 'First Name Should not be empty'})
                    i+=1
                    continue
                lname = data[i]['lname']
                status = valiadate.validateStr(lname)
                if not status:
                    message.append({'rowsAffected':0, 'data': 'Last Name Should not be empty'})
                    i+=1
                city = data[i]['city']
                status = valiadate.validateStr(city)
                if not status:
                    message.append({'rowsAffected':0, 'data': 'City Should not be empty'})
                    i+=1
                phonenumber = data[i]['phonenumber']
                status = valiadate.validatePhone(phonenumber)
                if not status:
                    message.append({'rowsAffected':0, 'data': 'Phone Number must be 10 digit'})
                    i+=1
                dob = data[i]['dob']
                status = valiadate.validateDob(dob)
                if not status:
                    message.append({'rowsAffected':0, 'data': 'Invalid date of birth'})
                    i+=1
                dob = datetime.strptime(dob, "%d/%m/%Y").strftime("%Y-%m-%d")
                email = data[i]['email']
                status, email  = valiadate.validateEMail(email)
                if not status:
                    message.append({'rowsAffected':0, 'data': 'Wrong email format'})
                    i+=1
                    continue
                    
                gender = data[i]['gender']
                
                # print(data[i]['id'], data[i]['fname'], data[i]['lname'], data[i]['city'],data[i]['phonenumber'],data[i]['dob'],data[i]['email'],data[i]['gender'])

                # cursor.execute('Insert into employee(employeeId, firstname, lastname, city, dateOfBirth, phoneNumber, email, gender) values(%s,%s,%s,%s,%s,%s,%s,%s)',(id, fname, lname, city, dob, phonenumber, email, gender))

                cursor.execute('Insert into employee(employeeId, firstname, lastname, city, dateOfBirth, phoneNumber, email, gender) select %s,%s,%s,%s,%s,%s,%s,%s where not exists (select 1 from employee where employeeId = %s)',(id, fname, lname, city, dob, phonenumber, email, gender, id))

                result = cursor.rowcount
                statusMessage = cursor.statusmessage
                message.append({'rowsAffected':result, 'data': statusMessage})

                i+=1

            print(message)
            return jsonify(message)

            # return jsonify(message='Everything is ok')

@app.route('/update/', methods=['PUT'])
def update():
    with connection:
        with connection.cursor() as cursor:
            data = request.get_json()

            id = data.get('id')
            fname = data.get('fname')
            status = valiadate.validateStr(fname)
            if not status:
                return jsonify({"result":False,"message":"First name should not be empty"})
                
            lname = data.get('lname')
            status = valiadate.validateStr(lname)
            if not status:
                return jsonify({"result":False,"message":"First name should not be empty"})
                
            city = data.get('city')
            status = valiadate.validateStr(lname)
            if not status:
                return jsonify({"result":False,"message":"First name should not be empty"})
                
            dob = data.get('dob')
            status = valiadate.validateDob(dob)
            if not status:
                return jsonify({"result":False,"message":"Invalid Date of birth"})
            dob = datetime.strptime(dob, "%d/%m/%Y").strftime("%Y-%m-%d")
            
            gender = data.get('gender')
            status = valiadate.validateGender(gender)
            if not status:
                return jsonify({"result":False,"message":"First name should not be empty"})
             

            email = data.get('email')
            status , email = valiadate.validateEMail(email)
            if not status:
                return jsonify({"result":False,"message":"Email is not in proper format"})
            
            phoneNumber = data.get('phonenumber')
            status = valiadate.validatePhone(phoneNumber)
            if not status:
                return jsonify({"result":False,"message":"PhoneNumber is not in proper format"})

            cursor.execute('''update employee set
                firstname=%s,
                lastname=%s,
                city=%s,
                dateOfBirth=%s,
                phoneNumber=%s,
                email=%s,
                gender=%s
            where employeeId = %s''',(fname, lname, city, dob, phoneNumber, email, gender, id))

            result = cursor.rowcount
            statusMessage = cursor.statusmessage
            return jsonify({"result":result,"message":statusMessage})

@app.route('/search/', methods=['GET'])
def search():
    with connection:
        with connection.cursor() as cursor:
           id = request.args.get('id') 
           cursor.execute('select * from employee where employeeId=%s',(id,))
           result = cursor.fetchall()

           if not result :
               return jsonify(message="No employee found with this employee id")
           return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)