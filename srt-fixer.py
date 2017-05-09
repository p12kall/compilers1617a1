# 1i Ergastiriaki Askisi - Metaglottistes (09.05.17)
# ANDREAS KALLI
# P2014186


# import libraries
import sys
import re
import argparse


# Diatiposi tis morfis pou theloume na asxolithoume/epeksergastoume meso kanonikis ekfrasis
# Morfi :	00:00:00.000 --> 00:00:00,000
restrow = r'( \d{2} ) : ( \d{2} ) : ( \d{2} ) , ( \d{3} ) \s --> \s ( \d{2} ) : ( \d{2} ) : ( \d{2} ) , ( \d{3} )$'
rexp = re.compile( restrow )

parser = argparse.ArgumentParser()

# add mandatory (positional) arguments
parser.add_argument( "fname", help = "input srt file name" )
parser.add_argument( "offset", type = float, help = "subtitle offset in seconds to apply (can be fractional)" )

# parse arguments
args = parser.parse_args()


# Anoigma tou arxeiou
with open( args.fname, 'r', newline = '' ) as ifp:

# Ksekiname tin sarosi tou keimenou ana grammi
# kai entopismo ton grammon pou teriazoun stin
# anazitisi mas
	for line in ifp:
		m = rexp.search(line)
		if m is not None:
			
# Gia ta deuterolepta tis arxis:
# Pernoume to 3o group tis grammis
			secBeginOld = m.group( 3 )
# Metatrepoume se float kai prosthetoume to offset
			secBeginNew = float( secBeginOld ) + args.offset
# Metatrepoume pali se string
			secBeginCorrect = str( secBeginNew )
			convertBegin = re.sub( restrow, r'\3' + secBeginCorrect, line )
			
# Gia ta deuterolepta tou telous:
# Pernoume to 7o group tis grammis
			secEndOld = m.group( 7 )
# Metatrepoume se float kai prosthetoume to offset
			secEndNew = float( secEndOld ) + args.offset
# Metatrepoume pali se string
			secEndCorrect = str( secEndNew )
			convertEnd = re.sub( restrow, r'\7' + secEndCorrect, line )

# Ektuposi tis ekastote grammis
		sys.stdout.write(line)		

# Kleisimo tou arxeiou .srt
ifp.close()
