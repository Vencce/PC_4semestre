from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def weapon_function(self):
        pass
    
    @abstractmethod
    def show_weapon(self):
        pass

class Soldier(ABC):
    @abstractmethod
    def soldier_function(self):
        pass
    
    @abstractmethod
    def show_soldier(self):
        pass


class FutureWeapon(Weapon):
    def weapon_function(self):
        return "Função: Atirar raios laser."
    
    def show_weapon(self):
        return "Arma: Rifle Laser (Future)"

class FutureSoldier(Soldier):
    def soldier_function(self):
        return "Função: Patrulhar o setor neon."
    
    def show_soldier(self):
        return "Soldado: Ciborgue (Future)"


class RegularWeapon(Weapon):
    def weapon_function(self):
        return "Função: Atirar balas 5.56mm."
    
    def show_weapon(self):
        return "Arma: Rifle de Assalto (Regular)"

class RegularSoldier(Soldier):
    def soldier_function(self):
        return "Função: Patrulhar a base."
    
    def show_soldier(self):
        return "Soldado: Fuzileiro (Regular)"


class NageWeapon(Weapon):
    def weapon_function(self):
        return "Função: Lançar projétil explosivo."
    
    def show_weapon(self):
        return "Arma: Lança-granadas (Nage)"

class NageSoldier(Soldier):
    def soldier_function(self):
        return "Função: Operar artilharia pesada."
    
    def show_soldier(self):
        return "Soldado: Especialista em Demolição (Nage)"


class AbstractFactory(ABC):
    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass

    @abstractmethod
    def create_soldier(self) -> Soldier:
        pass


class FutureFactory(AbstractFactory):
    def create_weapon(self) -> Weapon:
        return FutureWeapon()

    def create_soldier(self) -> Soldier:
        return FutureSoldier()

class RegularFactory(AbstractFactory):
    def create_weapon(self) -> Weapon:
        return RegularWeapon()

    def create_soldier(self) -> Soldier:
        return RegularSoldier()

class NageFactory(AbstractFactory):
    def create_weapon(self) -> Weapon:
        return NageWeapon()

    def create_soldier(self) -> Soldier:
        return NageSoldier()

class Client:
    def __init__(self, factory: AbstractFactory):
        self.weapon = factory.create_weapon()
        self.soldier = factory.create_soldier()

    def run(self):
        print(f"--- {self.soldier.show_soldier()} ---")
        print(self.soldier.soldier_function())
        print(f"--- {self.weapon.show_weapon()} ---")
        print(self.weapon.weapon_function())

if __name__ == "__main__":
    print("Executando com a RegularFactory:")
    client_regular = Client(RegularFactory())
    client_regular.run()

    print("\n" + "="*30 + "\n")

    print("Executando com a FutureFactory:")
    client_future = Client(FutureFactory())
    client_future.run()
    
    print("\n" + "="*30 + "\n")

    print("Executando com a NageFactory:")
    client_nage = Client(NageFactory())
    client_nage.run()