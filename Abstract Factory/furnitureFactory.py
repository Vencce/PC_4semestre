from abc import ABC, abstractmethod

class Cabinet(ABC):
    @abstractmethod
    def furniture_function(self):
        pass
    
    @abstractmethod
    def show_style(self):
        pass

class Chair(ABC):
    @abstractmethod
    def furniture_function(self):
        pass

    @abstractmethod
    def show_style(self):
        pass

class DiningTable(ABC):
    @abstractmethod
    def furniture_function(self):
        pass

    @abstractmethod
    def show_style(self):
        pass

class ScandinavianCabinet(Cabinet):
    def furniture_function(self):
        return "Função: Guardar coisas em um armário escandinavo."
    
    def show_style(self):
        return "Estilo: Escandinavo (Armário)"

class ScandinavianChair(Chair):
    def furniture_function(self):
        return "Função: Sentar em uma cadeira escandinava."

    def show_style(self):
        return "Estilo: Escandinavo (Cadeira)"

class ScandinavianDiningTable(DiningTable):
    def furniture_function(self):
        return "Função: Comer em uma mesa de jantar escandinava."

    def show_style(self):
        return "Estilo: Escandinavo (Mesa de Jantar)"


class ClassicCabinet(Cabinet):
    def furniture_function(self):
        return "Função: Guardar coisas em um armário clássico."
    
    def show_style(self):
        return "Estilo: Clássico (Armário)"

class ClassicChair(Chair):
    def furniture_function(self):
        return "Função: Sentar em uma cadeira clássica."

    def show_style(self):
        return "Estilo: Clássico (Cadeira)"

class ClassicDiningTable(DiningTable):
    def furniture_function(self):
        return "Função: Comer em uma mesa de jantar clássica."

    def show_style(self):
        return "Estilo: Clássico (Mesa de Jantar)"


class ContemporaryCabinet(Cabinet):
    def furniture_function(self):
        return "Função: Guardar coisas em um armário contemporâneo."
    
    def show_style(self):
        return "Estilo: Contemporâneo (Armário)"

class ContemporaryChair(Chair):
    def furniture_function(self):
        return "Função: Sentar em uma cadeira contemporânea."

    def show_style(self):
        return "Estilo: Contemporâneo (Cadeira)"

class ContemporaryDiningTable(DiningTable):
    def furniture_function(self):
        return "Função: Comer em uma mesa de jantar contemporânea."

    def show_style(self):
        return "Estilo: Contemporâneo (Mesa de Jantar)"


class FurnitureFactory(ABC):
    @abstractmethod
    def create_cabinet(self) -> Cabinet:
        pass

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_dining_table(self) -> DiningTable:
        pass


class ScandinavianFactory(FurnitureFactory):
    def create_cabinet(self) -> Cabinet:
        return ScandinavianCabinet()

    def create_chair(self) -> Chair:
        return ScandinavianChair()

    def create_dining_table(self) -> DiningTable:
        return ScandinavianDiningTable()

class ClassicFactory(FurnitureFactory):
    def create_cabinet(self) -> Cabinet:
        return ClassicCabinet()

    def create_chair(self) -> Chair:
        return ClassicChair()

    def create_dining_table(self) -> DiningTable:
        return ClassicDiningTable()

class ContemporaryFactory(FurnitureFactory):
    def create_cabinet(self) -> Cabinet:
        return ContemporaryCabinet()

    def create_chair(self) -> Chair:
        return ContemporaryChair()

    def create_dining_table(self) -> DiningTable:
        return ContemporaryDiningTable()


def client_program(factory: FurnitureFactory):
    cabinet = factory.create_cabinet()
    chair = factory.create_chair()
    table = factory.create_dining_table()

    print(chair.show_style())
    print(chair.furniture_function())
    
    print(cabinet.show_style())
    print(cabinet.furniture_function())
    
    print(table.show_style())
    print(table.furniture_function())

if __name__ == "__main__":
    print("Executando com a fábrica Clássica:")
    client_program(ClassicFactory())

    print("\n" + "="*30 + "\n")

    print("Executando com a fábrica Escandinava:")
    client_program(ScandinavianFactory())

    print("\n" + "="*30 + "\n")

    print("Executando com a fábrica Contemporânea:")
    client_program(ContemporaryFactory())