import pygame
import random
from queue import Queue

pygame.init()

#Clase que nos permite dividir un spritesheet
class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image

class button():
	def __init__(self,x,y,image,scale):
		width=image.get_width()
		height=image.get_height()
		self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
		self.rect=self.image.get_rect()
		self.rect.topleft=(x,y)
		self.clicked=False

	def draw(self,screen):
		action=False
		pos=pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
				action=True
				self.clicked=True
		
		if pygame.mouse.get_pressed()[0]==0:
				self.clicked=False

		screen.blit(self.image,(self.rect.x, self.rect.y))

		return action


#Clase que nos permite crear una animacion de un spritesheet
class animation():
	sprite_sheet=SpriteSheet
	def __init__(self,path,steps,cooldown,pwidth,pheight):
		sprite_sheet_path=pygame.image.load(path)
		self.sprite_sheet=SpriteSheet(sprite_sheet_path)
		self.animation_steps=steps
		self.animation_cooldown=cooldown
		self.width=pwidth
		self.height=pheight
		self.last_update=pygame.time.get_ticks()
		self.frame=0
		self.frames=[]


	def make_animation(self, scale,colour):
		animation_list=[]
		for x in range(self.animation_steps):
			animation_list.append(self.sprite_sheet.get_image(x,self.width,self.height,scale,colour))
		return animation_list
	
	def update_animation(self,animation_list):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.last_update >= self.animation_cooldown:
			self.frame+=1
			self.last_update=currentTime
			if self.frame >= len(animation_list):
				self.frame=0

#clase que permite jugar el juego de las teclas
class Keys_game():
	def __init__(self,path,steps,pwidth,pheight,scale):
		sprite_sheet_path=pygame.image.load(path)
		self.sprite_sheet=SpriteSheet(sprite_sheet_path)
		self.nkeys=steps
		self.width=pwidth
		self.height=pheight
		self.scale=scale
		self.frames=[]
		self.moves=Queue(maxsize=0)
	
	def random_keys_game(self, totalRand, colour):
		for x in range(totalRand):
			num=random.randint(0,3)
			self.frames.append(self.sprite_sheet.get_image(num ,self.width ,self.height ,self.scale,colour))
			match num:
				case 0:
					self.moves.put('w')
				case 1:
					self.moves.put('a')
				case 2:
					self.moves.put('s')
				case 3:
					self.moves.put('d')

class minigame1():
	def __init__(self):
		self.Astronaut=animation('assets\sprites\Minijuego1\AstronautaMin1.png',2,500,320,320)
		self.Astronaut_animation=self.Astronaut.make_animation(1,BLACK)
		self.Tornado=animation('assets\sprites\Minijuego1\TornadoMin1.png',3,500,320,960)
		self.Tornado_animation=self.Tornado.make_animation(1,BLACK)
		self.Teclas=Keys_game('assets\sprites\Minijuego1\TeclasMin1.png',4,240,240,0.4)
		self.Teclas.random_keys_game(4,BLACK)
		self.backG=pygame.image.load('assets\sprites\Minijuego1\FondoMin1.png').convert_alpha()
		self.backG=pygame.transform.scale(self.backG, (int(self.backG.get_width()*1.2),int(self.backG.get_height()*1.2)))
		self.A1=pygame.Rect(0,400,320,320)
		self.A2=pygame.Rect(-600,60,120,920)
		self.angle=1
		self.velAstro=1.8
		self.lose=0
		self.Astronaut_animation_rotated=pygame.image

	def load_minigame(self,screen,SCREEN_WIDTH,SCREEN_HEIGHT):
			
			screen.fill(BG)
			screen.blit(self.backG,(0,0))

			if pygame.Rect.colliderect(self.A1,self.A2) or self.A1.x>=SCREEN_WIDTH:
				return 0

			if self.lose==0:
				screen.blit(self.Astronaut_animation[self.Astronaut.frame], (self.A1.x, self.A1.y))
				self.Astronaut.update_animation(self.Astronaut_animation)

				if len(self.Teclas.frames)==0:
					self.velAstro=4

				#Dibujar teclas
				for x in range(len(self.Teclas.frames)):
					screen.blit(self.Teclas.frames[x], ((SCREEN_WIDTH/2-self.Teclas.width*self.Teclas.scale*len(self.Teclas.frames)/2)+(x*self.Teclas.width*self.Teclas.scale), SCREEN_HEIGHT/2))
			else:
				self.velAstro=0
				if self.angle<90:
					self.Astronaut_animation_rotated=pygame.transform.rotate(self.Astronaut_animation[self.Astronaut.frame],self.angle).convert_alpha()
					self.angle+=1
					self.A1.y+=1

				screen.blit(self.Astronaut_animation_rotated, (self.A1.x, self.A1.y))
			
			#Actualizar animacion
			self.Tornado.update_animation(self.Tornado_animation)

			#Dibujar imagen
			screen.blit(self.Tornado_animation[self.Tornado.frame], (self.A2.x, self.A2.y))

			#Movimiento de animacion
			self.A1.x+=self.velAstro
			self.A2.x+=3

			#El minijuego sigue funcionando
			return 2
	
	def key_inputs(self,event):
		if event.type == pygame.KEYDOWN and len(self.Teclas.frames)!=0:  
			if event.key == pygame.K_w and self.Teclas.moves.queue[0]=='w':
				self.Teclas.frames.pop(0)
				self.Teclas.moves.get()
			elif event.key == pygame.K_a and self.Teclas.moves.queue[0]=='a':
				self.Teclas.frames.pop(0)
				self.Teclas.moves.get()				
			elif event.key == pygame.K_s and self.Teclas.moves.queue[0]=='s':
				self.Teclas.frames.pop(0)
				self.Teclas.moves.get()				
			elif event.key == pygame.K_d and self.Teclas.moves.queue[0]=='d':
				self.Teclas.frames.pop(0)
				self.Teclas.moves.get()	
			else:
				self.lose=1

class menu():
	btStart=pygame.image
	tiStart=pygame.image
	bg=pygame.image
	btStartload=button
	def __init__(self):
		self.btStart=pygame.image.load('assets\sprites\MainMenu\Boton.png').convert_alpha()
		
		self.tiStart=pygame.image.load('assets\sprites\MainMenu\Titulo1.png').convert_alpha()
		self.tiStart=pygame.transform.scale(self.tiStart, (int(self.tiStart.get_width()*0.35),int(self.tiStart.get_height()*0.35)))
		self.bg=pygame.image.load('assets\sprites\MainMenu\\bg.png').convert_alpha()
		self.bg=pygame.transform.scale(self.bg,(int(self.bg.get_width()*0.4),int(self.bg.get_height()*0.4)))
		self.btStartload=button(400,580,self.btStart,0.3)
	
	def menu_load(self,screen):
		minigame=0

		screen.blit(self.bg,(200,80))
		screen.blit(self.tiStart,(220,0))

		if self.btStartload.draw(screen):
			minigame=2
		
		return minigame
		
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Titan3023')

BG = (50, 50, 50)
BLACK = (0, 0, 0)
fps=60

#Seleccionando el nivel
minigame=0

menu_inst=menu()
minigame1_inst=minigame1()

#Creando un clock para limitar los Fps
clock=pygame.time.Clock()
run = True
while run:
	clock.tick(fps)

	#update background
	screen.fill(BG)	

	match minigame:
		case 0:
			minigame=menu_inst.menu_load(screen)
		case 2:
			minigame=minigame1_inst.load_minigame(screen,SCREEN_WIDTH,SCREEN_HEIGHT)
			if(minigame==0):
				print('reiniciando minijuego')
				del minigame1_inst
				minigame1_inst=minigame1()



	pygame.display.update()

	for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False	
				if minigame==2:
					minigame1_inst.key_inputs(event)

pygame.quit()