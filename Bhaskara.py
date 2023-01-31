#bhaskara  x = b2 - 4.a.C
# x1, x2 = -B +- x¬ / 2a
import math
def Bhaskara(A, B, C):
    '''Uma função do falecio Shidara, onde você apenas precisa incluir os valores de A, B e C, que a função lhe retornará o resultado de Delta, X¹ e X²'''
    delta = B**2 - 4 * A * C
    if delta < 0:
        return [delta]
    else:
        x1 = ( - B + math.sqrt(delta)) / 2*A
        x2 = (- B - math.sqrt(delta)) / 2*A

    return delta,x1,x2
if __name__ == '__main__':
    while True:    
        A = float(input("Insira seu valor de A aqui: "))
        B = float(input("Insira seu valor de B aqui: "))
        C = float(input("Insira seu valor de C aqui: "))
        
        if  len(Bhaskara(A,B,C)) >= 2:
            delta, x1, x2 = Bhaskara(A,B,C)
            print("O valor de delta: {}\nO valor de x¹: {:.4}\nO valor de x²: {:.4}".format(delta, x1, x2))      
        else:
            delta =  Bhaskara(A,B,C)
            print("O valor de delta é negativo, por isso não há valor de x¹ e x²\nO valor de delta é: {}".format(delta[0]))
        continua = input('\nDeseja sair? Digite Q ou Enter para um novo cálculo: \n')
        if (continua == 'q'):
            break