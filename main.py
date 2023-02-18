from fastapi import FastAPI,Depends,HTTPException
import schemas,models

app = FastAPI()

from database import engine,SessionLocal
models.Base.metadata.create_all(engine)
from sqlalchemy.orm import Session 

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Here is the function that add a user into a database
@app.post("/",status_code=200)
def create(request: schemas.newusers,db: Session = Depends(get_db)):
    new_users = models.User(name=request.name,email=request.email,password=request.password,phone_number=request.phone_number)
    email_check=models.User(email=request.email)
    if email_check is True:
            # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=404,detail="User already exists")
    else:
        db.add(new_users)
        db.commit()
        db.refresh(new_users)
        return new_users