from application import models, schemas
from application.crud.crud import BaseCRUD


class AircraftCRUD(BaseCRUD):
    ModelClass = models.Aircraft
    SchemaClass = schemas.Aircraft
    id_field = models.Aircraft.serial_number
