from sense_hat import SenseHat
from time import sleep

def move_marble(pitch,roll,x,y):
    new_x = x #assume no change to start with
    new_y = y #assume no change to start with
    if 1 < pitch < 179 and x != 0:
        new_x -= 1 # move left
    elif 359 > pitch > 179 and x != 7:
        new_x += 1 # move right
    if 1 < roll < 179 and y != 7:
        new_y += 1 # move up
    elif 359 > roll > 179 and y != 0:
        new_y -= 1 # move down
    return new_x, new_y
    
sense = SenseHat()
y=2 # initial y coordinate of marble
x=2 # initial x coordinate of marble
while True:

    pitch = sense.get_orientation()["pitch"]
    roll = sense.get_orientation()["roll"]
    #print("pitch= ", round(pitch,0), "roll= ",round(roll,0))
    sleep(0.05)
    
    b = (0,0,0)
    w = (255,255,255)
    
    board = [[b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b] ] 
             

    # board[y][x]=w # a white marble
    # board_1D=sum(board,[]) # convert to 1-dimension list
    # sense.set_pixels(board_1D) # display it

    new_x,new_y = move_marble(pitch,roll,x,y)

    board[y][x]=w
    board_1D=sum(board,[]) # convert to 1-dimension list
    sense.set_pixels(board_1D) # display it
    x,y=new_x,new_y
    
