from flare.display import Stage, Bitmap
import math

HEIGHT = 64 # Really 96, but the lower third overlaps
WIDTH = 64

stage = Stage(9*WIDTH, 8*HEIGHT + 32)
stage.color = 'white'

def add_block(name, x, y, a, r):
	global stage
	block = Bitmap("cute_craft/" + name + ".png")
	stage.add_child(block)
	block.x = x
	block.y = y
	block.alpha = a
	block.rotation = r

def spuzzle1():
	square = 7
	for y in range(square):
		offset = y*WIDTH + WIDTH
		add_block("grass1", y*WIDTH, y*HEIGHT, 1, 0)
		for x in range(square-y):
			add_block("stone1", x*WIDTH + offset, y*HEIGHT, 1, 0)
		for x in range(y):
			add_block("sand1", x*WIDTH, y*HEIGHT, 1, 0)

def spuzzle2():
	for y in range(4):
		for x in range(9):
			add_block("grass1", x*WIDTH, y*2*HEIGHT, math.fabs(-4+x)/4, 0)

def spuzzle3():
	for y in range(8):
		for x in range(9):
			add_block("stone1", x*WIDTH, y*HEIGHT, y/7.0, (x/8.0)*math.pi)	

spuzzle2()
stage.run()
