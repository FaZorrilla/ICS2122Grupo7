from collections import namedtuple

## BARCOS
Barcos = namedtuple("Barcos_type", ["ide", "tamano", "lista_conteines",
                                    "entro"])

# base de datos
lista = [("grande", 1), ("chico", 2), ("mediano", 3)]

# implementación forma 1
Lista_Barcos = map(lambda x: Barcos(*x), lista)

# visualización
print(list(Lista_Barcos))

## CAMIONES
Camiones = namedtuple("Camiones_type", ["ide", "capacidad", "carga"])

## CONTEINERS

Cointeiners = namedtuple("Conteiners_type", ["ide", "posicion", "tipo"])


