# Clase Carro
class Carro:
    """
    Clase que representa un carro.

    Propiedades:
    - marca: almacena la marca del carro
    - modelo: almacena el modelo del carro
    - velocidad: almacena la velocidad actual del carro
    """

    def __init__(self, marca, modelo, velocidad):
        """
        Constructor de la clase.

        Parámetros:
        - marca: marca del carro
        - modelo: modelo del carro
        - velocidad: velocidad inicial del carro
        """
        self.marca = marca        # Propiedad que guarda la marca
        self.modelo = modelo      # Propiedad que guarda el modelo
        self.velocidad = velocidad  # Propiedad que guarda la velocidad

    def acelerar(self, incremento):
        """
        Método que aumenta la velocidad del carro.

        Parámetro:
        - incremento: cantidad de velocidad a aumentar
        """
        self.velocidad += incremento
        print(self.marca, "aceleró a", self.velocidad, "km/h")

    def frenar(self, decremento):
        """
        Método que disminuye la velocidad del carro.

        Parámetro:
        - decremento: cantidad de velocidad a disminuir
        """
        self.velocidad -= decremento

        # Validación para que la velocidad no sea negativa
        if self.velocidad < 0:
            self.velocidad = 0

        print(self.marca, "frenó a", self.velocidad, "km/h")

    def mostrar_info(self):
        """
        Método adicional que muestra la información del carro.
        """
        print("Marca:", self.marca, "| Modelo:", self.modelo, "| Velocidad:", self.velocidad)


# =========================
# Programa principal
# =========================

# Creación de objetos
carro1 = Carro("Toyota", "Corolla", 50)
carro2 = Carro("Chevrolet", "Spark", 30)

# Uso de métodos con el primer objeto
carro1.mostrar_info()
carro1.acelerar(20)
carro1.frenar(10)

print("----------------------")

# Uso de métodos con el segundo objeto
carro2.mostrar_info()
carro2.acelerar(15)
carro2.frenar(5)
