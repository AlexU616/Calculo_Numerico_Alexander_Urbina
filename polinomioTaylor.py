import math

def derivada(f, h = 0.01):
    def _(x):
        return (f(x + h) - f(x))/h
    return _

def polinomioTaylor(f, x0, n):
    def polinomio(x):
        i=1
        p=f(x0)
        while (i!=n+1):
            if (i==1):
                d_Actual=derivada(f)
                p+=d_Actual(x0) * (x-x0)
            else:
                d_Actual=derivada(d_Actual)
                p+=( d_Actual(x0) * (x-x0)**i ) / math.factorial(i) 
            i+=1      
        return p
    return polinomio

f=lambda x: x**2 + math.cos(x)

def resultadoPolinomio(f,x,x0,n):
    poli = polinomioTaylor(f,x0,n)
    print(f"|Valor Aproximado: {poli(x) : 4.4f} | Valor Real: {f(x) : 4.4f} | Error Relativo:  {abs(f(x)-poli(x)) : 4.4f}|")
    print("**************************************************")
    return poli(x)

if __name__ == '__main__':
    resultadoPolinomio(f,0.3,0,3)