from abc import ABC, abstractmethod

class MotorVehicle(ABC):
    @abstractmethod
    def build(self):
        pass

class Car(MotorVehicle):
    def build(self):
        print("Construindo um Carro")

class Motorcycle(MotorVehicle):
    def build(self):
        print("Construindo uma Motocicleta")

class MotorVehicleFactory(ABC):
    @abstractmethod
    def create_motor_vehicle(self) -> MotorVehicle:
        pass

    def create(self) -> MotorVehicle:
        vehicle = self.create_motor_vehicle()
        return vehicle

class CarFactory(MotorVehicleFactory):
    def create_motor_vehicle(self) -> MotorVehicle:
        return Car()

class MotorcycleFactory(MotorVehicleFactory):
    def create_motor_vehicle(self) -> MotorVehicle:
        return Motorcycle()

def client_code(factory: MotorVehicleFactory):
    print(f"Cliente: Não conheço a classe do criador, mas está funcionando.")
    vehicle = factory.create()
    vehicle.build()

if __name__ == "__main__":
    print("App: Lançado com a fábrica de carros.")
    client_code(CarFactory())

    print("\n" + "="*30 + "\n")

    print("App: Lançado com a fábrica de motocicletas.")
    client_code(MotorcycleFactory())