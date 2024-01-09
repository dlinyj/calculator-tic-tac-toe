import math 

x = 0
y = 0
p2 = 0
p7 = 0
p8 = 0

def calc_win():
	global x
	print(f"Calc winer! x={x}")
	exit()

def draw_win():
	print(f"Draf... x={x}")
	exit()

def input_x():
	global x
	global y
	y = x
	print(x)
	x = int(input())

def subprog():
	global x
	global y
	global p2 #A
	global p7 #B
	global p8 #C
	x = x - 1	#24.1 #25.- #27.29 
	if x == 0:	#26.Fx=0 
		x = 8	#28.8 
	p2 = x		#29.П2 
	input_x()	#30.С/П 
	p7 = x		#31.П7 
	x = p2		#32.ИП2 
	x = x - 4	#33.4 #34.- 
	if (x <= 0): #35.Fx#0 #36.39 #37.Fx<0 #38.41 
		x = x + 8 #39.8 #40.+ 
	p8 = x		#41.П8
	x = x - p7	#42.ИП7 #43.- 
	if (x == 0):#44.Fx=0 
		x = p2
	else:
		x = p8
		calc_win()


x = 9			#00.9  
input_x()		#01.С/П 
subprog()		#02.ПП #03.24
x = x * math.pi #04.Fпи #05.x 
x = math.cos(x) #06.Fcos 
if x < 0: 		#07.Fx<0  
	x = p2		#09.ИП2 
	subprog()	#10.ПП #11.24 
	x = x - 1	#12.1 #13.- 
	calc_win()	#14.БП #15.49 
x = p7			#16.ИП7 
subprog()		#17.ПП #18.24 
x = p7			#19.ИП7 
subprog()		#20.ПП #21.24 
#x = 0			#22.0 
draw_win()		#23.С/П 

