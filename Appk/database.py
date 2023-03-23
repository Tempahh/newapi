from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:204682@localhost/newapi'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
        
        
        
        
        
        
#while True:    
#    try:
#       conn = psycopg2.connect(host='localhost', database='newapi', user='postgres', password='204682', cursor_factory=RealDictCursor)
#       cursor = conn.cursor()
#       print("Database connect successful!")
#       break
#    except Exception as error:
#        print("Connecting to database failed")
#        print("Error: ", error)
#       time.sleep(2)
        
