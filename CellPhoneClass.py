class Cellphone:


    def __init__(self, m, n, p):
        self.__manufact = m
        self.__model = n
        self.__retail_price = p

    def set_manufact(self,m):
        self.__manufact = m

    def set_model(self,n):
        self.__model = n

    def set_retail_price(self,p):
        self.__retail_price = p

    def get_manufact(self):
        return self.__manufact
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price