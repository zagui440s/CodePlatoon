class CarManager:
    #class attributes below that go to all cars
    all_cars = {}
    total_cars = 0
    _next_id = 1
    #below are instance attributes
    def __init__(self, make: str, model: str, year: int, mileage: int, services: list) -> None:

        self._id = CarManager._next_id
        CarManager._next_id += 1

        self._make = make.lower()
        self._model = model.lower()
        self._year = year
        self._mileage = mileage
        self._services = services
    
    #below keep track of all_cars list and total_cars
        CarManager.all_cars[self._id] = str(self)
        CarManager.total_cars += 1
    
    @property
    def make(self):
        return self._make.capitalize()
    
    @property
    def model(self):
        return self._model.capitalize()


    #below dunder repr to see in terminal strings and objects
    def __repr__(self) -> str:
        return f"Car(id={self._id} | make='{self._make}'| model='{self._model}', year={self._year}, mileage={self._mileage}, services={self._services})"
    
    # def update_mileage(self, new_mileage: int):
    #     self._mileage = new_mileage

    # def service_car(self, service: str):
    #     self._services.append(service)

car1 = CarManager("honda", "civic", 2002, 130000, ['tuneup, ac repair'])
car2 = CarManager("prius", "wagon", 2002, 145000, ['oil change'])
car3 = CarManager("Toyota", "Camry", 2010, 50000, ['tire rotation'])

print(car1)
print(car2)
print(car3)

# Accessing all_cars and total_cars
print(f"Total cars: {CarManager.total_cars}")
print("All cars:", CarManager.all_cars)
