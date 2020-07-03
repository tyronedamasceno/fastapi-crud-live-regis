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


def delete_pet(db: Session, pet_id: int):
    db.query(models.Pet).filter(models.Pet.id == pet_id).delete()
    db.commit()


def update_pet(db: Session, pet_id: int, pet: schemas.PetUpdate):
    pet_db = get_pet(db, pet_id)
    pet_db.name = pet.name or pet_db.name
    pet_db.kind = pet.kind or pet_db.kind

    db.add(pet_db)
    db.commit()
    db.refresh(pet_db)
    return pet_db
