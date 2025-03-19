import jwt
from flask import jsonify, request
from services.db import Database
from services.encrypttext import isPasswordCorrect

dbObject = Database()

def authorized():
    open_routes = ['/', '/login']

    # If the request path is in open_routes, skip authentication
    if request.path in open_routes:
        return None
    
    token = request.headers.get('Authorization')
    # print(token)
    
    if not token:
        return jsonify(message = "No token found"), 401
    try:
        if token.startswith("Bearer "):
            token = token.split(" ")[1]  # Extract the actual JWT
        # print(token)
        decoded = jwt.decode(token, "secret", algorithms=["HS256"])
        # print(decoded)
        if decoded :
            user = dbObject.search(decoded.get('userId'))
            # print(decoded.get('user'), decoded.get('password'))
            if user and isPasswordCorrect(decoded.get('password'), user[8]):
                return None
        return jsonify(message = "Not authorized "), 401

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
        
    except jwt.DecodeError:
        return jsonify({"message":"Invalid Token"}), 401
        
    except jwt.InvalidTokenError:
        return jsonify({"message":"Invalid Token"}), 401


def getID(token):
    try:
        if token.startswith("Bearer "):
            token = token.split(" ")[1]  # Extract the actual JWT
        # print(token)
        decoded = jwt.decode(token, "secret", algorithms=["HS256"])
        # print(decoded)
        if decoded :
            id = decoded.get('userId')
            return id

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
        
    except jwt.DecodeError:
        return jsonify({"message":"Invalid Token"}), 401
        
    except jwt.InvalidTokenError:
        return jsonify({"message":"Invalid Token"}), 401
