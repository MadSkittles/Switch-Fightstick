from NXController import Controller

ctr = Controller()
## Or use your serial port if you have many
# ctr = Controller('/dev/tty.usbserial-AO0099VT');

# Hold two stick in the oppsite direction
ctr.LS_RIGHT(-1)
ctr.RS_LEFT(-1)
ctr.pause(5)
ctr.release()
# Backwards
ctr.LS_LEFT(-1)
ctr.RS_RIGHT(-1)
ctr.pause(5)
ctr.release()

ctr.close()