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
	def __init__(self, health, speed):
		self.health=health
		self.speed=speed
		self.position=[0, 0]
    self.momentum=[0, 0]
  def movement(self, direction):
      if direction=="up":
        self.momentum[1]+=speed
class Ground:
