from sqlalchemy.orm import Session
import models


def create_branch(db: Session,branchname:str,address:str):
    db_branch = models.Branch(branchname=branchname,address=address)
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch

def create_icecream(db: Session,icecreamname:str):
    db_icecream = models.Icecream(icecreamname=icecreamname)
    db.add(db_icecream)
    db.commit()
    db.refresh(db_icecream)
    return db_icecream
    
def create_link(db: Session,branch_id:int, icecream_id:int):
    db_link = models.Link(branch_id= branch_id, icecream_id=icecream_id)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link