import os 

class Config:
    DEBUG = True
    API_KEY = os.getenv('API_KEY')

