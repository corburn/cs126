import string

ascii_art = {}

ascii_art['a'] = [ " ### ", "#   #", "#####", "#   #", "#   #" ]
ascii_art['b'] = [ "#### ", "#   #", "#### ", "#   #", "#### " ]
ascii_art['c'] = [ " ### ", "#   #", "#    ", "#   #", " ### " ]
ascii_art['d'] = [ "#### ", "#   #", "#   #", "#   #", "#### " ]
ascii_art['e'] = [ "#####", "#    ", "###  ", "#    ", "#####" ]
ascii_art['f'] = [ "#####", "#    ", "###  ", "#    ", "#    " ]
ascii_art['g'] = [ " ####", "#    ", "#  ##", "#   #", " ### " ] 
ascii_art['h'] = [ "#   #", "#   #", "#####", "#   #", "#   #" ]
ascii_art['i'] = [ "#####", "  #  ", "  #  ", "  #  ", "#####" ]
ascii_art['j'] = [ "    #", "    #", "    #", "#   #", " ### " ]
ascii_art['k'] = [ "#   #", "#  # ", "###  ", "#  # ", "#   #" ]
ascii_art['l'] = [ "#    ", "#    ", "#    ", "#    ", "#####" ]
ascii_art['m'] = [ "#   #", "## ##", "# # #", "#   #", "#   #" ]
ascii_art['n'] = [ "#   #", "##  #", "# # #", "#  ##", "#   #" ]
ascii_art['o'] = [ " ### ", "#   #", "#   #", "#   #", " ### " ]
ascii_art['p'] = [ "#### ", "#   #", "#### ", "#    ", "#    " ]
ascii_art['q'] = [ " ### ", "#   #", "# # #", "#  # ", " ## #" ]
ascii_art['r'] = [ "#### ", "#   #", "#### ", "#  # ", "#   #" ]
ascii_art['s'] = [ " ####", "#    ", " ### ", "    #", "#### " ]
ascii_art['t'] = [ "#####", "  #  ", "  #  ", "  #  ", "  #  " ]
ascii_art['u'] = [ "#   #", "#   #", "#   #", "#  # ", " ## #" ]
ascii_art['v'] = [ "#   #", "#   #", "#   #", " # # ", "  #  " ]
ascii_art['w'] = [ "#   #", "#   #", "#   #", "## ##", "# # #" ]
ascii_art['x'] = [ "#   #", " # # ", "  #  ", " # # ", "#   #" ]
ascii_art['y'] = [ "#   #", " # # ", "  #  ", "  #  ", "  #  " ]
ascii_art['z'] = [ "#####", "   # ", "  #  ", " #   ", "#####" ]

def print_banner(msg, horizontal=True):
	msg = msg.lower()
	if horizontal:
		banner = []
		for i in range(5):
			line = ""
			for c in msg:
				line += ascii_art[c][i] + " "
			banner.append(line)
		for row in banner:
			print row
	if not horizontal:
		for c in msg:
			for i in ascii_art[c]:
				print i

#print_banner("abcdefghijklmnopqrstuvwxyz", False)
print_banner("hi", False)
