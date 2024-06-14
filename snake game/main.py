import pygame #library pygame

width, height = 600, 600 #ukuran display dengan tinggi 600px dan lebar 600px
size = 20 

pygame.init() #inisiasi game
window = pygame.display.set_mode((width, height)) #set window display
pygame.display.set_caption("Snake-sanake") #set untuk judul game. bisa dikustomisasi sesuai kebutuhan

running = True #Kondisi loop Game 

#koordinat untuk kotak calon snake
x = 0 
y = 0

#isi dari redraw window. bisa dirubah warna window dan calon snake-nya
def redraw_window():
    window.fill((0,0,0))
    #draw seluruh elemen
    pygame.draw.rect(window, "white", (x*size, y*size, size, size))
    pygame.display.flip()
    
while running: #selama game running apa yang dikerjakan ketika game berlangsung
    redraw_window() #kondisi while running isi game
    #kondisi while running untuk quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #event handler untuk menggerakan snake
        elif event.type == pygame.K_DOWN:
            if event.key == pygame.K_UP:
                y -= 1
            elif event.key == pygame.KEYDOWN:
                y += 1
            elif event.key == pygame.K_LEFT:
                x -= 1
            elif event.key == pygame.K_RIGHT:
                x += 1
                
# pygame.quit()
                