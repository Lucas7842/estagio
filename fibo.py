def is_fibonacci_number(n):
  
    if n == 0 or n == 1:
        return True
    
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    
    return b == n

numero = int(input("Informe um número: "))
pertence = is_fibonacci_number(numero)

mensagem = f"O número {numero} {'pertence' if pertence else 'não pertence'} à sequência de Fibonacci."
print(mensagem)
