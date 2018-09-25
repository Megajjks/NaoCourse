# -*- encoding: UTF-8 -*-
#Nao el presentador
#Descripción: Nao avanza unos pasos y se presenta dando la bienvenida al curso
#Hecho por: Jayro Salazar y Raul Chin
import sys
import math
import almath as m #biblioteca matemática
from naoqi import ALProxy
robotIP="192.168.10.100"
port=9559

def StiffnessOn(proxy):
	pNames = "Body"
	pStiffnessLists = 1.0
	pTimeLists = 1.0
	proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def main(robotIP, port):
 	
 	try:
		motionProxy = ALProxy("ALMotion",robotIP, port)
	except Exception, e:
		print "No se a creado el proxy para ALMotion correctamente"
		print "Error:",e
	StiffnessOn(motionProxy)
	#Encendemos los motores de los brazos para caminar
	motionProxy.setWalkArmsEnabled(True, True)
    #Encendemos la protección de caida
	motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    #Obtenemos  las posiciones anteriores del robot para saber donde estan los ejes de movimiento
	initRobotPosition = m.Pose2D(motionProxy.getRobotPosition(False))
    #Ejes de movimiento que avanzará nao
	X = 0.3 
	Y = 0.1
	Theta = 0
	motionProxy.post.moveTo(X,Y,Theta) #Empieza a caminar conforme a los parametros
    #
	motionProxy.waitUntilMoveIsFinished()
    #Obtiene las posiciones después de moverse para finalizar
	endRobotPosition = m.Pose2D(motionProxy.getRobotPosition(False))
    #Imprimimos en consola lo que avanzo el nao
	robotMove = m.pose2DInverse(initRobotPosition)*endRobotPosition
	print "Robot Move :", robotMove
    #Hacemos que nao hable
	tts = ALProxy("ALTextToSpeech",robotIP,port)
	tts.say("!Hola¡, muy buenos días a todos. Les doy la más cordial bienvenida al curso de Nao y Python")
	
main(robotIP,port)    
