from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends
from database import SessionLocal, engine
import models , crud
from typing import List



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Many2Many with ALembic")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/createbranch/")
def create_branch(
    branchname :str, address :str, db: Session = Depends(get_db)):
    return crud.create_branch(db=db, branchname=branchname, address=address)


@app.post("/createicecream/")
def create_icecream(
    icecreamname :str, db: Session = Depends(get_db)):
    return crud.create_icecream(db=db, icecreamname=icecreamname)


@app.post("/createlink/")
def create_link(
    branch_id:int, icecream_id:int, db: Session = Depends(get_db)):
    return crud.create_link(db=db, branch_id=branch_id, icecream_id=icecream_id)


@app.get("/mydata")
def mydata(db:Session = Depends(get_db)):
    bran = db.query(models.Branch).all()
    return bran

@app.get("/get_address_by_branch_id")
def get_address_by_branch_id(db:Session = Depends(get_db), *, icecream_id:int) -> List:
        return (
            db.query(models.Branch, models.Icecream)
            .filter(models.Link.branch_id == models.Branch.id, models.Link.icecream_id == models.Icecream.id, models.Icecream.id == icecream_id)
            # .filter(models.Icecream.id == "1")
            .all()
        )
