from jose import JWTError, jwt

#Provide 3 pieces of information
#Secret Key
#Algorithm
#Expiration time

#random string. To get a string like this run openssl rand -hex 32
SECRET_KET = "c88e28e903b57e2c5e6787388577712ed3168421cd5e21fd244e5aa495a86a65"

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30