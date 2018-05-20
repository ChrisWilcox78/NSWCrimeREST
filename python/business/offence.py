from typing import Optional


class Offence:
    def __init__(self, category: str, subcategory: str, id: str = None) -> None:
        self._id: Optional[str] = id
        self._category: str = category
        self._subcategory: str = subcategory

    @property
    def id(self) -> Optional[str]:
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
