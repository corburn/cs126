from flare.display import Stage, Bitmap

stage = Stage(1024, 600)
stage.color = 'white'

HEIGHT = 96
WIDTH = 64

def add_block(name, x, y):
    global stage
    block = Bitmap("cute_craft/" + name + ".png")
    stage.add_child(block)
    block.x = x
    block.y = y

def tree(x, y):
    # trunk
    add_block("dirt1", x + WIDTH , y + HEIGHT)
    # bottom
    add_block("grass1", x, y + HEIGHT*2/3)
    add_block("grass1", x + WIDTH, y + HEIGHT*2/3)
    add_block("grass1", x + WIDTH * 2, y + HEIGHT*2/3)
    # middle
    add_block("grass1", x + WIDTH/2, y + HEIGHT/3)
    add_block("grass1", x + WIDTH/2 + WIDTH, y + HEIGHT/3)
    # top
    add_block("grass1", x + WIDTH, y)

def lake(x,y):
    # top
    add_block("water1", x + WIDTH/2, y)
    add_block("water1", x + WIDTH/2 + WIDTH, y)
    # middle
    add_block("water1", x, y + HEIGHT*2/3)
    add_block("water1", x + WIDTH, y + HEIGHT*2/3)
    add_block("water1", x + WIDTH * 2, y + HEIGHT*2/3)
    # bottom
    add_block("water1", x + WIDTH/2 , y + 2*HEIGHT*2/3)
    add_block("water1", x + WIDTH/2 + WIDTH , y + 2*HEIGHT*2/3)
    
def puzzle1():
    column = ["stone1", "stone1", "sand1", "dirt1", "grass1"]
    base = len(column)*HEIGHT/3
    gap = WIDTH*1.5
    offset = WIDTH/2
    for x in range(6):
        for y, block in enumerate(column):
            add_block(block, x*gap+offset, base-y*HEIGHT/3)

def puzzle2():
    for x in range(3):
        tree(x*WIDTH*5 + WIDTH, 0)
        lake(x*WIDTH*5 + WIDTH, 244)

def puzzle3():
    # wall and sidewalk
    for x in range(12):
        add_block("wood_wall",x*WIDTH,0)
	# left-shift and draw extra blocks offscreen
        add_block("stone1",x*WIDTH-3*WIDTH,320)
    # trees
    tree(0,64)
    tree(WIDTH*5,64)
    # pathway
    for x in range(2):
        add_block("door_closed",x*WIDTH*5 + WIDTH*3,0)
        for y in range(4):
            add_block("stone1",x*WIDTH*5 + WIDTH*3,128+y*64)

puzzle3()
stage.run()
