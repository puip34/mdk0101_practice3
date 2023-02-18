class Car:
    def __init__(self, model, horsepower, torque):
        self._model = model
        self._horsepower = horsepower
        self._torque = torque

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_horsepower(self):
        return self._horsepower

    def set_horsepower(self, horsepower):
        if horsepower < 0:
            raise ValueError("horsepower cannot be negative")
        self._horsepower = horsepower

    def get_torque(self):
        return self._torque

    def set_torque(self, torque):
        if torque < 0:
            raise ValueError("torque cannot be negative")
        self._torque = torque



car = Car("ГАЗ-24-10", 330, 440)
car.set_model("Supra-mk4")


print(car.get_model())  # выведет "Bob"


class Car:
    def __init__(self, model, horsepower, torque):
        self._model = model
        self._horsepower = horsepower
        self._torque = torque
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def horsepower(self):
        return self._horsepower

    @horsepower.setter
    def horsepower(self, horsepower):
        if horsepower < 0:
            raise ValueError("horsepower cannot be negative")
        self._horsepower = horsepower

    @property
    def torque(self):
        return self._torque

    @torque.setter
    def torque(self, torque):
        if torque < 0:
            raise ValueError("torque cannot be negative")
        self._torque = torque


car = Car("ГАЗ-24-10", 330, 440)
car.model = "Supra-mk4"


print(car.model)

