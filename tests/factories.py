import uuid

import factory.fuzzy

from application import models


class AircraftFactory(factory.alchemy.SQLAlchemyModelFactory):
    manufacturer = factory.fuzzy.FuzzyChoice(choices=["Boeing", "Airbus", "Embraer"])

    @factory.lazy_attribute
    def serial_number(self):
        return str(uuid.uuid4())

    class Meta:
        model = models.Aircraft
