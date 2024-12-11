import ctypes
from threading import Thread
import pygame


ctypes.windll.shcore.SetProcessDpiAwareness(1)
def Main():
    pygame.init()
    pygame.font.init()
    AccentColour = (250,250,250)
    Title = 'Platform'
    Name = (" "*len(Title)) + Title
    screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SRCALPHA | pygame.NOFRAME)
    x, y = screen.get_size()
    pygame.display.set_caption(Title)
    Raw_Close = pygame.image.load(r"Accessories/Images/Buttons/Close Button.png").convert()
    Close = pygame.transform.smoothscale(Raw_Close, (40,40))
    Raw_HClose = pygame.image.load(r"Accessories/Images/Buttons/Close Button (Highlighted).png").convert()
    HClose = pygame.transform.smoothscale(Raw_HClose, (40,40))
    Raw_Minimise = pygame.image.load(r"Accessories/Images/Buttons/Minimise Button.png").convert()
    Minimise = pygame.transform.smoothscale(Raw_Minimise, (40,40))
    Raw_HMinimise = pygame.image.load(r"Accessories/Images/Buttons/Minimise (Highlighted).png").convert()
    HMinimise = pygame.transform.smoothscale(Raw_HMinimise, (40,40))
    pygame.key.set_repeat(200,50)
    font1 = pygame.font.Font(r'Accessories/Fonts/Lexend/static/Lexend-Regular.ttf',20)
    text1 = font1.render(Name, True, AccentColour)
    textRect1 = text1.get_rect() 
    textRect1.center = (50, 20)
    text2 = font1.render("GUI Console", True, AccentColour)
    textRect2 = text2.get_rect() 
    textRect2.center = (50, 20)
    running = True
    Communicator_File = open(r"Accessories/Texts/Communicator.txt","w")
    Communicator_File.write("$tartUp Complete")
    Communicator_File.close()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    running = False
                if event.key == pygame.K_LALT and event.key == pygame.K_w:
                    running  = False
    
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.fill((20, 20, 30))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, x-80, 40),0,7,0,7,0)
        textRect1.center = (50, 20)
        screen.blit(text1, textRect1)
        textRect2 = text2.get_rect() 
        textRect2.center = (x/2, y/2)
        screen.blit(text2, textRect2)

        if mouse_x > x-40 and mouse_y < 40:
            screen.blit(HClose, (x-40, 0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                i = 1
                while i < y:
                    screen = pygame.display.set_mode((x,y-i))
                    i = i*1.1
                screen = pygame.display.set_mode((x,0))
                running = False
        else:
            screen.blit(Close, (x-40, 0)) 
        if mouse_x > x-80 and mouse_x < x-40 and mouse_y < 40:
            screen.blit(HMinimise, (x-80, 0)) 
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen = pygame.display.set_mode((x, y))
                pygame.display.iconify()
        else:
            screen.blit(Minimise, (x-80, 0))    

        pygame.display.flip()
    pygame.quit()

main_thread = Thread(target=Main)
main_thread.start()
main_thread.join()