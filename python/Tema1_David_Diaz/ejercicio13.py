def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")

    if n <= 1:
        return 1
    return n * factorial_recursivo(n - 1)


print(factorial(5))             
print(factorial_recursivo(5))   
print(factorial(0))            