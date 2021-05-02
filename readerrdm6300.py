
#!/usr/bin/env python

import RPi.GPIO as GPIO

import time
#VARIABLE TO DELAY ABSENCE OF DEVICE
aviso=0 
#DIGITAL PIN TO READ DATA FROM RDM6300
rxPin=21
#VECTOR TO STORE DIGITAL STATES FROM RDM6300
id=[]
#NUMBER FROM BITS TO READ FROM SOFTWARE UART
count_byte=0
#SETTING GPIO BOARD
GPIO.setmode(GPIO.BCM)
#SETTING GPIO 21 AS INPUT
GPIO.setup(rxPin, GPIO.IN)

#FUNCTION TO CALCULATE POWER BASE 2
def pot_2(x):
	return (2**x)



while True:
	#AWAIT WHILE NO RFID 125 kHz TAG NEARBY 
	while (GPIO.input(rxPin)):
		time.sleep(0.00001)
		aviso=aviso+1
		#PRINT  `DISPOSITIVO AUSENTE` EACH 5 SEG
		if aviso==20000:
			print("DISPOSITIVO AUSENTE")
			aviso=0
		#CAME BACK BEGINNING OF LOOP  
		continue
	#LOOP TO CATCH 28 BITS
	while count_byte<28:
		#STORE NOW TIME
		tempo_inicial = time.time()
		#AWAIT PERIOD OF BIT FROM BAUD RATE OF 9600 bps. DISREGARD START BIT TOO
		while (time.time()-tempo_inicial<0.00010):
			continue
		#READ CURRENT BIT
		id.append(GPIO.input(rxPin))
		count_byte+=1
	count_byte=0
	
	#DETEC Y TAG
	#PRINT 3 FIRST BYTES INCLUDING 4 BITS PARITY
	print(str(id[27])+" "+str(id[26])+" "+str(id[25])+" "+str(id[24])+" "+str(id[23])+" "+str(id[22])+" "+str(id[21])+" "+str(id[20])+" "+str(id[19])+" "+str(id[18])+" "+str(id[17])+" "+str(id[16])+" "+str(id[15])+" "+str(id[14])+" "+str(id[13])+" "+str(id[12])+" "+str(id[11])+" "+str(id[10])+" "+str(id[9])+" "+str(id[8])+" "+str(id[7])+" "+str(id[6])+" "+str(id[5])+" "+str(id[4])+" "+str(id[3])+" "+str(id[2])+" "+str(id[1])+" "+str(id[0]))

	#CONVERT BINARY VALUES TO DECIMAL VALUES 
	value_1 = pot_2(7)*(id[7])+pot_2(6)*(id[6])+pot_2(5)*(id[5])+pot_2(4)*(id[4])+pot_2(3)*(id[3])+pot_2(2)*(id[2])+pot_2(1)*(id[1])+pot_2(0)*(id[0])
	if value_1==2:
		value_1=pot_2(7)*(id[17])+pot_2(6)*(id[16])+pot_2(5)*(id[15])+pot_2(4)*(id[14])+pot_2(3)*(id[13])+pot_2(2)*(id[12])+pot_2(1)*(id[11])+pot_2(0)*(id[10])
		if value_1==49:
			value_1=pot_2(7)*(id[27])+pot_2(6)*(id[26])+pot_2(5)*(id[25])+pot_2(4)*(id[24])+pot_2(3)*(id[23])+pot_2(2)*(id[22])+pot_2(1)*(id[21])+pot_2(0)*(id[20])
			if value_1==54:
				#IF 3 FIRTES BYTES ARE ACCORDING TO WAITED VALUES, DEVICE IS DETECTED 
				print("DISPOSITIVO PRESENTE")
	
	#CLEAR VECTOR OF DIGITAL STATES
	id=[]
	#AWAIT TO ANOTHER READING IN SILENCE TIME
	tempo_inicial=time.time()
	while(time.time()-tempo_inicial<1.2):
		continue	
	










