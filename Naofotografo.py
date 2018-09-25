# -*- encoding: UTF-8 -*- 
from naoqi import ALProxy
from ftplib import FTP
robotIP="192.168.10.100"
port=9559

def main(ip,port):
	#Crear el proxy de ALPhotoCapture
	try:
		photoCaptureProxy = ALProxy("ALPhotoCapture", ip, port)
	except Exception, e:
  		print "Error al crear ALPhotoCapture proxy:"
  		print str(e)
  		exit(1)
  	#Se toma 3 fotos	
  	photoCaptureProxy.setResolution(2)
	photoCaptureProxy.setPictureFormat("jpg")
	photoCaptureProxy.takePictures(3, "/home/nao/recordings/cameras/", "image")
	tts = ALProxy("ALTextToSpeech", ip, port)
	tts.say("Imagen capturada")
	#Codigo para obtener una imagene en el servidor ftp de NAO
	ftp=FTP(ip,"nao","nao") #ipservidor
	ftp.cwd("/recordings/cameras/") #Carpeta
	ftp.retrbinary('RETR image_2.jpg',open('image_2.jpg','wb').write)
	ftp.quit()

	tts = ALProxy("ALTextToSpeech", ip, port)
	tts.say("Imagen capturada con exito y descargado del servidor ftp a ordenador local")
main(robotIP,port)
