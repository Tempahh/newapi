from pydantic import BaseSettings
from sqlalchemy import INTEGER

class Settings(BaseSettings):
    database_hostname= str
    database_Port= str
    database_password= str
    database_name= str
    database_username= str
    secret_key= str
    algorithm= str
    access_token_expire_minutes= INTEGER

    class Config:
        env_file = ".env"

   
    
settings = Settings() 