from business.offence import Offence
from business.location import Location
from mongoengine import Document, StringField, IntField, ReferenceField


class CrimeReport():
    def __init__(self, time_period: str, crime_count: int, location: Location, offence: Offence, id: str = None):
        self._id = id
        self._time_period = time_period
        self._crime_count = crime_count
        self._location = location
        self._offence = offence

    @property
    def id(self):
        return self._id

    @property
    def time_period(self):
        return self._time_period

    @property
    def crime_count(self):
        return self._crime_count

    @property
    def location(self):
        return self._location

    @property
    def offence(self):
        return self._offence

    def __eq__(self, other):
        if type(other) is type(self):
            return (self.time_period == other.time_period) and (self.crime_count == other.crime_count) and (self.location == other.location) and (self.offence == other.offence)
        return False

    def __repr__(self):
        return "CrimeReport(id={}, time_period={}, crime_count={}, location={}, offence={})".format(self.id, self.time_period, self.crime_count, repr(self.location), repr(self.offence))
