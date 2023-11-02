from ursina import *
import random as r

app = Ursina()
window.fullscreen = True
window.color = color.white

animation_path = "Dinogame/dino"
animation_path2 = 'Dinogame/cacti'
dino = Animation(animation_path, collider='box', x=-5)

cactus = Entity(model="quad", texture=animation_path2, collider="box", x=20)
ground = Entity(model='quad', texture="Dinogame/ground", scale=(50, 0.5, 1), z=1)
ground2 = duplicate(ground, x=50)
pair = [ground, ground2]

cacti = []

def new_cact():
    new = duplicate(cactus, x=12 + r.randint(0, 5))
    cacti.append(new)
    invoke(new_cact, delay=2.5)

new_cact()

label = Text(
    text=f'Points: {0}',
    color=color.black,
    position=(-0.5, 0.4)
)
points = 0
Halt = False
n=5
def late_quit():
    sys.exit()
    
def quit():
    # application.pause()  # Pause the game
    invoke(application.quit, delay=3)
    print("used")
    
def Pause():
    global Halt
    Halt = True

def Resume():
    global Halt
    Halt = False

def update():
    global n, points
    points += 1
    label.text = f'Points: {points}'
    
    if Halt:
        return  # Game is paused, don't update
    
    for ground in pair:
        ground.x -= n * time.dt
        if ground.x < -35:
            ground.x += 100
    
    for c in cacti:
        c.x -= n * time.dt

    if dino.intersects().hit:
        dino.texture = 'Dinogame/hit'
        label2 = Text(
            text="SKILL ISSUE! NOOB!",
            scale=1,
            color=color.black,
            position=(-0.25, 0.2))
        Pause()
        invoke(quit)
        
        
    if n >10:
        label2 = Text(
            text="Max speed reached,Congratulations",
            scale=1.5,
            color=color.black,
            position=(-0.25, 0.2))
        invoke(late_quit, delay=3)
        
    # n += 1 
    # print(n)
sound = Audio('Dinogame/beep', autoplay=False)

def input(key):
    global n
    if key == 'space':
        if dino.y < 0.01:
            sound.play()
            dino.animate_y(2, duration=0.5, curve=curve.out_sine)
            dino.animate_y(0, duration=0.5, delay=0.5, curve=curve.in_sine)
            n += .50  # Increment 'n' on each keypress
        print(n)
camera.orthographic = True
camera.fov = 10

app.run()
