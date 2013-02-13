from flare.display import Stage, Bitmap
import math

HEIGHT = 64 # Really 96, but the lower third overlaps
WIDTH = 64
SQUARE = 8

stage = Stage(8*WIDTH, 8*HEIGHT + 32)
stage.color = 'white'

def add_block(name, x, y, a):
	global stage
	block = Bitmap("cute_craft/" + name + ".png")
	stage.add_child(block)
	block.x = x
	block.y = y
	block.alpha = a


def spuzzle1():
	for y in range(SQUARE):
		offset = y*WIDTH + WIDTH
		add_block("grass1", y*WIDTH, y*HEIGHT, 1)
		for x in range(SQUARE-y):
			add_block("stone1", x*WIDTH + offset, y*HEIGHT, 1)
		for x in range(y):
			add_block("sand1", x*WIDTH, y*HEIGHT, 1)

def spuzzle2():
	for y in range(4):
		for x in range(8):
			add_block("grass1", x*WIDTH, y*2*HEIGHT, math.fabs(-4+x)/4)
			print math.fabs(-4+x)/4

spuzzle2()
stage.run()
