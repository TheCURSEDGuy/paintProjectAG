
from pygame import *
from tkinter import *
from tkinter import filedialog
from math import *
from random import *

Tk().withdraw()

font.init()

th = 10
R = 0
G = 0
B = 0
anum = 0
somnum = 1
thicc = False
curPic0 = 0
curPic1 = 1
curMusic = 0
pause = False
col = (0,0,0)

width,height=1200,700
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE = (255,255,255)


#########################################################################################################################################################
#                                                                                                                                                       #
#    NOTE THAT STAMPS AND IMAGES MIGHT NOT WORK SINCE PATHS WORK DIFFERENTLY HERE (MIGHT NEED TO TRY IT ON VSCODE OR CHANGE DIRECTORY TO pics/file)     #
#                                                                                                                                                       #
#########################################################################################################################################################


#BG ELEMENTS (LOADS IN THE BACKGROUND ELEMENTS)
screen.fill(YELLOW)
joobiBG = transform.smoothscale(image.load("paintProj/pics/backgroundimg.png"),(width,height))
screen.blit(joobiBG,(0,0))
screen.blit(transform.smoothscale(image.load("paintProj/pics/gametitle.png"),(215,50)),(20,10))


#CIRCLE THING
circle = Rect(600-th,70-th,2*th,2*th) 
screenCircle = screen.subsurface(circle).copy()

draw.circle(screen,BLACK,(600,70),50) #CIRCLE WITH THICKNESS OF BRUSH
draw.circle(screen,WHITE,(600,70),50,50-th) #OUTSIDE CIRCLE THAT GROWS BIGGER AS THICKNESS GROWS SMALLER

#COLOR PICKER
sliderR = Rect(250,30,255,10)
sliderG = Rect(250,60,255,10)
sliderB = Rect(250,90,255,10)
screen.blit(transform.smoothscale(image.load("paintProj/pics/COLORGRADIENT.png"),(255,10)),(250,30))
screen.blit(transform.smoothscale(image.load("paintProj/pics/COLORGRADIENT1.png"),(255,10)),(250,60))
screen.blit(transform.smoothscale(image.load("paintProj/pics/COLORGRADIENT2.png"),(255,10)),(250,90))

#SLIDER
draw.rect(screen,GREY,(250,30,10,10))
draw.rect(screen,GREY,(250,60,10,10))
draw.rect(screen,GREY,(250,90,10,10))
slider = Rect(250,20,255,100)



#CANVAS
canvasRect = Rect(200,150,750,500)
draw.rect(screen,WHITE,canvasRect)
draw.rect(screen,BLACK,(199,149,752,502),1)

#TEXT
draw.rect(screen,WHITE,(975,25,195,100))
draw.rect(screen,BLACK,(975,25,195,100),2)
comicFont=font.SysFont("Comic Sans MS",25)

#MUSIC
init()                # need init to initialize the mixer
#FILE LOCATION OF ALL MUSIC FILES
music = ["paintProj/Music/msgstar.mp3","paintProj/Music/music.mp3","paintProj/Music/nsk.mp3","paintProj/Music/nerd.mp3","paintProj/Music/bignbigger.mp3","paintProj/Music/GOOFY.mp3","paintProj/Music/CBAT.mp3","paintProj/Music/ehhh.mp3"]
mixer.music.load(music[0])       # load a MUSIC object
mixer.music.play()
previousRect = Rect(20,70,50,50)
pauseRect = Rect(75,70,50,50)
nextRect = Rect(130,70,50,50)
shuffleRect = Rect(185,70,50,50)
draw.rect(screen,WHITE,previousRect)
draw.rect(screen,RED,previousRect,2)
screen.blit(transform.smoothscale(image.load("paintProj/pics/previous.png"),(50,50)),previousRect)
draw.rect(screen,WHITE,pauseRect)
draw.rect(screen,RED,pauseRect,2)
screen.blit(transform.smoothscale(image.load("paintProj/pics/resume.png"),(50,50)),pauseRect)
draw.rect(screen,WHITE,nextRect)
draw.rect(screen,RED,nextRect,2)
screen.blit(transform.flip(transform.smoothscale(image.load("paintProj/pics/previous.png"),(50,50)),True,False),nextRect)
draw.rect(screen,WHITE,shuffleRect)
draw.rect(screen,RED,shuffleRect,2)
screen.blit(transform.smoothscale(image.load("paintProj/pics/shuffle.png"),(50,50)),shuffleRect)

#PEN
pen = transform.smoothscale(image.load("paintProj/pics/joobipencil.png"),(75,75))
screen.blit(pen,(15,150))
drawRect = Rect(15,150,75,75)
screen.blit(pen,(15,150))
draw.rect(screen,RED,drawRect,2)

#ERASER
eraser = transform.smoothscale(image.load("paintProj/pics/ERASERCAT.png"),(75,75))
screen.blit(eraser,(110,150))
eraserRect = Rect(110,150,75,75)
myRect = [drawRect,eraserRect]
draw.rect(screen,RED,eraserRect,2)

#LINE
lineRect = Rect(15,250,75,75)
draw.rect(screen,WHITE,lineRect)
draw.rect(screen,RED,lineRect,2)
draw.line(screen,BLACK,(20,255),(80,320),5)

#SCREENSHOT
screenShot = screen.subsurface(canvasRect).copy()
screenSlider = screen.subsurface(slider).copy()

#SAVE
screen.blit(transform.scale(image.load("paintProj/pics/save.png"),(75,75)),(110,250))
saveRect = Rect(110,250,75,75)
draw.rect(screen,RED,saveRect,2)

#LOAD
loadRect = Rect(15,350,75,75)
draw.rect(screen,WHITE,loadRect)
draw.rect(screen,RED,loadRect,2)
screen.blit(transform.scale(image.load("paintProj/pics/load.png"),(65,65)),(20,355))

#BRUSH
screen.blit(transform.smoothscale(image.load("paintProj/pics/brushcat.jpg"),(75,75)),(110,350))
brushRect = Rect(110,350,75,75)
draw.rect(screen,RED,brushRect,2)

#RECTANGLE
rectRect = Rect(15,450,75,75)
draw.rect(screen,WHITE,rectRect)
draw.rect(screen,RED,rectRect,2)
draw.rect(screen,BLACK,(25,460,55,55),5)

#UNDO
undoRect = Rect(700,30,75,75)
draw.rect(screen,WHITE,undoRect)
draw.rect(screen,RED,undoRect,2)
screen.blit(transform.smoothscale(image.load("paintProj/pics/UNDO.png"),(74,74)),(701,31))
undo = [screenShot]

#REDO
redoRect = Rect(800,30,75,75)
draw.rect(screen,WHITE,redoRect)
screen.blit(transform.smoothscale(image.load("paintProj/pics/REDO.png"),(74,74)),(801,31))
draw.rect(screen,RED,redoRect,2)
redo =[]

#sprayPaint
sprayRect = Rect(110,450,75,75)
draw.rect(screen,WHITE,sprayRect)
draw.rect(screen,RED,sprayRect,2)
screen.blit(transform.smoothscale(image.load("paintProj/pics/spray.png"),(75,75)),sprayRect)

#STAMP THING
stamps = [transform.smoothscale(image.load("paintProj/pics/NLESOGNARKITTYREAL.png"),(184,147)),transform.smoothscale(image.load("paintProj/pics/skrunkly.png"),(184,147)),transform.smoothscale(image.load("paintProj/pics/sillyCat.jpg"),(184,147)),transform.smoothscale(image.load("paintProj/pics/verysillycat.jpg"),(184,147)),transform.smoothscale(image.load("paintProj/pics/kevin.png"),(184,147)),transform.smoothscale(image.load("paintProj/pics/tiredkitty.png"),(184,147)),transform.smoothscale(image.load("paintProj/pics/CATPIC.png"),(184,147))]
cur = [stamps[0],stamps[1]]
stampURect = Rect(975,150,190,50)
stampDRect = Rect(975,600,190,50)
current1 = Rect(977,220,186,150)
current2 = Rect(977,420,186,150)
draw.rect(screen,WHITE,(975,150,190,500))
draw.rect(screen,BLACK,(975,150,190,500),2)
draw.rect(screen,GREY,stampURect)
draw.rect(screen,GREY,stampDRect)
screen.blit(transform.smoothscale(image.load("paintProj/pics/uparrow.png"),(75,75)),(1032.5,140))
screen.blit(transform.smoothscale(image.load("paintProj/pics/downarrow.png"),(75,75)),(1032.5,585))

#ELLIPSE
ellipseRect = Rect(15,550,75,75)
draw.rect(screen,WHITE,ellipseRect)
draw.rect(screen,RED,ellipseRect,2)
draw.circle(screen,BLACK,(15+75/2,550+75/2),30,5)

#FILL TOOL
fillRect = Rect(110,550,75,75)
draw.rect(screen,WHITE,fillRect)
draw.rect(screen,RED,fillRect,2)
screen.blit(transform.smoothscale(image.load("paintProj/pics/fillbg.png"),(75,75)),fillRect)


#MODES
#LIST OF ALL RECTANGLE TOOL SELECTER
myRect = [drawRect,eraserRect,lineRect,saveRect,loadRect,brushRect,rectRect,undoRect,redoRect,sprayRect,stampURect,stampDRect,current1,current2,previousRect,pauseRect,nextRect,shuffleRect,ellipseRect,fillRect]
#ALL TOOL TYPES
type = ["pencil","eraser","line","save","load","brush","rect","undo","redo","spray","stampup","stampdown","pic1","pic2","rewind","pause","forward","shuffle","ellipse","change bg color"]
#STARTS OFF DEFAULT (none tool)
mode = 0

running=True

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

        #SELECTION
        for i in myRect: #GOES THROUGH ALL THE RECTANGLES
            if i.collidepoint(mouse.get_pos()): #CHECKS FOR COLLISION
                draw.rect(screen,BLACK,i,2) #DRAW A BLACK RECT AROUND
            else:
                draw.rect(screen,RED,i,2) #DRAW A RED RECT IF NO COLLISION FOUND (so it goes back to normal once no collision is found)
        if mode != 0:
            draw.rect(screen,GREEN,myRect[num],2) #WILL ALWAYS DRAW A GREEN RECT AROUND A SELECTED OTOL

        #SCREENSHOT PORTION
        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1:
                screenCircle = screen.subsurface(circle).copy() #TAKES A SCREENSHOT OF THE THICKNESS MEASURER
                screenShot = screen.subsurface(canvasRect).copy() #TAKES SCREENSHOT OF THE CANVAS
                if (canvasRect.collidepoint(mx,my) and mode != 0): #APPENDS SCREENSHOT ONLY IF THERE IS A COLLISION IN THE CANVAS AND A TOOL IS SELECTED
                    undo.append(screen.subsurface(canvasRect).copy())
                    print("scrrenshot") #that's your doing
            
        if evt.type == MOUSEBUTTONDOWN:
            screenSlider = screen.subsurface(slider).copy() #SCREENSHOT

            if evt.button == 3:
                thicc = not thicc #MAKES SHAPES FILLED OR UNFILLED

            if evt.button == 4: #ADDS THICKNESS WHEN SCROLLING UP
                if th < 50:
                    th+=1

            if evt.button == 5: #MINUSES THICKNESS WHEN SCROLLING DOWN
                if th > 1:
                    th-=1
            
            if evt.button == 1: #when right click, registers mouse position
                sx,sy = evt.pos

            for i in myRect: #Goes through every element in that list and checks if the mouse has collided with it
                if i.collidepoint(mouse.get_pos()) and (i != stampURect and i != stampDRect and i != undoRect and i != redoRect and i != previousRect and i != pauseRect and i != nextRect): #skips over those
                    
                    mode = type[anum] #mode is the rect it collided with
                    num = anum
                    draw.rect(screen,WHITE,(975,25,195,100))
                    draw.rect(screen,BLACK,(975,25,195,100),2)
                    screen.blit(comicFont.render(type[anum],False,GREEN),(980,40))
                    [draw.rect(screen,RED,myRect[j],2) for j in range(len(myRect))]
                    draw.rect(screen,GREEN,myRect[anum],2)
                    redo = []

                anum+=1
            anum = 0 #resets counter
            
            if saveRect.collidepoint(mx,my): 
                image.save(screenShot,filedialog.asksaveasfilename(defaultextension=".png")) #saves the whole canvas
            
            if loadRect.collidepoint(mx,my): #loads image from gallery
                draw.rect(screen,WHITE,canvasRect)
                fname = filedialog.askopenfilename()
                if fname != "": #if input not empty then load the image (prevents crash)
                    screen.blit(transform.scale(image.load(fname),(750,500)),canvasRect)
                col = (255,255,255)

            if undoRect.collidepoint(mx,my):
                if len(undo) > 1: #if there are items in the undo list
                    redo.append(undo[-1]) #appends the most recent in the list to the redo list
                    undo.pop() #removes that
                    screen.blit(undo[-1],canvasRect) #and loads the screen before that image
            
            if redoRect.collidepoint(mx,my):
                if len(redo) > 0:
                    undo.append(redo[-1]) #appends the most recent in that list in undo
                    screen.blit(redo[-1],canvasRect) #loads that image
                    redo.pop() #and removes it so it cannot be used again 
            
            if stampURect.collidepoint(mx,my): #this basically goes through every picture in order and blits it
                if curPic0 == 0: 
                    curPic0 = len(stamps)-1
                    curPic1 = 0
                elif curPic1 == 0:
                    curPic0 = len(stamps)-2
                    curPic1 = len(stamps)-1
                else:
                    curPic0 -= 1
                    curPic1 -= 1
                cur[0] = stamps[curPic0]
                cur[1] = stamps[curPic1]
                mode = 0
            
            if stampDRect.collidepoint(mx,my): #same thing with this but in the opposite way
                if curPic1 == len(stamps)-1:
                    curPic0 = len(stamps)-1
                    curPic1 = 0
                elif curPic0 == len(stamps)-1:
                    curPic0 = 0
                    curPic1 = 1
                else:
                    curPic0 += 1
                    curPic1 += 1
                cur[0] = stamps[curPic0]
                cur[1] = stamps[curPic1]
                mode = 0
            
            if previousRect.collidepoint(mx,my):
                curMusic -= 1
                if curMusic < 0:
                    curMusic = len(music) - 1
                mixer.music.load(music[curMusic])
                mixer.music.play()
            
            if pauseRect.collidepoint(mx,my):
                if mixer.music.get_busy(): #if something is playing then pause
                    mixer.music.pause()
                    pause = True
                    draw.rect(screen,WHITE,(77,72,46,46))
                    screen.blit(transform.smoothscale(image.load("paintProj/pics/pause.png"),(50,50)),pauseRect)

                else: #if nothing is playing then unpause
                    mixer.music.unpause()
                    pause = False
                    draw.rect(screen,WHITE,(77,72,46,46))
                    screen.blit(transform.smoothscale(image.load("paintProj/pics/resume.png"),(50,50)),pauseRect)

            if nextRect.collidepoint(mx,my):
                curMusic += 1
                if curMusic > len(music) - 1:
                    curMusic = 0
                mixer.music.load(music[curMusic])
                mixer.music.play()
            
            if shuffleRect.collidepoint(mx,my):
                shuffle(music)
                mixer.music.load(music[0])
                mixer.music.play()


    if not mixer.music.get_busy() and pause == False: #if nothing is playing and it has not been paused then play next song
        curMusic += 1
        if curMusic > len(music)-1:
            curMusic = 0
        mixer.music.load(music[curMusic])       # load a MUSIC object
        mixer.music.play()

    #Stamps       
    draw.rect(screen,WHITE,(978,222,184,147))
    draw.rect(screen,WHITE,(978,422,184,147))
    screen.blit(cur[0],(978,222))
    screen.blit(cur[1],(978,422))

    #Circle
    draw.rect(screen,WHITE,(550,20,100,100))
    draw.circle(screen,WHITE,(600,70),50,50-th)
    draw.circle(screen,(R,G,B),(600,70),th)


    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    screen.set_clip(sliderR)

    #COLOR PICKER THING
    #If any of the sliders are in collision with the mouse, then the slider goes to the mouse's pos, and blits an image of the rect so there are no repeats of the slider
    if mb[0]:
        
        if mx > 254 and mx < 501: 
            screen.set_clip(sliderR)
            if sliderR.collidepoint(mx,my): 
                    screen.blit(screenSlider,slider)
                    
                    screen.blit(transform.scale(image.load("paintProj/pics/COLORGRADIENT.png"),(250,30)),(250,30))
                    draw.rect(screen,WHITE,(250,10,255,20))
                    draw.rect(screen,GREY,(mx-5,20,10,20))
                    R = mx-255
            screen.set_clip(None)

            screen.set_clip(sliderG)
            if sliderG.collidepoint(mx,my):
                    
                    screen.blit(screenSlider,slider)
                    
                    screen.blit(transform.scale(image.load("paintProj/pics/COLORGRADIENT1.png"),(255,10)),(250,60))
                    draw.rect(screen,WHITE,(250,40,255,20))
                    # sliderG = Rect((mx-5,50,10,20))
                    draw.rect(screen,GREY,(mx-5,50,10,20))
                    G = mx-255
            screen.set_clip(None)

            screen.set_clip(sliderB)
            if sliderB.collidepoint(mx,my):
                    
                    screen.blit(screenSlider,slider)
                    
                    screen.blit(transform.scale(image.load("paintProj/pics/COLORGRADIENT2.png"),(255,10)),(250,90))
                    draw.rect(screen,WHITE,(250,70,255,20))
                    # sliderB = Rect((mx-5,80,10,20))
                    draw.rect(screen,GREY,(mx-5,80,10,20))
                    B = mx-255
            screen.set_clip(None)
            

    #draws a circle inside the size of the thickness of paint and another outside so it replicates the brush size
    if evt.type == MOUSEWHEEL:
        if 1 < th < 50:
            screen.blit(screenCircle,circle)
            draw.circle(screen,WHITE,(600,70),50,50-th)
            draw.circle(screen,(R,G,B),(600,70),th)


    screen.set_clip(canvasRect)

    if mb[0] and canvasRect.collidepoint(mx,my): #does the action when mouse is clicked and it is colliding with the canvas

        if mode == "pencil":
            draw.line(screen,(R,G,B),(ox,oy),(mx,my),1)

        if mode == "eraser":
            draw.circle(screen,col,(mx,my),th)
            draw.line(screen,col,(ox,oy),(mx,my),th*2)

        if mode == "line":
            screen.blit(screenShot,canvasRect) # removes the lines everytime you move the line so doesn't show multiple lines
            draw.line(screen,(R,G,B),(sx,sy),(mx,my),th)
        
        if mode == "brush":
            draw.line(screen,(R,G,B),(ox,oy),(mx,my),th*2)
            draw.circle(screen,(R,G,B),(mx,my),th)
        
        if mode == "rect":
            screen.blit(screenShot,canvasRect)
            lx,ly = mx-sx,my-sy
            if not thicc:
                if mx > sx and my > sy:
                    draw.rect(screen,(R,G,B),(sx,sy,lx,ly))
                elif mx < sx and my > sy:
                    draw.rect(screen,(R,G,B),(mx,sy,-lx,ly))
                elif mx < sx and my < sy:
                    draw.rect(screen,(R,G,B),(mx,my,-lx,-ly))
                elif mx > sx and my < sy:
                    draw.rect(screen,(R,G,B),(sx,my,lx,-ly))
            
            if thicc:
                if mx > sx and my > sy:
                    draw.rect(screen,(R,G,B),(sx,sy,lx,ly),th)
                elif mx < sx and my > sy:
                    draw.rect(screen,(R,G,B),(mx,sy,-lx,ly),th)
                elif mx < sx and my < sy:
                    draw.rect(screen,(R,G,B),(mx,my,-lx,-ly),th)
                elif mx > sx and my < sy:
                    draw.rect(screen,(R,G,B),(sx,my,lx,-ly),th)
        
        if mode == "spray":
            rx = randint(-th,th)
            ry = randint(-th,th)
            if sqrt(((mx+rx)-mx)**2+((my+ry)-my)**2) <=  th:
                draw.circle(screen,(R,G,B),(mx+rx,my+ry),1)

        if mode == "pic1":
            screen.blit(screenShot,canvasRect)
            screen.blit(transform.smoothscale(cur[0],(75,75)),(mx-75/2,my-75/2))

        if mode == "pic2":
            screen.blit(screenShot,canvasRect)
            screen.blit(transform.smoothscale(cur[1],(75,75)),(mx-75/2,my-75/2))
        
        if mode == "ellipse":
            screen.blit(screenShot,canvasRect)
            lx,ly = mx-sx,my-sy
            if not thicc:
                if mx > sx and my > sy:
                    draw.ellipse(screen,(R,G,B),(sx,sy,lx,ly))
                elif mx < sx and my > sy:
                    draw.ellipse(screen,(R,G,B),(mx,sy,-lx,ly))
                elif mx < sx and my < sy:
                    draw.ellipse(screen,(R,G,B),(mx,my,-lx,-ly))
                elif mx > sx and my < sy:
                    draw.ellipse(screen,(R,G,B),(sx,my,lx,-ly))
            
            if thicc:
                if mx > sx and my > sy:
                    draw.ellipse(screen,(R,G,B),(sx,sy,lx,ly),th)
                elif mx < sx and my > sy:
                    draw.ellipse(screen,(R,G,B),(mx,sy,-lx,ly),th)
                elif mx < sx and my < sy:
                    draw.ellipse(screen,(R,G,B),(mx,my,-lx,-ly),th)
                elif mx > sx and my < sy:
                    draw.ellipse(screen,(R,G,B),(sx,my,lx,-ly),th)
        
        if mode == "change bg color":
                col = (R,G,B)
                draw.rect(screen,col,canvasRect)

    

    screen.set_clip(None) # Turns it off 
    
    ox,oy=mx,my
    display.flip()
            
quit()