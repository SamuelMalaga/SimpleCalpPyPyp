def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Erro: raiz quadrada de número negativo"

# Exemplos de uso:
num1 = 10
num2 = 5

print(f"Soma: {soma(num1, num2)}")
print(f"Subtração: {subtracao(num1, num2)}")
print(f"Multiplicação: {multiplicacao(num1, num2)}")
print(f"Divisão: {divisao(num1, num2)}")
print(f"Potência: {potencia(num1, num2)}")
print(f"Raiz Quadrada de {num1}: {raiz_quadrada(num1)}")
