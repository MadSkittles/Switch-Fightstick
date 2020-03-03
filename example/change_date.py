from NXController import Controller

ctr = Controller()

for i in range(30):
	ctr.A()
	if i == 0:
		ctr.RIGHT()
		ctr.RIGHT()
	else:
		ctr.LEFT()
		ctr.LEFT()
		ctr.LEFT()
	ctr.UP()
	ctr.RIGHT(0.4)
	ctr.A()

ctr.close()