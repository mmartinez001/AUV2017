#!/usr/bin/env python


import matplotlib.pyplot as plt
import serial, time, sys, threading, datetime, shutil

######Global Variables#####################################################
# you must declare the variables as 'global' in the fxn before using#
ser = 0
lat = 0
long = 0
pos_x = 0
pos_y = 0
alt = 0
i = 0 #x units for altitude measurment

BAUDRATE = 57600
######FUNCTIONS############################################################

def check_serial():
		init_serial()

def init_serial():
	#opens the serial port based on the COM number you choose
	print "Found Ports:"
	for n,s in scan():
		print "%s\n" % s
	#	print "%s1" % s1
	print " "

	comnum = '/dev/ttyUSB0'    #QC to define serial port


	# configure the serial connections		ser = qc ser1 = gv
	global ser, BAUDRATE
	ser = serial.Serial()
	ser.baudrate = BAUDRATE
	ser.port = comnum
	ser.timeout = 1
	ser.open()
	ser.isOpen()



	print 'OPEN: '+ ser.name + '\n'
	print 'Im cereal'
	print ''


	thread()

def save_raw():
    	#this fxn creates a txt file and saves only GPGGA sentences
    	while True:
		try:
			line = ser.readline()
		    	line_str = str(line)
			f = open('sensor_data.txt', 'a')
		    	f.write('{0:}'.format(line_str))
			f.close()
		    	stream_serial()
		except IndexError:
			pass
					    	
def scan():
        #scan for available ports. return a list of tuples (num, name)
        available = []
        for i in range(1):
            try:
		s = serial.Serial('/dev/ttyUSB0')
                available.append( (i, s.name))
                s.close()   # explicit close 'cause of delayed GC in java
            except serial.SerialException:
                pass
        return available

def stream_serial():
        #stream data directly from the serial port
        line = ser.readline()
        line_str = str(line)
        print line_str

	line1 = ser1.readline()
        line1_str = str(line1)
        print line1_str



def thread():
    	#threads - run idependent of main loop
    	thread1 = threading.Thread(target = save_raw) #saves the raw GPS data over serial while the main program runs
    	#thread2 = threading.Thread(target = user_input) #optional second thread
    	thread1.start()
    	#thread2.start()


check_serial()
