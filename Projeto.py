# Calculadora Básica = + - / *
def calculadora(): 
    operacao = input('''
Ecolha a operação que deseja fazer:
+ ou *s* para soma
- ou *sub* para subtração
* ou m para multiplicação
/ ou *d* para divisão
''')
    num1 = int(input("insira seu primeiro valor aqui:"))
    num2 = int(input("insira seu segundo valor aqui: "))
    valor = 0 
    if operacao == 's' or operacao == "+":
        valor =  print(num1 + num2)
    elif operacao == "sub" or operacao == "-":
        valor = num1 - num2
    elif operacao == "d" or operacao == "/":
        valor = num1 / num2
    elif operacao == "m" or operacao == "*":
        valor = print(num1 * num2)
    else:
        valor = print("insira um valor verdadeiro!")
    return valor

if __name__ == "__main__":
    while True:
        calculadora()
        continua = input('\nDeseja sair? Digite *Q* ou Enter para um novo cálculo: \n')
        if (continua == 'q'):
            break
        
