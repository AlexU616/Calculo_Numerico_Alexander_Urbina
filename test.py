import unittest
from metodoBiseccion import *
from newtonRaphson import *
from polinomioTaylor import *
from integralRieman import *
from metodoTrapecio import *

class test(unittest.TestCase):
	def testBiseccion(self):
		print("\n\n***********  METODO DE BISECCIÓN  ************************************")
		f1 = lambda x: math.exp(-x) - math.log(x)
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		f4 = lambda x: (x + 1)**0.5 - math.tan(x)
		self.assertEqual(Biseccion(f1,1,1.5,0.05,20),1.3125)
		self.assertEqual(Biseccion(f2,1,2,0.05,20),1.4375)
		self.assertEqual(Biseccion(f3,0,1,0.04,20),0.578125)
		self.assertEqual(Biseccion(f4,0.5,1,0.01,20),0.9453125)
	def testNewtonRaphson(self):
		print("\n\n***********  METODO DE NEWTHON RAPHSON  ******************************")
		f1 = lambda x: math.exp(x) - 2*x**2
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(newtonRaphson(f1,0.5,0.02,10),2.6212275327680037)
		self.assertEqual(newtonRaphson(f2,1,0.05,20),1.4124215461418443)
		self.assertEqual(newtonRaphson(f3,0.5,0.02,10),0.5885488916184832)
	def testPolinomioTaylor(self):
		print("\n\n***********  POLINOMIO DE TAYLOR  ************************************")
		f1 = lambda x: math.exp(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(resultadoPolinomio(f1,1,0,5),2.730287258710013)
		self.assertEqual(resultadoPolinomio(f3,1,0,3),0.49251258302209866)
	def testIntegralRieman(self):
		print("\n\n***********  METODO DE RIEMAN  ***************************************")
		f1 = lambda x: x / (x**2 + 1)
		f2 = lambda x: x * (x**2 + 1)**0.5
		self.assertEqual(resultadoRieman(f1,0,1,4),0.2788235294117647)
		self.assertEqual(resultadoRieman(f2,1,2,4),2.4116477770123668)
	def testMetodoTrapecio(self):
		print("\n\n*********** METODO DEL TRAPECIO  *************************************")
		f1 = lambda x: x*math.cos(x**2)
		f2 = lambda x: math.sin(x) - x**2
		self.assertEqual(resultadoMetodoTrapecio(f1,0,1,4),0.23858922110272346)
		self.assertEqual(resultadoMetodoTrapecio(f2,0,1,4),0.046867405336244575)


if __name__ == '__main__':
	unittest.main()