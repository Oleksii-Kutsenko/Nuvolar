from application.database import Session


class BaseCRUD:
    ModelClass = None
    SchemaClass = None
    id_field = None

    @classmethod
    def create_object(cls, session: Session, schema: SchemaClass):
        db_object = cls.ModelClass(**schema.dict())
        session.add(db_object)
        session.commit()
        session.refresh(db_object)
        return db_object

    @classmethod
    def get_object(cls, session: Session, _id):
        db_object = session.query(cls.ModelClass).filter(cls.id_field == _id).first()
        if db_object:
            return db_object
        return None

    @classmethod
    def get_objects(cls, session: Session, skip: int = 0, limit: int = 100):
        return session.query(cls.ModelClass).offset(skip).limit(limit).all()

    @classmethod
    def update_object(cls, session: Session, _id, schema: SchemaClass):
        db_object = session.query(cls.ModelClass).filter(cls.id_field == _id).first()
        if db_object is None:
            return None

        for attr, value in vars(schema).items():
            setattr(db_object, attr, value) if value else None

        session.add(db_object)
        session.commit()
        session.refresh(db_object)
        return db_object

    @classmethod
    def delete_object(cls, session: Session, _id):
        db_object = session.query(cls.ModelClass).filter(cls.id_field == _id).first()
        if db_object is None:
            return False

        session.delete(db_object)
        session.commit()
        return True
