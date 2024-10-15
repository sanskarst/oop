from datetime import date

class student:

    def __init__(self, i, n, d, c):
        self.__studentid = i
        self.__name = n
        self.__dob = d
        self.__classifcation = c
        self.__age = 0
        self.__register = ''

    def calc_age(self):
        today = date.today()
        dob_list = self.__dob.split('/')
        dob_year = int(dob_list[2])
        self.__age = today.year - dob_year
        
    def get_age(self):
        return self.__age

    def get_id(self):
       return self.__studentid
    
    def get_class(self):
        return self.__classifcation

    def get_dob(self):
        return self.__dob

    def set_registration(self):
        if self.__classifcation == 'F':
            self.__register = 'Student can register from 4/10 through 4/12'
        elif self.__classifcation == 'S':
            self.__register = 'Student can register from 4/7 through 4/9'
        elif self.__classifcation =='Jr':
            self.__register = 'Student can register from 4/4 through 4/6'
        elif self.__classifcation == 'Sr':
            self.__register = 'Student can register from 4/1 through 4/3'

    def get_registration(self):
        return self.__classifcation

    
        