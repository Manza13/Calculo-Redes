# -*- coding: utf-8 -*-
from progress.bar import Bar, ChargingBar
import time

bar1 = Bar('Cargando todos los modulos y opciones', max=100)
for num in range(100):
	time.sleep(0.005)
	bar1.next()
bar1.finish()

def titulo():
	print("""
 /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$      /$$        /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$
|__  $$__/| $$_____/ /$$__  $$| $$$    /$$$       /$$__  $$| $$__  $$| $$__  $$ /$$__  $$| $$$ | $$| $$_____/|__  $$__/
   | $$   | $$      | $$  \ $$| $$$$  /$$$$      | $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$| $$| $$         | $$   
   | $$   | $$$$$   | $$$$$$$$| $$ $$/$$ $$      | $$$$$$$$| $$$$$$$/| $$$$$$$/| $$$$$$$$| $$ $$ $$| $$$$$      | $$   
   | $$   | $$__/   | $$__  $$| $$  $$$| $$      | $$__  $$| $$__  $$| $$____/ | $$__  $$| $$  $$$$| $$__/      | $$   
   | $$   | $$      | $$  | $$| $$\  $ | $$      | $$  | $$| $$  \ $$| $$      | $$  | $$| $$\  $$$| $$         | $$   
   | $$   | $$$$$$$$| $$  | $$| $$ \/  | $$      | $$  | $$| $$  | $$| $$      | $$  | $$| $$ \  $$| $$$$$$$$   | $$   
   |__/   |________/|__/  |__/|__/     |__/      |__/  |__/|__/  |__/|__/      |__/  |__/|__/  \__/|________/   |__/             

   Version: 2.0		Estado: BETA!!!		Creado por: TEAM ARPANET		Curso: ASIR 1º
________________________________________________________________________________________________________________________                                                                                                                    
		""")
	
def redes_shannon():
	global sn_lineal
	global busqueda
	def shannon(sn_lineal):
		if busqueda == "1":
			w = float(input("Introduce el ancho de banda (W): "))
			log = math.log2(1+sn_lineal)
			resultado = w*log
			print(f"Resultado de la Velocidad de transmision: {resultado}")
			input("\nEnter para continuar\n")
			inicio()

		elif busqueda == "2":
			c = float(input("Introduce la Velocidad de transmision (C): "))
			log2 = math.log2(1+(sn_lineal))
			resultado = c / log2
			print(f"Resultado de la Ancho de banda: {resultado}")
			input("\nEnter para continuar\n")
			inicio()

		elif busqueda == "inicio":
				inicio()
		else:
			print(f"Lo siento el numero '{busqueda}' introducido no es valido, introduza uno valido de nuevo\n")

	def line():
		lineal = input("\nSacar S/N lineal [Y/N]? ")
		lineal.lower()
		if lineal == "y" or lineal == "s":
			lineal_2 = input("Esta en formato DB [Y/N]? ")
			lineal_2.lower()
			if lineal_2 == "n":
				pontencia_señal = float(input("Potencia de la señal watios(S): "))
				potencia_ruido = float(input("Ruido de la señal watios(N): "))
				sn_lineal = pontencia_señal / potencia_ruido
				print(f"S/N Lineal es: {sn_lineal}")
				shannon(sn_lineal)
			elif lineal_2 == "y" or lineal_2 == "s":
				db = float(input("Introduce el valor db: "))
				lineal_3 = db/10
				sn_lineal = 10**lineal_3
				print(f"S/N Lineal es: {sn_lineal}")
				shannon(sn_lineal)
			elif lineal_2 == "inicio":
				inicio()
			else:
				print(f"Lo siento el codigo '{lineal_2}' introducido no es valido, introduza uno valido de nuevo\n")
				line()
		elif lineal == "n":
			sn_lineal = float(input("Introduce S/N: "))
			print(f"S/N Lineal es: {sn_lineal}")
			shannon(sn_lineal)
		elif lineal == "inicio":
			inicio()
		else:
			print(f"Lo siento el codigo '{lineal}' introducido no es valido, introduza uno valido de nuevo\n")
			line()


	def incognita():
		print("""
Que quieres conseguir:
	
	1.- S de S/N
	2.- N de S/N

	S = Señal
	N = Ruido
				""")
		h = input("--> ")
		if h == "1":
			n = float(input("Indica el valor de N: "))
			sn = float(input("Introduce el valor de S/N: "))
			resultado = n * sn
			print(f"El resultado de S es: {resultado}")
			input("\nEnter para continuar\n")
			inicio()
		elif h == "2":
			s = float(input("Indica el valor de S: "))
			sn = float(input("Introduce el valor de S/N: "))
			resultado = s / sn
			print(f"El resultado de N es: {resultado}")
			input("\nEnter para continuar\n")
			inicio()
		elif h == "inicio":
			inicio()
		else:
			print(f"Lo siento el numero '{h}' introducido no es valido, introduza uno valido de nuevo\n")

	print("""
Que quires sacar:

	1.- Velocidad de transmision (C)
	2.- Ancho de banda (W)
	3.- Señal de Ruido
	4.- Sacar S o N de S/N

		""")
	while True:
		busqueda = input("--> ")
		busqueda.lower()
		if busqueda == "1":
			line()
		elif busqueda == "2":
			line()
		elif busqueda == "3":
			c = float(input("Introduce la Velocidad de transmision (C): "))
			w = float(input("Introduce el Ancho de Banda (W-B): "))
			p = c/w
			a = 2**p
			resultado = a - 1
			print(f"El resultado de ruido: {resultado}")
			input("\nEnter para continuar\n")
			inicio()
		elif busqueda == "4":
			incognita()
		elif busqueda == "inicio":
			inicio()
		else:
			print(f"Lo siento el numero '{busqueda}' introducido no es valido, introduza uno valido de nuevo\n")

def redes_nyquist():
	print("""
Que quires sacar:

	1.- Velocidad de transmision (C)
	2.- Ancho de banda (W) 
	3.- Estados

		""")
	while True:
		a = input("--> ")
		a.lower()

		if a == "1":
			w = float(input("Introduce el ancho de banda: "))
			m = float(input("Introduce los estados o niveles: "))
			log2 = math.log2(m)
			resultado = 2*w*log2
			print(f"El resultado de la velocidad de transmision es: {resultado}")
			input("\nEnter para continuar\n")
			inicio()

		elif a == "2":
			c = float(input("Introduce la velocidad de transmision: "))
			m = float(input("Introduce los estados o niveles: "))
			log2 = math.log2(m)
			log2_mul = 2 * log2
			resultado = c / log2_mul
			print(f"El resultado del ancho de banda es: {resultado}")
			input("\nEnter para continuar\n")
			inicio()

		elif a == "3":
			c = float(input("Introduce la velocidad de transmision: "))
			w = float(input("Introduce el ancho de banda: "))

			q = 2*w
			v = c / q
			resultado = 2**v
			print(f"El resultado de los estados es: {resultado}")
			input("\nEnter para continuar\n")
			inicio()
		elif a == "inicio":
			inicio()
		else:
			print(f"Lo siento el numero '{a}' introducido no es valido, introduza uno valido de nuevo\n")
def historico():
	print(f"Ultimo resultado: {resultado}")
def inicio():

	print("""
Que quieres hacer:

	1.- Shannon  	(Ejercicos con ruido)
	2.- Nysquist	(Ejercicos sin ruido)
	3.- Ayudas Extras

""")
#NOTA: Leer bien los campos que se os pide, ya que cualquier error puede hacer que el programa se cierre.
#Tiene un sistema para detectar cuando algo esta incorrecto, intentara que el programa no se cierre.
# ---> ""Pero no es perfecto"" <---\n
#	""")
	lines = ["NOTA: Leer bien los campos que se os pide, ya que cualquier error puede hacer que el programa se cierre.",
			"Tiene un sistema para detectar cuando algo esta incorrecto, intentara que el programa no se cierre.",
			"---> 'Pero no es perfecto' <---\n"]

	for line in lines:
		   for c in line:
			   print(c, end='')
			   sys.stdout.flush()
			   time.sleep(0.01)
		   print('')
	while True:
		metodo = input("--> ")
		metodo.lower()
		if metodo == "1":
			redes_shannon()
		elif metodo == "2":
			redes_nyquist()
		elif metodo == "3":
			print("\nLa unica que te puedo dar ahora mismo es que si te pierdes, pongas donde pongas el comando 'inicio' volveras al\nprincipio, por si te equivocas tambien te sirve.\n")
			inicio()
		elif metodo == "4":
			graficos()
		else:
			print(f"Lo siento el numero '{metodo}' introducido no es valido, introduza uno valido de nuevo\n")

import math, sys

titulo()
inicio()