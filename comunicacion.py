import serial
import csv

PuertoSerial = serial.Serial(port = '/dev/ttyS0')

f= open("mediciones.csv",'w') 
writer = csv.writer(f)

while(1):
	valor = PuertoSerial.readline()
	writer.writerow(valor)

f.close()
