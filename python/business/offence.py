class Offence:
    def __init__(self, category: str, subcategory: str, id: str = None):
        self._id = id
        self._category = category
        self._subcategory = subcategory

    @property
    def id(self) -> str:
        return self._id

    @property
    def category(self) -> str:
        return self._category

    @property
    def subcategory(self) -> str:
        return self._subcategory

    def __eq__(self, other):
        if type(other) is type(self):
            return self.category == other.category and self.subcategory == other.subcategory
        return False

    def __repr__(self):
        return "Offence(id ={}, category={}, subcategory={})".format(self.id, self.category, self.subcategory)
