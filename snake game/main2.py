import pygame #library pygame

width, height = 600, 600 #ukuran display dengan tinggi 600px dan lebar 600px
size = 20 
fps = 10 #nilai pada variabel fps untuk mengatur kecepatan snake

class Snake:
    #fungsi inisiasi untuk objek snake
    def __init__(self):
        self.segments = []
        self.vel_x = 1
        self.vel_y = 0
        self.create_snake()
        self.head = self.segments[0]
    
    #fungsi untuk membuat snake dengan jumlah 3 kotak
    def create_snake(self):
        x = 300
        for _ in range(3):
            self.add_segment(x, 300)
            x -= size
            
    #fungsi untuk menambahkan segment yang membentuk bagian ekornya
    def add_segment(self, posx, posy):
        new_segment = pygame.Rect(posx, posy, size, size)  
        self.segments.append(new_segment)
        
    #fungsi untuk menambahkan snake pada window
    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(window,(255,255,255), segment)
            
    #fungsi update snake. untuk pemisahan bagian head dan ekor
    def update(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].x = self.segments[i-1].x 
            self.segments[i].y = self.segments[i-1].y 
        self.head.x += self.vel_x * size
        self.head.y += self.vel_y * size
        
    #membuat fungsi event handler untuk menggerakan snake dengan keyboard
    def up(self):
        self.vel_x = 0
        self.vel_y = -1
    def down(self):
        self.vel_x = 0
        self.vel_y = 1
    def left(self):
        self.vel_x = -1
        self.vel_y = 1
    def left(self):
        self.vel_x = -1
        self.vel_y = 0
    def right(self):
        self.vel_x = 1
        self.vel_y = 0 

pygame.init() #inisiasi game
window = pygame.display.set_mode((width, height)) #set window display
pygame.display.set_caption("Snake- Game") #set untuk judul game. bisa dikustomisasi sesuai kebutuhan


player = Snake()
clock = pygame.time.Clock() #pengaturan batasan speed dari variabel fps
running = True #Kondisi loop Game 

#isi dari redraw window. bisa dirubah warna window dan calon snake-nya
def redraw_window():
    window.fill((0,0,0))
    #draw seluruh elemen
    player.draw()
    pygame.display.flip()
    
while running: #selama game running apa yang dikerjakan ketika game berlangsung
    clock.tick(fps)
    redraw_window() #kondisi while running isi game
    #kondisi while running untuk quit
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #event handler untuk menggerakan snake
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
                
# pygame.quit()
                