
################################################################################################################################################################################################################################################
def lines():
    print( "___" * 9 ) 
################################################################################ 
def break_lines():
    print("")
    print("")
################################################################################
def load():
    import time
    from time import sleep

    while True:
        load = 0
        load = load + 1
        print("Okei criando os personagens ...")
        time.sleep(1)
        load = load + 1
        print("Okei criando os personagens .")
        time.sleep(1)
        load = load + 1
        print("Okei criando os personagens ..")
        time.sleep(1)
        print("Okei criando os personagens ...")
        load = load + 1
        if load == 4:
            break
################################################################################
def home():    
    print("    ", 'Pygame engine')
    lines()
################################################################################################################################################################
home()

nun_per = int(input('Quantos Personagens? '))

print("Você escolheu", nun_per, "personagens. Correto? ")

Y_n = (input(" "))

if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes" or Y_n == nun_per:
    load()

else:
    print("Ahh Desculpa")

    nun_per = int(input('Quantos Personagens? '))

    print("Você escolheu", nun_per, "personagens. Correto? ")

    Y_n = (input(" "))

    if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
        load() 

################################################################################################################################################################

lines()
break_lines()

size_players = int(input("Tamanho dos personagens ' 0/80 ': "))    

print("O Tamanho dos seus personagens é", size_players, " . Correto? ")

Y_n = input("")

if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
    load()

else:
    print('Ahhh está bom...')
    size_players = int(input("Tamanho dos personagens '0 - 80': "))
    print("O Tamanho dos seus personagens é", size_players, " . Correto? ")
    Y_n = input("")
            
    if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
        load()

    else:
        print('Ahhh está bom...')
        size_players = int(input("Tamanho dos personagens '0 - 80': "))
        print("O Tamanho dos seus personagens é", size_players, " . Correto? ")
        Y_n = input("")
        if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
            load()

################################################################################################################################################################

lines()
break_lines()

Size_Window1 = int(input("Qual é a Altura da janela: "))

Size_Window2 = int(input("Qual é a Largura da janela: "))

print('A Altura da janela é ', Size_Window1, 'E a Largura é ', Size_Window2, '. Correto?' )
        
Y_n = input("")

if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
    load()

else:

    print("Opss...")

    Size_Window1 = int(input("Qual é a Altura da janela: "))
    Size_Window2 = int(input("Qual é a Largura da janela: "))
    print('A Altura da janela é ', Size_Window1, 'E a Largura é ', Size_Window2, '. Correto?' )
            
    Y_n = input("")

    if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
        load()
            
    else:
        pass

################################################################################################################################################################

lines()
break_lines()

if nun_per == 1:

    print("Qual é a cor do seu personagen?")
    print("R:   ")
    Color_R = int(input(""))
    print("G:   ")
    Color_G = int(input(""))
    print("B:   ")
    Color_B = int(input(""))
    print("As cores que você escolheu foi: R:", Color_R,"G: ", Color_G,"B: ", Color_B, ". Correto?")
    Y_n = input("")
    if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
        pass
        load()

if nun_per == 2:
    
    print("Qual é a cor do seu personagen?")
    print("R:   ")
    Color_R = int(input(""))
    print("G:   ")
    Color_G = int(input(""))
    print("B:   ")
    Color_B = int(input(""))
    print("As cores que você escolheu foi: R:", Color_R,"G: ", Color_G,"B: ", Color_B, ". Correto?")
    Y_n = input("")
    if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
        
        load()

    print("Qual é a cor do seu personagen?")
    print("R:   ")
    Color_R_2 = int(input(""))
    print("G:   ")
    Color_G_2 = int(input(""))
    print("B:   ")
    Color_B_2 = int(input(""))
    print("As cores que você escolheu foi: R:", Color_R_2,"G: ", Color_G_2,"B: ", Color_B_2, ". Correto?")
    Y_n = input("")
    if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
        
        load()

if nun_per == 3:
    pass
    print("Qual é a cor do seu personagen?")
    print("R:   ")
    Color_R = int(input(""))
    print("G:   ")
    Color_G = int(input(""))
    print("B:   ")
    Color_B = int(input(""))
    print("As cores que você escolheu foi: R:", Color_R,"G: ", Color_G,"B: ", Color_B, ". Correto?")
    Y_n = input("")
    if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
        
        load()

    print("Qual é a cor do seu personagen?")
    print("R:   ")
    Color_R_2 = int(input(""))
    print("G:   ")
    Color_G_2 = int(input(""))
    print("B:   ")
    Color_B_2 = int(input(""))
    print("As cores que você escolheu foi: R:", Color_R_2,"G: ", Color_G_2,"B: ", Color_B_2, ". Correto?")
    Y_n = input("")
    if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
        
        load()

    print("Qual é a cor do seu personagen?")
    print("R:   ")
    Color_R_3 = int(input(""))
    print("G:   ")
    Color_G_3 = int(input(""))
    print("B:   ")
    Color_B_3 = int(input(""))
    print("As cores que você escolheu foi: R:", Color_R_2,"G: ", Color_G_2,"B: ", Color_B_2, ". Correto?")
    Y_n = input("")
    if Y_n == "Sim" or Y_n == "S" or Y_n == "sim" or Y_n == "s" or Y_n == "Yes" or Y_n == "Yes" or Y_n == "Y" or Y_n == "yes":
        
        load()

if nun_per == 4:
    pass

if nun_per == 5:
    pass

if nun_per == 6:
    pass

if nun_per == 7:
    pass

if nun_per == 8:
    pass

if nun_per == 9:
    pass

if nun_per == 10:
    pass

if nun_per == 11:
    pass

if nun_per == 12:
    pass

if nun_per == 13:
    pass

if nun_per == 14:
    pass

if nun_per == 15:
    pass

if nun_per == 16:
    pass

if nun_per == 17:
    pass

if nun_per == 18:
    pass

if nun_per == 19:
    pass

if nun_per == 20:
    pass

if nun_per == 21:
    pass

if nun_per == 22:
    pass

if nun_per == 23:
    pass

if nun_per == 24:
    pass

if nun_per == 25:
    pass

if nun_per == 26:
    pass

################################################################################################################################################################
                              #
import pygame                 #    
from pygame.locals import *   #
import OpenGL                 #
from OpenGL.GL import *       #
##############################

                        ############################
                       #  Altura        Largura    #
# size_players, nun_per, Size_Window1, Size_Window2

if nun_per == 1:
    
    X_Player_1 = 0
    Y_Player_1 = 0



    def largura_Dos_Players():
        return size_players

    def Altura_Dos_Players():
        return size_players

    def Desenhar_Players(x, y, largura, altura, r, g, b):
        glColor3f(r, g, b)
        glBegin(GL_QUADS)
        glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
        glVertex2f(0.5 * largura + x, -0.5 * altura + y)
        glVertex2f(0.5 * largura + x, 0.5 * altura + y)
        glVertex2f(-0.5 * largura + x, 0.5 * altura + y)    
        glEnd()  
    
    def Desenhar():
        glViewport(0, 0, Size_Window2, Size_Window1)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-Size_Window2 / 2, Size_Window2/ 2, -Size_Window1 / 2,Size_Window1 / 2, 0, 1 )
        glClear(GL_COLOR_BUFFER_BIT)
        Desenhar_Players(X_Player_1, Y_Player_1, largura_Dos_Players(), Altura_Dos_Players(), Color_R, Color_G, Color_B)
        
        pygame.display.flip()

    def Atualizar():
        global Y_Player_1, X_Player_1

        key = pygame.key.get_pressed()

        if key[K_UP]:
            Y_Player_1 = Y_Player_1 + 0.3

        if key[K_DOWN]:
            Y_Player_1 = Y_Player_1 - 0.3

        if key[K_LEFT]:
            X_Player_1= X_Player_1 - 0.3

        if key[K_RIGHT]:
            X_Player_1 = X_Player_1 + 0.3



    pygame.init()

    pygame.display.set_mode((Size_Window2, Size_Window1), DOUBLEBUF | OPENGL)

    while True:
        Atualizar()
        Desenhar()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

if nun_per == 2:
    
    X_Player_1 = 0
    Y_Player_1 = 0

    X_Player_2 = 0
    Y_Player_2 = 0
    def largura_Dos_Players():
        return size_players

    def Altura_Dos_Players():
        return size_players

    def Desenhar_Players(x, y, largura, altura, r, g, b):
        glColor3f(r, g, b)
        glBegin(GL_QUADS)
        glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
        glVertex2f(0.5 * largura + x, -0.5 * altura + y)
        glVertex2f(0.5 * largura + x, 0.5 * altura + y)
        glVertex2f(-0.5 * largura + x, 0.5 * altura + y)    
        glEnd()  
    
    def Desenhar():
        glViewport(0, 0, Size_Window2, Size_Window1)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-Size_Window2 / 2, Size_Window2/ 2, -Size_Window1 / 2,Size_Window1 / 2, 0, 1 )
        glClear(GL_COLOR_BUFFER_BIT)
        Desenhar_Players(X_Player_1, Y_Player_1, largura_Dos_Players(), Altura_Dos_Players(), Color_R, Color_G, Color_B)
        Desenhar_Players(X_Player_2, Y_Player_2, largura_Dos_Players(), Altura_Dos_Players(), Color_R_2, Color_G_2, Color_B_2)
        pygame.display.flip()

    def Atualizar():
        global Y_Player_1, X_Player_1, Y_Player_2, X_Player_2

        key = pygame.key.get_pressed()

        if key[K_UP]:
            Y_Player_1 = Y_Player_1 + 0.3

        if key[K_DOWN]:
            Y_Player_1 = Y_Player_1 - 0.3

        if key[K_LEFT]:
            X_Player_1= X_Player_1 - 0.3

        if key[K_RIGHT]:
            X_Player_1 = X_Player_1 + 0.3

        if key[K_w]:
            pass
            Y_Player_2 = Y_Player_2 + 0.3

        if key[K_s]:
            Y_Player_2 = Y_Player_2 - 0.3

        if key[K_d]:
            X_Player_2 = X_Player_2 + 0.3

        if key[K_a]:
            X_Player_2 = X_Player_2 - 0.3

    pygame.init()

    pygame.display.set_mode((Size_Window2, Size_Window1), DOUBLEBUF | OPENGL)

    while True:
        Atualizar()
        Desenhar()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()














