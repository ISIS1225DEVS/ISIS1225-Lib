"""
Módulo con funciones de utilidad para el manejo de datos en los mapas no ordenados en *DISClib*. Especificamente para tablas de Hash por Encadenamiento Separado (Separate Chaining) y tablas de Hash por Sondeo Lineal (Linear Probing).

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.

*NOTA:* código contribuido por Sanjit_Prasad en https://www.geeksforgeeks.org/prime-numbers/
"""


# python native modules
# math module for getting the prime numbers
import math

# custom modules
# error handler and datatypes
from DISClib.Utils.default import T
from DISClib.Utils.default import VALID_IO_TYPE


def is_prime(n: int) -> bool:
    """*is_prime()* revisa si un número es primo o no.

    Args:
        n (int): número entero para verificar si es primo.

    Returns:
        bool: si el número es primo o no.
    """
    # we asume that the number is prime
    # Corner cases
    # check if n is 1 or 0
    prime = True
    if n < 2:
        return False

    # checking if n is 2 or 3
    if n < 4:
        return prime

    # checking if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # checking if n is divisible by 5 to to square root of n
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    # return True if the number is prime
    return prime


def next_prime(n: int) -> int:
    """*next_prime()* devuelve el siguiente número primo mayor que n.

    Args:
        n (int): número entero para calcular el siguiente número primo.

    Returns:
        int: el siguiente número primo mayor que n.
    """
    # base case
    if n < 2:
        return 2

    # working with the next odd number
    prime = n
    found = False

    # Loop continuously until isPrime returns
    while not found:
        prime += 1
        # True for a prime number greater than n
        if is_prime(prime) is True:
            found = True
    # return the next prime number to n
    return prime


def previous_prime(n: int) -> int:
    """*previous_prime()* devuelve el número primo anterior a n.

    Args:
        n (int): número entero para calcular el siguiente número primo.

    Returns:
        int: el siguiente número primo menor que n.
    """
    # base case
    if n < 2:
        return 2

    # working with the next odd number
    prime = n
    found = False

    # Loop continuously until isPrime returns
    while not found:
        prime -= 1
        # True for a prime number greater than n
        if is_prime(prime) is True:
            found = True


def hash_compress(key: T,
                  scale: int,
                  shift: int,
                  prime: int,
                  mcapacity: int) -> int:

    """*hash_compress()* función de compresión para los índices de las tablas de Hash utilizando el método MAD (Multiply-Add-and-Divide).
    MAD se define como: hash_compress(y) = ((a*y + b) % p) % M, donde:
        a (scale) y b (shift) enteros aleatoreos dentro del intervalo [0,p-1], con a > 0
        p (prime) es un primo mayor a M,
        M (capacity) es el tamaño de la tabla, primo

    Args:
        key (T): llave para calcular el índice en la tabla de Hash, Puede ser cualquier tipo de dato nativo en Python o definido por el usuario.
        scale (int): pendiente de la función de compresión.
        shift (int): desplazamiento de la función de compresión.
        prime (int): número  primo mucho mayor a la capacidad de la tabla de Hash.
        mcapacity (int): tamaño de la tabla de Hash, es un número primo para evitar colisiones.

    Returns:
        int: el índice del elemento en la tabla de Hash.
    """
    # TODO is easier if we cast the dynamic keys to strings?
    # if it is a dynamic data type, we cast it to string
    # data types are (dict, list, set, tuple)
    if isinstance(key, VALID_IO_TYPE) or isinstance(key, dict):
        key = str(key)
    # getting the hash from the key
    hkey = hash(key)
    # calculating the index with the MAD compression function
    idx = int((abs(scale * hkey + shift) % prime) % mcapacity)
    return idx
