import pygame #library pygame
import random

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
        self.alive = True
        self.score = 0
    
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
        
    #Fungsi untuk cek tabrakan bisa menabrak tembok dan apa yang trjadi? menabrak ekor sendiri dan apa yang terjadi? serta jika menabrak food dan apa yang terjadi?
    def check_collision(self):
        #keluar atau nabrak tembok
        if self.head.left < 0 or self.head.right > width or self.head.top < 0 or self.head.bottom > height:
            self.alive = False
        #cek collision head dengan segments
        for segment in self.segments[1:]:
            if self.head.colliderect(segment):
                self.alive = False
                
        #Cek collision dengan food
        if self.head.colliderect(food.rect):
            self.add_segment(self.segments[-1].x, self.segments[-1].y)
            food.reset_pos()
            self.score +=1
            return True 

    #membuat fungsi event handler untuk menggerakan snake dengan keyboard
    def up(self):
        if not self.head.y - self.segments[1].y == size: #membuat bentukan sudut disetiap pergerakan snake membuat gambar menjadi ralistis
            self.vel_x = 0
            self.vel_y = -1
    def down(self):
        if not self.head.y - self.segments[1].y == size:
            self.vel_x = 0
            self.vel_y = 1
    def left(self):
        if not self.head.x - self.segments[1].x == size:
            self.vel_x = -1
            self.vel_y = 1
    def right(self):
        if not self.head.x - self.segments[1].x == size:
            self.vel_x = 1
            self.vel_y = 0 
    def restart(self):
        self.__init__()

#membuat fungsi m=untuk menambahkan objek makanan
class Food:
    def __init__(self, player):
        self.player = player
        self.rect = pygame.Rect(0,0, size, size)
        self.reset_pos()
        
    def reset_pos(self):
        is_valid = False
        while not is_valid:
            self.rect.x = random.randint(0, width//size - 1)* size
            self.rect.y = random.randint(0, width//size - 1)*size
            collide = False
            for segment in player.segments:
                if self.rect.colliderect(segment):
                    collide = True
            is_valid = not collide
            
    def draw(self):
        pygame.draw.circle(
            window, "red", (self.rect.centerx, self.rect.centery), size//2
            )
    def restart(self):
        self.__init__(self.player)    
        
pygame.init() #inisiasi game
pygame.font.init()
window = pygame.display.set_mode((width, height)) #set window display
pygame.display.set_caption("Snake- Game") #set untuk judul game. bisa dikustomisasi sesuai kebutuhan
player = Snake()
food = Food(player)
clock = pygame.time.Clock() #pengaturan batasan speed dari variabel fps
font = pygame.font.SysFont("Arial", 18)
speed = 0.25
running = True #Kondisi loop Game 

#isi dari redraw window. bisa dirubah warna window dan calon snake-nya
def redraw_window():
    window.fill((0, 0, 0))
    # Draw all elements
    player.draw()
    food.draw()
    scoreboard = font.render(f"Score: {player.score}", False, "green")
    window.blit(scoreboard, (0, 0))
    pygame.display.flip()
    
while running: #selama game running apa yang dikerjakan ketika game berlangsung
    clock.tick(fps*speed)
    redraw_window() #kondisi while running isi game
    #kondisi while running untuk quit
    player.update()
    if player.check_collision():
        speed += 0.01
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
            elif event.key == pygame.K_F2:
                if not player.alive:
                    player.restart()
                    food.restart()
                
# pygame.quit()
                