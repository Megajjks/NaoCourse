# -*- encoding: UTF-8 -*-
#Piedra, papel o tijera
#By Jayro

from random import choice

def opc(num):
	if num == 1:
		cadena ="Papel"
	elif num ==2:
		cadena = "Tijera"
	else:
		cadena = "Piedra"
	return cadena	

def Player1(num):
	res = opc(num)
	return res

def player2():
	res =opc(choice((1,2,3)))
	return res

def gana(p1,p2):
	if p1==p2:
		print("Empate, vuelve a intentarlo")
		main()
	elif p1=="Piedra" and p2=="Tijera" or p1=="Tijera" and p2=="Papel" or p1=="Papel" and p2=="Piedra":
		print("Tu eres el ganador")
	else:
		print("La maquina te ha ganado")	

def main():
	print("Bienvenido al juego de piedra, papel o tijera, veamos quien es mejor , si la maquina o tu")
	print("Escoge: Papel (1), Tijera(2), Piedra(3)")
	numero = input()
	p1=Player1(numero)
	p2=player2()	
	print ("- Tu escogiste: " + p1);
	print ("- La maquina escogio: " + p2)
	gana(p1,p2)
main()
