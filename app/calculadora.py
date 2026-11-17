"""Operaciones aritméticas usadas por la aplicación de la calculadora."""

# IMPORTANTE: reemplaza ??? con los nombres completos de los 3 integrantes,
# separados por " | " y en el mismo orden de la sección Integrantes del README.
# Ejemplo: "Ana María Pérez | Luis Andrés Gómez | Sara Restrepo Ríos"
AUTOR = "Manuela Jimenez Arredondo | David Moreno Moran | Angélica Martínez Carmona"


def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def restar(a, b):
    """Devuelve la diferencia entre dos números."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de dos números."""
    return a * b


def dividir(a, b):
    """Devuelve el cociente de dos números; falla si el divisor es cero."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """Devuelve a elevado a la potencia b."""
    return a**b


def modulo(a, b):
    """Devuelve el residuo de dividir a entre b; falla si b es cero."""
    if b == 0:
        raise ZeroDivisionError("No se puede calcular módulo por cero")
    return a % b
