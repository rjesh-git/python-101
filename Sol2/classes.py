class car():
    price = 0
    electric = False
    mileage = 2000
    name = ''

    def getPrice(self):
        return self.price
    
    def getMileage(self):
        return self.mileage
    
    def isElectric(self):
        return self.electric
    
    def __init__(self, name):
        self.name = name

def main():
    model3 = car('Tesla Model3')
    print(model3.name, model3.isElectric(), model3.getPrice())

if __name__ == "__main__":
    main()