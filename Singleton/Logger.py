class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.exception_queue = []
        return cls._instance

    def add_exception(self, exception_message):
        self.exception_queue.append(exception_message)

    def show_exceptions(self):
        print("Fila de Exceções:")
        for i, msg in enumerate(self.exception_queue):
            print(f"{i+1}: {msg}")