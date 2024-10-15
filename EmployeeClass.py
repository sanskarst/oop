class Employee:


    def __init__(self, n, id, d, jt, ms):
        self.__name = n
        self.__id = id
        self.__department = d
        self.__title = jt
        self.__salary = ms

    def set_name(self, n):
        self.__name = n

    def set_id(self,id):
        self.__id = id

    def set_department(self, d):
        self.__department = d

    def set_title(self, jt):
        self.__title = jt

    def set_salary(self, ms):
        self.__salary = ms

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title

    def get_salary(self):
        return self.__salary
