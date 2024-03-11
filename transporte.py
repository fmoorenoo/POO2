class Transporte:
    def __init__(self, ruedas: int, asientos: int) -> None:
        self.ruedas = ruedas
        self.asientos = asientos

    def desplazar(self, x: int, y: int) -> None:
        print(f"Desplazando a x= {x}; y= {y}.")

    def informacion(self):
        print(f"Tiene {self.ruedas} ruedas y {self.asientos} asientos.")
