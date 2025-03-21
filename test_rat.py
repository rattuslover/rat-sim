H=min
G=False
E=True
C=int
import pygame as B,os
class L:
	def __init__(A,x,y,image,flip_image):B=image;A.x=x;A.y=y;A.image=B;A.normal_image=B;A.flip_image=flip_image;A.vel_x=0;A.vel_y=0
	def update_image(A,facing_right=E):A.image=A.normal_image if facing_right else A.flip_image
class A:
	def __init__(A,base_width=750,base_height=500,scale=None):
		J=scale;I=base_height;F=base_width;B.init()
		if J is None:K=B.display.Info();M=K.current_w/F;N=K.current_h/I;J=H(M,N)
		A.scale=J;A.width=C(F*A.scale);A.height=C(I*A.scale);A.window=B.display.set_mode((A.width,A.height),B.FULLSCREEN);B.display.set_caption('Rat Sim dev Version');A.clock=B.time.Clock();A.max_speed=600;A.acceleration=800;A.deceleration=900;A.current_vel=0;A.run=E;A.sprint=E;A.stamina=100;A.openedshop=G;A.font=B.font.SysFont('consolas',C(20*A.scale));A.bg=B.image.load('assets/background.png');A.bg=B.transform.scale(A.bg,(A.width,A.height));A.shoprat=B.image.load('assets/shoprat.png');A.shoprat=B.transform.scale(A.shoprat,(C(105*A.scale),C(75*A.scale)));A.shop_icon_pos=C(200*A.scale),C(130*A.scale);A.entshoptext=A.font.render('Press E to enter or close the shop',E,(0,0,0));D=B.image.load('assets/transparentrat.png');O=C(125*A.scale);P=C(75*A.scale);D=B.transform.scale(D,(O,P));Q=B.transform.flip(D,E,G);A.player=L(C(F*.45*A.scale),C(I*.45*A.scale),D,Q);print('Right-shift to sprint, Q to regain stamina.')
	def draw(A):
		A.window.blit(A.bg,(0,0))
		if not A.openedshop:
			A.window.blit(A.shoprat,A.shop_icon_pos)
			if C(140*A.scale)<=A.player.x<=C(240*A.scale)and C(90*A.scale)<=A.player.y<=C(145*A.scale):A.window.blit(A.entshoptext,(A.player.x+C(100*A.scale),A.player.y+C(100*A.scale)))
		A.window.blit(A.player.image,(A.player.x,A.player.y));D=A.font.render('Stamina: '+str(C(A.stamina)),E,(0,0,0));A.window.blit(D,(C(25*A.scale),A.height-C(40*A.scale)));B.display.flip()
	def handle_keys(A,dt):
		C=dt;D=B.key.get_pressed();F=A.max_speed
		if D[B.K_RSHIFT]and A.sprint and A.stamina>0:F*=1.5;A.stamina-=20*C
		elif A.stamina<=0:F*=.6
		if D[B.K_w]or D[B.K_UP]:A.player.vel_y-=A.acceleration*C
		elif D[B.K_s]or D[B.K_DOWN]:A.player.vel_y+=A.acceleration*C
		else:A.apply_friction_y(C)
		if D[B.K_a]or D[B.K_LEFT]:A.player.update_image(facing_right=G);A.player.vel_x-=A.acceleration*C
		elif D[B.K_d]or D[B.K_RIGHT]:A.player.update_image(facing_right=E);A.player.vel_x+=A.acceleration*C
		else:A.apply_friction_x(C)
		A.player.vel_x=max(-F,H(F,A.player.vel_x));A.player.vel_y=max(-F,H(F,A.player.vel_y));A.player.x+=A.player.vel_x*C;A.player.y+=A.player.vel_y*C
		if A.player.x<=-150*A.scale:A.player.x=A.width
		elif A.player.x>=A.width:A.player.x=-150*A.scale
		if A.player.y<=-60*A.scale:A.player.y=A.height
		elif A.player.y>=A.height:A.player.y=-60*A.scale
		if D[B.K_q]and A.stamina<100:A.stamina+=10*C
	def apply_friction_x(A,dt):
		if A.player.vel_x>0:
			A.player.vel_x-=A.deceleration*dt
			if A.player.vel_x<0:A.player.vel_x=0
		elif A.player.vel_x<0:
			A.player.vel_x+=A.deceleration*dt
			if A.player.vel_x>0:A.player.vel_x=0
	def apply_friction_y(A,dt):
		if A.player.vel_y>0:
			A.player.vel_y-=A.deceleration*dt
			if A.player.vel_y<0:A.player.vel_y=0
		elif A.player.vel_y<0:
			A.player.vel_y+=A.deceleration*dt
			if A.player.vel_y>0:A.player.vel_y=0
	def game_loop(A):
		while A.run:
			C=A.clock.tick(60)/1e3
			for D in B.event.get():
				if D.type==B.QUIT:A.run=G
			A.handle_keys(C);A.draw()
		B.quit()
if __name__=='__main__':D=A();D.game_loop()
