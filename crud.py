from sqlalchemy.orm import Session

import models, schemas


def list_pets_with_filter(db: Session, kind: str = None):
    if kind:
        return db.query(models.Pet).filter(models.Pet.kind == kind).all()
    return db.query(models.Pet).all()


def create_pet(db: Session, pet: schemas.PetCreate):
    pet_db = models.Pet(**pet.dict())
    # pet_db = models.Pet(name=pet.name, kind=pet.kind)
    db.add(pet_db)
    db.commit()
    db.refresh(pet_db)
    return pet_db


def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()
