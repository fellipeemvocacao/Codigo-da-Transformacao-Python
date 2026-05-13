class CarroPremium:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def __str__(self):
        return f"Este é um luxuoso {self.marca} {self.modelo}."

carro_luxo = CarroPremium("Porsche", "911")
print(carro_luxo) 