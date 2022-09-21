import car

def returnCarYear(myCar):
    return myCar.year

myCar=car.Car()
#myCar2=car.Car()
#myCar3=car.Car()
print(myCar.year)
myCar.year = '2019'
myCarYear = returnCarYear(myCar)
print(myCarYear)

