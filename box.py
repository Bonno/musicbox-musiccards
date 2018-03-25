#!/usr/bin/env python
#from readtest import *
import re
from CardList import CardList
from Reader import Reader
import sys
import subprocess
import shlex

reader = Reader()
cardList = CardList()

print 'Ready: place a card on top of the reader'

while True:
	try:
		card = reader.readCard()
		print 'Read card', card
		plist = cardList.getPlaylist(card)
		print 'Playlist', plist
		if plist != '':
                   subprocess.check_call( ["./haplaylist.sh %s" % plist], shell=True)
	except KeyboardInterrupt:
		sys.exit(0)
	except:
		pass

