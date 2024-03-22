import jwt
from flask import jsonify



def decode_user(token,secret_key):
    try:

        decoded_token = jwt.decode(jwt=token,
                                key= secret_key ,
                                algorithms=["HS256"])

       
        return decoded_token
    except jwt.ExpiredSignatureError:
        return {"error": "Bearer token has expired"}
    except Exception as e:
        return {"error": str(e)}
    


def check_bearer_token(request, SECRET_KEY):
    auth_header = request.headers.get('Authorization')
    
    
    if auth_header is None:
        return {'error': 'Missing Authorization header'}, 401

    scheme, token = auth_header.split()
    
    if scheme != 'Bearer':
        return {'error': 'Invalid Authorization header'}, 401

    
    user = decode_user(token,SECRET_KEY)
    
    
    
    #if "error" in user and "Bearer token has expired" in user["error"]:
     #   return jsonify({'error': 'Bearertoken token has expired'}), 401
    
    #else:
    return user



    
