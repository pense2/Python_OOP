# Car class
class Car:
    def __init__(self):
        self.__make = 'Honda'
        self.__model = 'Pilot'
        self.year = '2018'

#    def set_make(self, make):
#        self.__make = make
#
#    def set_model(self, model):
#        self.__model = model
#
#    def set_year(self, year):
#        self.__year = year
#
    def get_make(self):
        return self.__make

#   def get_model(self):
#        return self.__model

#   def get_year(self):
#        return self.__year
