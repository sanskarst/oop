class Payroll:

    def __init__(self, desc, date, charge, i):
        self.__description = desc
        self.__date = date
        self.__charge = charge
        self.__id = i


    def set_desc(self, desc):
        self.__description = desc

    def set_id(self,i):
        self.__id = i

    def set_date(self, date):
        self.__date = date

    def set_charge(self, charge):
        self.__charge = charge

    def get_desc(self):
        return self.__description

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge


