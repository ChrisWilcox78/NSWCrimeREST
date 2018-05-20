

class Location:
    def __init__(self, statsArea: str, lga: str, id: str = None):
        self._id: str = id
        self._statsArea: str = statsArea
        self._lga: str = lga

    @property
    def id(self) -> str:
        return self._id

    @property
    def statsArea(self) -> str:
        return self._statsArea

    @property
    def lga(self) -> str:
        return self._lga

    def __eq__(self, other):
        if type(other) is type(self):
            return self.lga == other.lga and self.statsArea == other.statsArea
        return False

    def __repr__(self):
        return "Location(id={}, statsArea={}, lga={})".format(self.id, self.statsArea, self.lga)
