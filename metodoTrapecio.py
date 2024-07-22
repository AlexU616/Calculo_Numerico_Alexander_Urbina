import math

def metodoTrapecio(f,a,b,n):
	area = 0
	h = (b-a)/n
	x0 = a
	for i in range(n):
		xi = x0 + (i + 1) * h
		area+= (h/2)*(f(x0) + f(xi))
	return area

f=lambda x: x* math.cos(x**2)

def resultadoMetodoTrapecio(f,a,b,n):
    trapecio = metodoTrapecio(f,a,b,n)
    print("|Valor Aproximado: ",trapecio, "|")
    print("**************************************************")
    return trapecio

if __name__ == '__main__':
    resultadoMetodoTrapecio(f,0,1,4)