from flask import Flask, jsonify, request
import validate as validate
from middleware import authorized, getID
from services.db import Database
import services.auth as auth
from services.sendMail import sendMail

app = Flask(__name__)
dbObject = Database()

@app.before_request
def beforeRequest():
    auth_response = authorized()
    if auth_response:
        return auth_response
    

@app.route('/', methods=['GET'])
def greet():
    return jsonify(message="All fine !")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    userId = data['userId']
    password = data['password']

    message = auth.login(userId, password)
    
    return jsonify(message)


#db service
@app.route('/getall', methods=['GET'])
def getAll():
    pageNumber = int(request.args.get('pagenumber',1))
    pageSize = int(request.args.get('pagesize',10))
    message = dbObject.getAll(pageNumber, pageSize)
    return jsonify(message)


@app.route('/getlist/', methods=['GET'])
def getList():
    # id = request.args.get('id')

    token = request.headers.get('Authorization')
    
    id = getID(token)

    message = dbObject.getList(id)
    if not message:
        return jsonify(message="No employee found with this manager id")
    return jsonify(message)


@app.route('/insert/', methods=['POST'])
def post():
            res = request.get_json()
            
            message =[]
            for data in res:
                result, mess = validate.validateData(data)
                if not result:
                    message.append({'error':[m for m in mess]})
                    continue
                
                sendMail()
                result = dbObject.insert(data)
                message.append(result)
                
            # print(message)
            return jsonify(message)


@app.route('/update/', methods=['PUT'])
def update():

    data = request.get_json()

    result , mess = validate.validateData(data)
    if not result:
        return jsonify({"result":result,"message":mess})
    
    message = dbObject.update(data)
    sendMail()
    return jsonify(message)


@app.route('/search/', methods=['GET'])
def search():
    id = request.args.get('id') 
    result = dbObject.search(id)
    if not result :
        return jsonify(message="No employee found with this employee id")
    return jsonify(result)





if __name__ == '__main__':
    app.run(debug=True)


#email using python
# password field in database and check from there.
# get list of employee based on managers from table. 


# parquet file
#schema in db
#CRON Jobs