from vehiculo import Vehiculo


def main():     
    automovil = Vehiculo(4, "rojo")
    camion = Vehiculo(6, "blanco")
    bicicleta = Vehiculo(2, "gris")
    moto = Vehiculo(2, "negro")

    automovil.info()
    camion.info()
    bicicleta.info()
    moto.info()

main()