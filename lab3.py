from flare.display import Stage, Bitmap
import math

SQUARE = 64

stage = Stage(9*SQUARE, 8*SQUARE + 32)
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
	size = 8
	for y in range(size):
		offset = y*SQUARE + SQUARE
		add_block("grass1", y*SQUARE, y*SQUARE, 1, 0)
		for x in range(size-y-1):
			add_block("stone1", x*SQUARE + offset, y*SQUARE, 1, 0)
		for x in range(y):
			add_block("sand1", x*SQUARE, y*SQUARE, 1, 0)

def spuzzle2():
	for y in range(4):
		for x in range(9):
			add_block("grass1", x*SQUARE, y*2*SQUARE, math.fabs(-4+x)/4, 0)

def spuzzle3():
	for y in range(8):
		for x in range(9):
			add_block("stone1", x*SQUARE, y*SQUARE, y/7.0, (x/8.0)*math.pi)	

spuzzle2()
stage.run()
