import math
def derivada(f, h = 0.02):
    def _(x):
        return (f(x + h) - f(x))/h
    return _

def newtonRaphson(f, x, Er, N):
    Ea=Er+1     #Error Relativo Actual
    i=1         #Numero de Iteracion
    xi=0        #Aproximacion actual
    while ( (Ea>Er) & (i<N) ):
        fd=derivada(f)
        xi = x - ( f(x) / fd(x) )
        Ea= abs( ( xi - x ) / xi)
        if(i>1):
            print(f"|Iteración: {i} Aproximación: {xi : 4.4f} Error: {Ea : 4.4f}|")
        else:
            print(f"|Iteracion: {i} Aproximacion: {xi : 4.4f}|")
        x=xi
        i+=1
    return xi

if __name__ == "__main__":
    f = lambda x: math.sin(x) - math.exp(-x) 
    print ("|El ultimo valor de Xi es: ",newtonRaphson(f, 0.5, 0.02, 10), "|")
    print("**************************************************")