class CategoryDTO:
    def __init__(self, category_number, category_name):
        self.__category_number = category_number
        self.__category_name = category_name

    @property
    def category_number(self):
        return self.__category_number

    @property
    def category_name(self):
        return self.__category_name

    def serialize(self):
        return {
            'ID': self.__category_number,
            'Name': self.__category_name
            # 'category_number': self.__category_number,
            # 'category_name': self.__category_name
        }
