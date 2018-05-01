import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		self.screen=screen
		self.ai_settings=ai_settings
		#加载飞船外形并获取外接矩形
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()#屏幕的矩形
		#将飞船
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		self.center=float(self.rect.centerx)
		self.moving_right=False
		self.moving_left=False
		
		
	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			#self.rect.centerx+=1
			#self.center+=self.ai_settings.ship_speed_factor
			self.center+=self.ai_settings.ship_speed_factor
		elif self.moving_left and self.rect.right>0:
			#self.rect.centerx-=1
			
			#self.center-=self.ai_settings.ship_speed_factor
			self.center-=self.ai_settings.ship_speed_factor
			
		self.rect.centerx=self.center
	def blitme(self):
		self.screen.blit(self.image,self.rect)