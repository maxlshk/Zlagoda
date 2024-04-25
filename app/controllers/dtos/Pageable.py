class Pageable:
    def __init__(self, column, order, search_column, search_value):
        self.__column = column
        self.__order = order
        self.__search_column = search_column
        self.__search_value = search_value

    @property
    def column(self):
        return self.__column

    @property
    def order(self):
        return self.__order

    @property
    def search_column(self):
        return self.__search_column

    @property
    def search_value(self):
        return self.__search_value

    @staticmethod
    def get_pageable(args, mapper):
        db_column = mapper.map_to_db_column(args.get('sort', 'ID', type=str))
        sort_order = args.get('order', 'asc')
        if 'search-column' in args:
            search_column = mapper.map_to_db_column(args['search-column'])
        else:
            search_column = None
        search_val = args.get('search-value', type=str)
        return Pageable(db_column, sort_order, search_column, search_val)


class ReceptPageable:
    def __init__(self, start_date, end_date, cashier_id):
        self.__start_date = start_date
        self.__end_date = end_date
        self.__cashier_id = cashier_id

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    @property
    def cashier_id(self):
        return self.__cashier_id

    @staticmethod
    def get_pageable(args):
        start_date = args.get('start-date', type=str)
        end_date = args.get('end-date', type=str)
        cashier_id = args.get('cashier-id', type=str)
        return ReceptPageable(start_date, end_date, cashier_id)
