from NXController import Controller

# Full party lead with flame body, on your bike, egg is ready to pick
# Text speed fast. No animation.

cycle = 20			# Egg cycles
hatchingtime = 9	# Unfreeze the game before fly, egg hatching time in seconds. 18 is safest
slot = 1			# The first party slot to be replaced (1~5)
N = 210				# Number of eggs to receive

ctr = Controller()
ctr.LS()
ctr.buttondelay = 0

for i in range(N):
	# Fly to Day Care in Wild Area
	ctr.X()
	ctr.pause(1)
	if i == 0: # Select map
		ctr.LS_DOWN(0.5)
		ctr.LS_LEFT(0.7)
	ctr.A()
	ctr.pause(2.5)
	ctr.A()
	ctr.pause(0.5)
	ctr.A()
	ctr.pause(2.8)

	# Go back to Day Care
	ctr.LS_DOWN(0.7)
	ctr.LS_RIGHT(0.2)
	ctr.pause(0.2)

	print(f"Picking {i + 1}th egg(s)")
	ctr.A()
	ctr.pause(1)
	ctr.A()
	ctr.pause(3)
	ctr.B()
	ctr.pause(2)
	ctr.A()
	ctr.pause(1.3)
	ctr.B()
	ctr.pause(2.1)
	for jj in range(slot):
		ctr.DOWN()
		ctr.pause(0.1)
	ctr.A()
	ctr.pause(2.5)
	ctr.B()
	ctr.pause(1.5)
	ctr.B()

	# Move forward
	ctr.LS_UP(2)
	ctr.LS_RIGHT(1)

	for c in range(cycle):
		ctr.B()
		ctr.LS_RIGHT(0.6)
		ctr.LS_DOWN(0.5)
		ctr.LS_LEFT(0.5)
		ctr.LS_UP(0.5)

	for cnt in range(hatchingtime):
		ctr.B()
		ctr.pause(0.9)

	slot = 1 if slot == 5 else slot + 1

if N >= 30:
	ctr.sleepmode()

ctr.close()