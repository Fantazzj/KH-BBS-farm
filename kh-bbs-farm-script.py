import time

a = 0

def press(k, t=0.1):
	keyboard.setKeyDown(k)
	time.sleep(t)
	keyboard.setKeyUp(k)

def wait(t):
	time.sleep(t)

wait(5)
while True:
	a+=1
	press(Key.W,4)
	press(Key.A,1.5)
	wait(0.5)
	press(Key.F)
	wait(4)
	press(Key.F)
	wait(2.5)
	#press(Key.A,1.9) #for Ventus
	press(Key.A,1.7) #for Aqua
	#press(Key, ) #TODO for Terra
	press(Key.W,5)
	wait(1)
	press(Key.C)
	if a==2:
		wait(20)
		a=0
	press(Key.S,2)
	wait(2)
