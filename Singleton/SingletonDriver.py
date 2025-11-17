from Logger import Logger

class SingletonDriver:
    def run_tests(self):
        logger1 = Logger()
        logger2 = Logger()

        logger1.add_exception("Exceção na Classe A: Divisão por zero.")
        logger2.add_exception("Exceção na Classe B: NullPointerException.")
        logger1.add_exception("Exceção na Classe C: Timeout de rede.")

        print("--- Testando logger1 ---")
        logger1.show_exceptions()
        
        print("\n--- Testando logger2 ---")
        logger2.show_exceptions()

        print(f"\nLogger1 é o mesmo objeto que Logger2? {logger1 is logger2}")

if __name__ == "__main__":
    driver = SingletonDriver()
    driver.run_tests()