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

#Clase que nos permite crear una animacion de un spritesheet
class animation():
	animation_steps=0
	width=0
	height=0
	last_update=pygame.time.get_ticks()
	animation_cooldown=0
	frame=0
	sprite_sheet=SpriteSheet
	frames=[]
	def __init__(self,path,steps,cooldown,pwidth,pheight):
		sprite_sheet_path=pygame.image.load(path)
		self.sprite_sheet=SpriteSheet(sprite_sheet_path)
		self.animation_steps=steps
		self.animation_cooldown=cooldown
		self.width=pwidth
		self.height=pheight
		self.last_update=pygame.time.get_ticks()


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
	nkeys=0
	width=0
	height=0
	scale=0
	sprite_sheet=SpriteSheet
	frames=[]
	moves=Queue(maxsize=0)
	def __init__(self,path,steps,pwidth,pheight,scale):
		sprite_sheet_path=pygame.image.load(path)
		self.sprite_sheet=SpriteSheet(sprite_sheet_path)
		self.nkeys=steps
		self.width=pwidth
		self.height=pheight
		self.scale=scale
	
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
	Astronaut=animation
	Tormenta=animation
	Tornado=animation
	Astronaut_animation=[]
	Tormenta_animation=[]
	Tornado_animation=[]
	velAstro=1
	angle=1
	lose=0
	Teclas=Keys_game
	A1=pygame.Rect(0,500,320,320)
	A2=pygame.Rect(-400,150,320,320)
	A3=pygame.Rect(-700,500,320,320)
	Astronaut_animation_rotated=pygame.image
	def __init__(self):
		self.Astronaut=animation('assets\sprites\Minijuego1\AstronautaMin1.png',2,500,320,320)
		self.Astronaut_animation=self.Astronaut.make_animation(1,BLACK)
		self.Tormenta=animation('assets\sprites\Minijuego1\TormentaMin1.png',2,500,320,320)
		self.Tormenta_animation=self.Tormenta.make_animation(1,BLACK)
		self.Tornado=animation('assets\sprites\Minijuego1\TornadoMin1.png',2,500,320,320)
		self.Tornado_animation=self.Tornado.make_animation(1,BLACK)
		self.Teclas=Keys_game('assets\sprites\Minijuego1\TeclasMin1.png',4,240,240,0.4)
		self.Teclas.random_keys_game(4,BLACK)

	def load_minigame(self,screen,SCREEN_WIDTH,SCREEN_HEIGHT):
			
			screen.fill(BG)

			if self.lose==0:
				screen.blit(self.Astronaut_animation[self.Astronaut.frame], (self.A1.x, self.A1.y))
				self.Astronaut.update_animation(self.Astronaut_animation)

				if len(self.Teclas.frames)==0:
					self.velAstro=2.5

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
			self.Tormenta.update_animation(self.Tormenta_animation)
			self.Tornado.update_animation(self.Tornado_animation)

			#Dibujar imagen
			screen.blit(self.Tormenta_animation[self.Tormenta.frame], (self.A2.x, self.A2.y))
			screen.blit(self.Tornado_animation[self.Tornado.frame], (self.A3.x, self.A3.y))

			#Movimiento de animacion
			self.A1.x+=self.velAstro
			self.A2.x+=1
			self.A3.x+=2

					#Cerrando pygame por si se cierra la ventana
			for event in pygame.event.get():
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
				

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

BG = (50, 50, 50)
BLACK = (0, 0, 0)
fps=60

#Seleccionando minijuego y condicion de perdida
minigame=1

minigame1_inst=minigame1()

#Creando un clock para limitar los Fps
clock=pygame.time.Clock()
run = True
while run:
	clock.tick(fps)

	#update background
	screen.fill(BG)	

	#Cargamos minijuego1
	minigame1_inst.load_minigame(screen,SCREEN_WIDTH,SCREEN_HEIGHT)

	pygame.display.update()

	for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

pygame.quit()