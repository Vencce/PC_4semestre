from abc import ABC, abstractmethod

class Armchair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class CoffeeTable(ABC):
    @abstractmethod
    def put_on(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

class ModernArmchair(Armchair):
    def sit_on(self):
        return "Sentando em uma poltrona moderna."

class ModernCoffeeTable(CoffeeTable):
    def put_on(self):
        return "Colocando algo sobre uma mesa de café moderna."

class ModernSofa(Sofa):
    def lie_on(self):
        return "Deitando em um sofá moderno."

class RetroArmchair(Armchair):
    def sit_on(self):
        return "Sentando em uma poltrona retrô."

class RetroCoffeeTable(CoffeeTable):
    def put_on(self):
        return "Colocando algo sobre uma mesa de café retrô."

class RetroSofa(Sofa):
    def lie_on(self):
        return "Deitando em um sofá retrô."

class FurnitureFactory(ABC):
    @abstractmethod
    def make_armchair(self) -> Armchair:
        pass

    @abstractmethod
    def make_coffee_table(self) -> CoffeeTable:
        pass

    @abstractmethod
    def make_sofa(self) -> Sofa:
        pass

class RetroFurnitureFactory(FurnitureFactory):
    def make_armchair(self) -> Armchair:
        return RetroArmchair()

    def make_coffee_table(self) -> CoffeeTable:
        return RetroCoffeeTable()

    def make_sofa(self) -> Sofa:
        return RetroSofa()

class ModernFurnitureFactory(FurnitureFactory):
    def make_armchair(self) -> Armchair:
        return ModernArmchair()

    def make_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()

    def make_sofa(self) -> Sofa:
        return ModernSofa()

def client_code_furniture(factory: FurnitureFactory):
    armchair = factory.make_armchair()
    coffee_table = factory.make_coffee_table()
    sofa = factory.make_sofa()

    print(armchair.sit_on())
    print(coffee_table.put_on())
    print(sofa.lie_on())

if __name__ == "__main__":
    print("Cliente: Testando o código com a fábrica Retrô.")
    client_code_furniture(RetroFurnitureFactory())

    print("\n" + "="*30 + "\n")

    print("Cliente: Testando o código com a fábrica Moderna.")
    client_code_furniture(ModernFurnitureFactory())