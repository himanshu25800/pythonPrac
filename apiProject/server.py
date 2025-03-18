from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import validate as validate
import jwt
from middleware import authorized
from services.db import Database
import services.auth as auth

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

    user = data['user']
    password = data['password']

    message = auth.login(user, password)
    
    return jsonify(message)


#db service
@app.route('/getall', methods=['GET'])
def getAll():
    pageNumber = int(request.args.get('pagenumber',1))
    pageSize = int(request.args.get('pagesize',10))
    message = dbObject.getAll(pageNumber, pageSize)
    return jsonify(message)


@app.route('/getone/', methods=['GET'])
def getById():
    id = request.args.get('id') 
    message = dbObject.getOne(id)
    if not message:
        return jsonify(message="No employee found with this employee id")
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