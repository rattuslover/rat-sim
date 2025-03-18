import os
import math
import pygame
#remember all degrees are in radians
#just some usefull functions im going to use later
def RadianToDegree(radian):
	"""
 	Takes an input as a radian, and outputs it in degrees.
  	It just makes ur life easier

    	example:
     	-------------------
	>>> RadianToDegree(π)
 	180
	-------------------
 	You should also see DegreeToRadian
  	"""
	return radian*57.2957795131
def DegreeToRadian(degree):
	"""
 	Takes an input as a degree, and outputs it in radians.
  	It just makes ur life easier

    	example:
     	-------------------
	>>> DegreeToRadian(180)
 	π
	-------------------
 	You should also see RadianToDegree
  	"""
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
	
