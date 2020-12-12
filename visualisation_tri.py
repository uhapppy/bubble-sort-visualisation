import tkinter
import random
import pygame

pygame.init()

white=(255,255,255)
black=(0,0,0)
basse=0
hauteur=600
count=0
fin=-1
#liste de depart
LISTE=[]
for i in range(basse,hauteur+1):
    LISTE.append(i)

random.shuffle(LISTE)




def update1():
    global LISTE
    random.shuffle(LISTE)

print(LISTE)

def update2():
    global LISTE
    global count
    newlist=[]
    if count>=hauteur:
        #print(LISTE)
        return True

    if count<hauteur:
        for i in range(0,count+1):
            if LISTE[count]==LISTE[i]:
                continue
            if LISTE[i]<LISTE[count]:
                newlist.append(LISTE[i])
                print(count)
            if LISTE[i]>LISTE[count]:
                newlist.append(LISTE[count])
                print(count)
                for j in range(i,hauteur+1):
                    newlist.append(LISTE[j])
        count+=1
        LISTE=newlist
        
        return LISTE

def update3():
    global LISTE
    global count
    newlist=[]

    if count==hauteur:
        for i in range(0,hauteur+1):
            newlist.append(LISTE[i])
        count=0
        LISTE=newlist
        return LISTE


    

    if LISTE[count]>LISTE[count+1]:
        for i in range(0,count):
            newlist.append(LISTE[i])
        newlist.append(LISTE[count+1])
        newlist.append(LISTE[count])
        for j in range(count+2,hauteur+1):
                newlist.append(LISTE[j])
        
        
    if LISTE[count]<LISTE[count+1]:
        for k in range(0,hauteur+1):
            newlist.append(LISTE[k])
        
        
    count+=1
    
    LISTE=newlist
    return LISTE


def update4():
    global LISTE
    global count
    global fin
    newlist=[]

    if count==hauteur:
        for i in range(0,hauteur+1):
            newlist.append(LISTE[i])
        count=0
        
        LISTE=newlist
        return LISTE


    print(count)
    if LISTE[count]==LISTE[fin]-1 :
        print("saluttttt")
        for i in range(0,hauteur+1):
            if count==i or -fin==i+1:
                continue
            newlist.append(LISTE[i])
        newlist.append(LISTE[count])
        newlist.append(LISTE[fin])
        fin-=1
        count+=1
        LISTE=newlist
        return LISTE

    if LISTE[count]>LISTE[count+1]:
        print("2")
        for i in range(0,count):
            newlist.append(LISTE[i])
        newlist.append(LISTE[count+1])
        newlist.append(LISTE[count])
        for j in range(count+2,hauteur+1):
                newlist.append(LISTE[j])
        count+=1
        LISTE=newlist
        return LISTE

        
    if LISTE[count]<LISTE[count+1]:
        print("3")
        for k in range(0,hauteur+1):
            newlist.append(LISTE[k])

        count+=1
        LISTE=newlist
        return LISTE











def draw():
    global LISTE
    for i in range(0,hauteur+1):
        pygame.draw.line(screen,white,(i,hauteur),(i,hauteur-LISTE[i]),2)



screen = pygame.display.set_mode((hauteur,hauteur))

running=True

while running:
    #pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    screen.fill(black)
    while count%100!=0:
        update3()
    update3()
    draw()
    pygame.display.flip()


        

        







