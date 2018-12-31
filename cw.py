#!/usr/bin/python
import time
import serial
import sys, getopt
def main(argv):
	wpm=20
	serialport=''
	text=''
	try:
	        text=argv[len(argv)-1]
		opts, args = getopt.getopt(sys.argv[1:],"s:w:",["serialport=","wpm="])
	except getopt.GetoptError:
		print "test.py -s serialport -w wpm TEXTTOSEND"
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-s", "--serialport"):
			serialport=arg
		elif opt in ("-w","--wpm"):
			wpm=int(arg)
		else:
			text=arg
	serialp=openport(serialport)
	send(wpm,text,serialp)
	serialp.close()
	sys.exit(2)

def openport(serialport):
	import serial
	serialp=serial.Serial(serialport, 19200, timeout=1)
	serialp.rts=0
	serialp.dts=0
	return serialp

def send(wpm,text,s):
	coef=10
	CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',' ':'*' 
        }
	print "speed=",wpm
	print "text=",text
	for letter in text:
		letter=letter.upper()
		for sign in CODE[letter]:
			if sign=="*":
				time.sleep(0.3/wpm*coef)
			else:
				s.rts=1
				time.sleep(0.1/wpm*coef)
				if sign=="-":
					time.sleep(0.2/wpm*coef)
				s.rts=0
				time.sleep(0.1/wpm*coef)
		time.sleep(0.3/wpm*coef)
	return

if __name__ == "__main__":
	main(sys.argv)
