from dataclasses import field
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel ,Field
import models 
from database import engine , SessionLocal
from sqlalchemy.orm import Session 


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Emp(BaseModel):
    emp_id: int
    first_name: str = Field(min_length =1)
    last_name:str = Field(min_length =1)
    city: str = Field(min_length =1)
    age:float
    experience: float
    ctc:float
    age:float
    contact: int 
  
EMPS = []


@app.get("/")
def read_root():
    return {"hello":"World"}


@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Emps).all() 

@app.post("/")
def create_emp(emp: Emp, db: Session = Depends(get_db)):
    
    emp_model = models.Emps()
    emp_model.emp_id = emp.emp_id
    emp_model.first_name = emp.first_name
    emp_model.last_name = emp.last_name
    emp_model.city = emp.city
    emp_model.age = emp.age 
    emp_model.experience = emp.experience
    emp_model.ctc = emp.ctc
    emp_model.contact = emp.contact
    
    db.add(emp_model)
    db.commit()
    
    return emp 

@app.put("/{emp_id}")
def update_emp(emp_id: int, emp: Emp, db: Session = Depends(get_db)):

    emp_model = db.query(models.Emp).filter(models.Emp.id == emp_id).first()

    if emp_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {emp_id} : Does not exist"
        )

    emp_model.first_name = emp.first_name
    emp_model.last_name = emp.last_name
    emp_model.city = emp.city
    emp_model.age = emp.age
    emp_model.experience = emp.experience
    emp_model.ctc = emp.ctc
    emp_model.contact = emp.contact

    db.add(emp_model)
    db.commit()

    return emp


@app.delete("/{emp_id}")
def delete_emp(emp_id: int, db: Session = Depends(get_db)):

    emp_model = db.query(models.Emp).filter(models.Emp.id == emp_id).first()

    if emp_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {emp_id} : Does not exist"
        )

    db.query(models.Emps).filter(models.Emps.id == emp_id).delete()

    db.commit()