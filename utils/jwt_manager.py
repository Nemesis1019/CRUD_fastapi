from jwt import encode,decode

def token(data:dict):
    token:str =encode(payload=data,key="veneco",algorithm="HS256")
    return token

def v_token(token:str)->dict:
   data= decode(token,key="veneco",algorithms=["HS256"])
   return data