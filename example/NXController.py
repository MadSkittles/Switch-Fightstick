#!/usr/bin/env python3
import serial
import serial.tools.list_ports
from time import sleep


class Controller:
    def __init__(self, serial_port=None, printout=False):
        if serial_port is None:
            serial_port = Controller.find_port()[0]
            print(f"Using port: {serial_port}")
        self.ser = serial.Serial(serial_port, 9600)
        self.buttondelay = 0.1
        self.printout = printout

    @staticmethod
    def find_port():
        ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if p.vid is not None and p.pid is not None
        ]
        if not ports:
            raise IOError("No device found")
        if len(ports) > 1:
            print("Found multiple devices:")
            for p in ports:
                print(p)
        return ports

    def write(self, msg):
        self.ser.write(f"{msg}\r\n".encode("utf-8"))

    def release(self):
        self.ser.write(b"RELEASE\r\n")

    # Negative or zero duration to hold the button
    def send(self, msg, duration=0.1):
        if self.printout:
            print(msg)
        self.write(msg)
        if duration > 0:
            sleep(duration)
            self.release()
            sleep(self.buttondelay)

    def pause(self, duration):
        sleep(duration)

    def close(self):
        self.release()
        sleep(0.5)
        self.ser.close()
        print("Connection closed!")

    def __enter__(self):
        # self.ZL()
        # self.pause(0.5)
        return self

    def __exit__(self, type, value, trace):
        self.close()

    def combinations(self, button_lists, duration=0.1):
        valid_button_sets = {
            self.A,
            self.B,
            self.X,
            self.Y,
            self.L,
            self.R,
            self.ZL,
            self.ZR,
            self.LS,
            self.RS,
            self.PLUS,
            self.MINUS,
            self.HOME,
            self.CAPTURE,
            self.LEFT,
            self.UP,
            self.RIGHT,
            self.DOWN,
            self.LS_LEFT,
            self.LS_UP,
            self.LS_RIGHT,
            self.LS_DOWN,
            self.RS_LEFT,
            self.RS_UP,
            self.RS_RIGHT,
            self.RS_DOWN
        }
        
        if any(button not in valid_button_sets for button in button_lists):
            raise IOError("Invalid controller command")

        for button in button_lists:
            button(-1)
        self.pause(duration)
        self.release()

    # Botton
    def A(self, duration=0.1):
        self.send("Button A", duration)

    def B(self, duration=0.1):
        self.send("Button B", duration)

    def X(self, duration=0.1):
        self.send("Button X", duration)

    def Y(self, duration=0.1):
        self.send("Button Y", duration)

    def L(self, duration=0.1):
        self.send("Button L", duration)

    def R(self, duration=0.1):
        self.send("Button R", duration)

    def ZL(self, duration=0.1):
        self.send("Button ZL", duration)

    def ZR(self, duration=0.1):
        self.send("Button ZR", duration)

    # Press down left stick
    def LS(self, duration=0.1):
        self.send("Button LCLICK", duration)

    # Press down right stick
    def RS(self, duration=0.1):
        self.send("Button RCLICK", duration)

    # Plus
    def PLUS(self, duration=0.1):
        self.send("Button PLUS", duration)

    # Minus
    def MINUS(self, duration=0.1):
        self.send("Button MINUS", duration)

    # Home
    def HOME(self, duration=0.1):
        self.send("Button HOME", duration)

    # Capture
    def CAPTURE(self, duration=0.1):
        self.send("Button CAPTURE", duration)

    # DPAD
    def LEFT(self, duration=0.1):
        self.send("HAT LEFT", duration)

    def UP(self, duration=0.1):
        self.send("HAT TOP", duration)

    def RIGHT(self, duration=0.1):
        self.send("HAT RIGHT", duration)

    def DOWN(self, duration=0.1):
        self.send("HAT BOTTOM", duration)

    # LEFT STICK
    def LS_LEFT(self, duration=0.1):
        self.send("LX MIN", duration)

    def LS_RIGHT(self, duration=0.1):
        self.send("LX MAX", duration)

    def LS_DOWN(self, duration=0.1):
        self.send("LY MAX", duration)

    def LS_UP(self, duration=0.1):
        self.send("LY MIN", duration)

    # RIGHT STICK
    def RS_LEFT(self, duration=0.1):
        self.send("RX MIN", duration)

    def RS_RIGHT(self, duration=0.1):
        self.send("RX MAX", duration)

    def RS_DOWN(self, duration=0.1):
        self.send("RY MAX", duration)

    def RS_UP(self, duration=0.1):
        self.send("RY MIN", duration)

    # Quick Example
    def quit_app(self):
        self.HOME()
        sleep(0.5)
        self.X()
        self.A()

    def enter_app(self):
        self.A()
        sleep(1)
        self.A()

    def unlock(self):
        self.A()
        sleep(2)
        self.A()
        self.A()
        self.A()

    def sleepmode(self):
        self.HOME()
        sleep(0.5)
        self.DOWN()
        self.RIGHT(0.7)
        self.A()
        sleep(0.5)
        self.A()
        print("Switch entering sleep mode")

    # Key combinations
    # L + R (Example 1)
    def LR(self, duration=0.1):
        self.send("Button L\r\nButton R", duration)

    # DPAD_UP + B + X (Example 2)
    def AccessBackupSave(self, duration=0.1):
        # self.send('HAT TOP\r\nButton B\r\nButton X', duration)
        self.UP(-1)
        self.B(-1)
        self.X(-1)
        if duration > 0:
            sleep(duration)
            self.release()
            sleep(self.buttondelay)