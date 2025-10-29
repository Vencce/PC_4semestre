from abc import ABC, abstractmethod

class MotorVehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class ElectricVehicle(ABC):
    @abstractmethod
    def charge(self):
        pass


class FutureVehicleMotorcycle(MotorVehicle):
    def drive(self):
        return "Dirigindo uma motocicleta da FutureVehicle."

class FutureVehicleElectricCar(ElectricVehicle):
    def charge(self):
        return "Carregando um carro elétrico da FutureVehicle."


class NextGenMotorcycle(MotorVehicle):
    def drive(self):
        return "Dirigindo uma motocicleta da NextGen."

class NextGenElectricCar(ElectricVehicle):
    def charge(self):
        return "Carregando um carro elétrico da NextGen."

class Corporation(ABC):
    @abstractmethod
    def create_motor_vehicle(self) -> MotorVehicle:
        pass

    @abstractmethod
    def create_electric_vehicle(self) -> ElectricVehicle:
        pass

class FutureVehicleCorporation(Corporation):
    def create_motor_vehicle(self) -> MotorVehicle:
        return FutureVehicleMotorcycle()

    def create_electric_vehicle(self) -> ElectricVehicle:
        return FutureVehicleElectricCar()

class NextGenCorporation(Corporation):
    def create_motor_vehicle(self) -> MotorVehicle:
        return NextGenMotorcycle()

    def create_electric_vehicle(self) -> ElectricVehicle:
        return NextGenElectricCar()

def client_code_vehicles(factory: Corporation):
    motor_vehicle = factory.create_motor_vehicle()
    electric_vehicle = factory.create_electric_vehicle()

    print(motor_vehicle.drive())
    print(electric_vehicle.charge())

if __name__ == "__main__":
    print("Executando com a FutureVehicleCorporation:")
    client_code_vehicles(FutureVehicleCorporation())

    print("\n" + "="*30 + "\n")

    print("Executando com a NextGenCorporation:")
    client_code_vehicles(NextGenCorporation())