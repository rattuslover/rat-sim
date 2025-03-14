import os
import math
import pygame
#remember all degrees are in radians
#just some usefull functions im going to use later
def RadianToDegree(radian):
	return radian*57.2957795131
def DegreeToRadian(degree):
	return degree*0.01745329251
def GetAngle(pos):
	return math.atan2(pos[0], pos[1])
class Player:
	def __init__(self, health, speed, friction):
		self.health=health
		self.speed=speed
		self.position=[0, 0]
    		self.momentum=[0, 0]
		self.friction=0.8
  	def movement(self, direction):
		if direction=="up":
			self.momentum[1]-=speed
		if direction=="down":
			self.momentum[1]+=speed
		if direction=="left":
			self.momentum[0]-=speed
		if direction=="right":
			self.momentum[0]+=speed
		self.momentum[0]=self.momentum[0]*self.friction
		self.momentum[1]=self.momentum[1]*self.friction
		self.position[0]+=self.momentum[0]
		self.position[1]+=self.momentum[1]
	
