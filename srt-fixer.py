# import libraries
import sys
import re
import argparse


parser = argparse.ArgumentParser()

# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname, newline='') as ifp:	
	for line in ifp:
	
		# -- αντικαταστήστε με τον δικό σας κώδικα (αρχή) --
		
		's0' : { 'Digit' : 's1' }
		's1' : { 'Digit' : 's2' }
		's2' : { 'Symbol_1' : 's3' }
		's3' : { 'Digit' : 's4' }
		's4' : { 'Digit' : 's5' }
		's5' : { 'Symbol_1' : 's6' }
		's6' : { 'Digit' : 's7' }
		's7' : { 'Digit' : 's8' }
		's8' : { 'Symbol_2' : 's9' }
		's9' : { 'Digit' : 's10' }
		's10' : { 'Digit' : 's11' }
		's11' : { 'Digit' : 's12' }
		's12' : { 'Symbol_5' : 's13' }
		's13' : { 'Symbol_3' : 's14' }
		's14' : { 'Symbol_3' : 's15' }
		's15' : { 'Symbol_4' : 's16' }
		's16' : { 'Symbol_5' : 's17' }
		's17' : { 'Digit' : 's18' }
		's18' : { 'Digit' : 's19' }
		's19' : { 'Symbol_1' : 's20' }
		's20' : { 'Digit' : 's21' }
		's21' : { 'Digit' : 's22' }
		's22' : { 'Symbol_1' : 's23' }
		's23' : { 'Digit' : 's24' }
		's24' : { 'Digit' : 's25' }
		's25' : { 'Symbol_2' : 's26' }
		's26' : { 'Digit' : 's27' }
		's27' : { 'Digit' : 's28' }
		's28' : { 'Digit' : 's28' }

			
	sys.stdout.write(line)

		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --

