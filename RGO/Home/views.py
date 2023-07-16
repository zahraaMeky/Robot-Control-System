from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import json
#for work remote and robot together 
from threading import Thread
import threading
import socket
from time import sleep
from datetime import datetime
#for serial port of remote 
from serial import Serial
#for send data as json
from django.http import JsonResponse
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
# import cv2
    
    #!/usr/bin/python3    

# Robot Status
#---- parameter --- | --- Meaning
#       Batt        |     Robot Battery
#       temp        |     temperature
#       pres        |     pressure
#    connected      |     Robot connection
#    last_seen      |     last seen
class Robot:
	def __init__(self , connected, jd):
		self.data = {"Batt":0, "temp":0, "pres":0, "connected": "disconnected"}
		self.jd = None
		#self.last_seen = None
		if (connected != None):
			if (connected):
				#self.connected = "connected"
				self.data["connected"] = "connected"
			else:
				#self.connected = "disconnected"
				self.data["connected"] = "disconnected"

		else:
			#self.connected = None
			self.data["connected"] = None
		if(jd!=None):
			self.jd = jd
			#self.Batt = jd['Batt']
			#self.temp = jd['temp']
			#self.pres = jd['pres']
			#self.Ia = jd['Ia']
			#self.Ib = jd['Ib']
			self.data["Batt"] = jd['Batt']
			self.data["temp"] = jd['temp']
			self.data["pres"] = jd['pres']
			#self.data["Ia"] = jd['Ia']
			#self.data["Ia"] = jd['Ia']

	def setData(self, connected, jd):
		if (connected != None):
			if(connected): 
				#self.connected = "connected"
				self.data["connected"] = "connected"
			else: 
				#self.connected = "disconnected"
				self.data["connected"] = "disconnected"
		if (jd != None):
			self.jd = jd
			#self.Batt = jd['Batt']
			#self.temp = jd['temp']
			#self.pres = jd['pres']
			#self.Ia = jd['Ia']
			#self.Ib = jd['Ib']
			self.data["Batt"] = jd['Batt']
			self.data["temp"] = jd['temp']
			self.data["pres"] = jd['pres']
			self.data["Ia"] = jd['Ia']
			self.data["Ia"] = jd['Ia']

	def setLastSeen(self, lastseen):
		if (lastseen != None):
			self.last_seen = lastseen
			self.data["last_seen"] = lastseen

	def getData(self):
         return self.data

	def printAllData(self):
		if (self.jd != None):
			print("\nRobot Status")
			print("* Battery      : " , self.data["Batt"] , " V"  )
			print("* Temperature  : ", self.data["temp"]  , " C"  )
			print("* Pressure     : ", self.data["pres"]  , " bar")
			print("* Connection   : ", self.data["connected"]  )
			print("* Last Seen    : ", self.data["last_seen"] )

##Start take data from Robot and Remote and display it in index.html
### *** Remote class that handle remote data parameters
# Remote Object
#---- parameter ----  | --- Meaning
#    connected        |     Remote connection
#     Batt_lvl        |     Remote Battery
#    point_btn        |     point_btn
#    Fire_btn         |     Fire_btn
#    gun1_btn         |     gun1_btn
#    gun2_btn         |     gun2_btn
#    gun3_btn         |     gun3_btn
#    gun4_btn         |     gun4_btn
#    brake_btn        |     brake_btn
#    drive_btn        |     drive_btn
#    PTZ_btn          |     PTZ_btn
#    mouse_btn        |     mouse_btn
#    silent_btn       |     silent_btn
#    mic_btn          |     mic_btn
#    mouseRL_btn      |     mouseRL_btn
#    speedUpDown_btn  |     speedUpDown_btn
#    openClose_btn    |     openClose_btn
#    gripRL_btn       |     gripRL_btn
#    handUpDown_btn   |     handUpDown_btn
#    armUpDown_btn    |     armUpDown_btn
#    armFB_btn        |     armFB_btn
#    armRotRL_btn     |     armRotRL_btn
#    R_Joystick1      |     R_Joystick1
#    R_Joystick2      |     R_Joystick2
#    L_Joystick1      |     L_Joystick1
#    L_Joystick2      |     L_Joystick2
#    L_Joystick3      |     L_Joystick3
class Remote :
	def __init__(self, sd,jd,connected):
		self.data = {'Batt_lvl':0 , 'rem_connected': 'disconnected'}
		if connected: self.data['rem_connected'] = 'connected'
		else:  self.data['rem_connected'] = 'disconnected'
        
		
		if (sd!=None):
			self.string_data = sd
		if (jd!=None):
			self.json_data = jd
			# self.point_btn = jd['point_btn']
			# self.Fire_btn = jd['Fire_btn']
			# self.gun1_btn = jd['gun1_btn']
			# self.gun2_btn = jd['gun2_btn']
			# self.gun3_btn = jd['gun3_btn']
			# self.gun4_btn = jd['gun4_btn']
			# self.brake_btn = jd['brake_btn']
			# self.drive_btn = jd['drive_btn']
			# self.PTZ_btn = jd['PTZ_btn']
			# self.mouse_btn = jd['mouse_btn']
			# self.silent_btn = jd['silent_btn']
			# self.mic_btn = jd['mic_btn']
			# self.mouseRL_btn = jd['mouseRL_btn']
			# self.speedUpDown_btn = jd['speedUpDown_btn']
			# self.openClose_btn = jd['openClose_btn']
			# self.gripRL_btn = jd['gripRL_btn']
			# self.handUpDown_btn = jd['handUpDown_btn']
			# self.armUpDown_btn = jd['armUpDown_btn']
			# self.armFB_btn = jd['armFB_btn']
			# self.armRotRL_btn = jd['armRotRL_btn']
			# self.R_Joystick1 = jd['R_Joystick1']
			# self.R_Joystick2 = jd['R_Joystick2']
			# self.L_Joystick1 = jd['L_Joystick1']
			# self.L_Joystick2 = jd['L_Joystick2']
			# self.L_Joystick3 = jd['L_Joystick3']
			# self.Batt_lvl = jd['Batt_lvl']

			self.data['point_btn'] = jd['point_btn']
			self.data['Fire_btn'] = jd['Fire_btn']
			self.data['gun1_btn'] = jd['gun1_btn']
			self.data['gun2_btn'] = jd['gun2_btn']
			self.data['gun3_btn'] = jd['gun3_btn']
			self.data['gun4_btn'] = jd['gun4_btn']
			self.data['brake_btn'] = jd['brake_btn']
			self.data['drive_btn'] = jd['drive_btn']
			self.data['PTZ_btn'] = jd['PTZ_btn']
			self.data['mouse_btn'] = jd['mouse_btn']
			self.data['silent_btn'] = jd['silent_btn']
			self.data['mic_btn'] = jd['mic_btn']
			self.data['mouseRL_btn'] = jd['mouseRL_btn']
			self.data['speedUpDown_btn'] = jd['speedUpDown_btn']
			self.data['openClose_btn'] = jd['openClose_btn']
			self.data['gripRL_btn'] = jd['gripRL_btn']
			self.data['handUpDown_btn'] = jd['handUpDown_btn']
			self.data['armUpDown_btn'] = jd['armUpDown_btn']
			self.data['armFB_btn'] = jd['armFB_btn']
			self.data['armRotRL_btn'] = jd['armRotRL_btn']
			self.data['R_Joystick1'] = jd['R_Joystick1']
			self.data['R_Joystick2'] = jd['R_Joystick2']
			self.data['L_Joystick1'] = jd['L_Joystick1']
			self.data['L_Joystick2'] = jd['L_Joystick2']
			self.data['L_Joystick3'] = jd['L_Joystick3']
			self.data['Batt_lvl'] = jd['Batt_lvl']
			

	def setStringData(self, sd):
		if (sd!=None):
			self.string_data = sd

	def setJsonData(self, jd):
		if (jd!=None):
			self.alldata = jd
			# self.point_btn = jd['point_btn']
			# self.Fire_btn = jd['Fire_btn']
			# self.gun1_btn = jd['gun1_btn']
			# self.gun2_btn = jd['gun2_btn']
			# self.gun3_btn = jd['gun3_btn']
			# self.gun4_btn = jd['gun4_btn']
			# self.brake_btn = jd['brake_btn']
			# self.drive_btn = jd['drive_btn']
			# self.PTZ_btn = jd['PTZ_btn']
			# self.mouse_btn = jd['mouse_btn']
			# self.silent_btn = jd['silent_btn']
			# self.mic_btn = jd['mic_btn']
			# self.mouseRL_btn = jd['mouseRL_btn']
			# self.speedUpDown_btn = jd['speedUpDown_btn']
			# self.openClose_btn = jd['openClose_btn']
			# self.gripRL_btn = jd['gripRL_btn']
			# self.handUpDown_btn = jd['handUpDown_btn']
			# self.armUpDown_btn = jd['armUpDown_btn']
			# self.armFB_btn = jd['armFB_btn']
			# self.armRotRL_btn = jd['armRotRL_btn']
			# self.R_Joystick1 = jd['R_Joystick1']
			# self.R_Joystick2 = jd['R_Joystick2']
			# self.L_Joystick1 = jd['L_Joystick1']
			# self.L_Joystick2 = jd['L_Joystick2']
			# self.L_Joystick3 = jd['L_Joystick3']
			# self.Batt_lvl = jd['Batt_lvl']
			self.data['point_btn'] = jd['point_btn']
			self.data['Fire_btn'] = jd['Fire_btn']
			self.data['gun1_btn'] = jd['gun1_btn']
			self.data['gun2_btn'] = jd['gun2_btn']
			self.data['gun3_btn'] = jd['gun3_btn']
			self.data['gun4_btn'] = jd['gun4_btn']
			self.data['brake_btn'] = jd['brake_btn']
			self.data['drive_btn'] = jd['drive_btn']
			self.data['PTZ_btn'] = jd['PTZ_btn']
			self.data['mouse_btn'] = jd['mouse_btn']
			self.data['silent_btn'] = jd['silent_btn']
			self.data['mic_btn'] = jd['mic_btn']
			self.data['mouseRL_btn'] = jd['mouseRL_btn']
			self.data['speedUpDown_btn'] = jd['speedUpDown_btn']
			self.data['openClose_btn'] = jd['openClose_btn']
			self.data['gripRL_btn'] = jd['gripRL_btn']
			self.data['handUpDown_btn'] = jd['handUpDown_btn']
			self.data['armUpDown_btn'] = jd['armUpDown_btn']
			self.data['armFB_btn'] = jd['armFB_btn']
			self.data['armRotRL_btn'] = jd['armRotRL_btn']
			self.data['R_Joystick1'] = jd['R_Joystick1']
			self.data['R_Joystick2'] = jd['R_Joystick2']
			self.data['L_Joystick1'] = jd['L_Joystick1']
			self.data['L_Joystick2'] = jd['L_Joystick2']
			self.data['L_Joystick3'] = jd['L_Joystick3']
			self.data['Batt_lvl'] = jd['Batt_lvl']

	def setConnected(self, connected):
		self.connected = connected
		if self.connected: self.data['rem_connected'] = 'connected'
		else:  self.data['rem_connected'] = 'disconnected'
		
	def getData(self):  
		return self.data

class Main():
    def __init__(self):
        try:    self.remote_serial = Serial("COM3", 115200)
        except: self.remote_serial = None
        try:
            self.tcp_socket = self.tcp_connect()
            self.tcp_socket.settimeout(3.0)
        except:
            self.tcp_socket = None
        self._remote = Remote(None, None, False)  ## Remote object
        self._robot  = Robot(False, None)         ## Robot object

    def main_(self, request):
            print("main_")
            return render(request, 'index.html')

    def main(self, request):
        print("mymain")
        # create tcp thread
        self.tcp_task = Thread(target=self.tcp_main, args=([]))
		### *** remote thread
        self.remote_task = Thread(target=self.remote_main, args=([]))
        
        self.tcp_task.daemon = True
        self.tcp_task.start()
        
        #self.remote_task.daemon = True
        #self.remote_task.start()
        return render(request,'index.html')

    def recievedata(self,request):
        # data= {'bat':80,'tem':70}
        reb = self._robot.getData()
        rem = self._remote.getData()
        reb.update(rem)
        if request.method == 'GET':
              return JsonResponse(reb)
        # # rem = self._remote.getData()
        # print(rem)
        # if request.is_ajax():
        #         return JsonResponse(rem,safe=False)

    def RebotData(self):
        return  self._robot.getData()
    def RemoteData(self):
        return self._remote.getData()

    def DATE(self):
        print(datetime.now().date())
        return datetime.now().date()
    
    def TIME(self):
        TIME = datetime.now().time()
        AMPM = "AM"
        h = TIME.hour
        m = TIME.minute
        s = TIME.second
        if (h > 12):
            h -= 12
            AMPM = "PM"
        elif (h == 12):
            AMPM = "PM"
            time_str = str(h) + ":" + str(m) + ":" + str(s) + " " + AMPM
            print(time_str)
            return time_str
    
    def DATETIME(self):
        DATE = datetime.now().date()
        TIME = datetime.now().time()
        AMPM = "AM"
        h = TIME.hour
        m = TIME.minute
        s = TIME.second
        if (h > 12):
            h -= 12
            AMPM = "PM"
        elif (h == 12):
            AMPM = "PM"
            time_str = str(h) + ":" + str(m) + ":" + str(s) + " " + AMPM
            print(DATE, " ", time_str)
            return DATE, " ", time_str
    
    def tcp_connect(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.11.130'
        port = 5555
        self.tcp_socket.connect((host, port))
        self.tcp_socket.send('1'.encode())  # send to start connection
        connect_msg = self.tcp_socket.recv(1024).decode('ascii')
        print(connect_msg)
        if (connect_msg == "RAAD"):
            print("I am connected :)")
            return self.tcp_socket
    
    def encodeStatusData(self, str_data):
        data = str_data.replace('=', '')
        json_data = json.loads(data)
        self._robot.setData(True, json_data)
        return self._robot
    
    def readData(self):
        msg = self.tcp_socket.recv(1024)
        self._robot = self.encodeStatusData(msg.decode('ascii'))
        return self._robot
    
    def getRemoteData(self):
        msg = '={\"point_btn\":\"-1\",\"Fire_btn\":\"-1\",\"gun1_btn\":\"-1\",\"gun2_btn\":\"-1\",\"gun3_btn\":\"-1\",\"gun4_btn\":\"-1\",\"brake_btn\":\"-1\",\"drive_btn\":\"-1\",\"PTZ_btn\":\"-1\",\"mouse_btn\":\"-1\",\"silent_btn\":\"-1\",\"mic_btn\":\"-1\",\"mouseRL_btn\":\"-1\",\"speedUpDown_btn\":\"-1\",\"openClose_btn\":\"-1\",\"gripRL_btn\":\"-1\",\"handUpDown_btn\":\"-1\",\"armUpDown_btn\":\"-1\",\"armFB_btn\":\"-1\",\"armRotRL_btn\":\"-1\",\"R_Joystick1\":\"-1\",\"R_Joystick2\":\"-1\",\"L_Joystick1\":\"-1\",\"L_Joystick2\":\"-1\",\"L_Joystick3\":\"-1\"}='
        try:
            if (self._remote != None): msg = self._remote.string_data
        except:
            pass
        try:
            if(self.tcp_socket!=None): self.tcp_socket.send(msg.encode())
        except:
            self.tcp_socket = self.tcp_connect()


    
    def tcp_main(self):
        while True:
            try:
                self.readData()  # read data from robot
                self._robot.setLastSeen(self.DATETIME())
				#self._robot.printAllData()
                print(self._robot.getData())
                self._robot.getData()  # send data to robot
            except Exception as e:
				## disconnected
                print(e)
                self._robot.setData(False, None)
				#self._robot.printAllData()
            
                try:
                    if(self.tcp_socket!=None): self.tcp_socket.close()
                    print("reconnect again")
                    self.tcp_connect()
                except Exception as e:
                    print(e)

	### *** decode the data receive from serial into remote object
    def decodeData(self, string_data, json_data):
		# global remote
        self._remote.setStringData(string_data)
        self._remote.setJsonData(json_data)
        self._remote.setConnected(True)
        print(self._remote.getData())

	### *** read data from Serial
    def readRemoteData(self):
		# global remote_serial, remote
        try:
            if (self.remote_serial.inWaiting()):
                d = self.remote_serial.readline()
                print(d)
                string_data = d.decode()
                json_data = json.loads(string_data)
				#print(json_data)
                self.decodeData(string_data, json_data)
            # else:
            #     print('else')
        except Exception as e:
            print("exception: ", e)
            try:
                if (self.remote_serial == None):
                    self.remote_serial = Serial("COM3", 115200)  ## Serial connection
                else:
                    if self.remote_serial.isOpen(): self.remote_serial.close()
                    self.remote_serial.open()
            except Exception as e:
                print("no port .. reconnect : ", e)
                self._remote.setConnected(False)
                print(self._remote.connected)

	### *** main function for remote code
    def remote_main(self):
        while True:
            self.readRemoteData()


class Main2(TemplateView):
    template_name = "index.html"
    def __init__(self):
        try:    self.remote_serial = Serial("COM3", 115200)
        except: self.remote_serial = None
        try:
            self.tcp_socket = self.tcp_connect()
            self.tcp_socket.settimeout(3.0)
        except:
            self.tcp_socket = None
        self._remote = Remote(None, None, False)  ## Remote object
        self._robot  = Robot(False, None)         ## Robot object

		# create tcp thread
        self.tcp_task = Thread(target=self.tcp_main, args=([]))
		### *** remote thread
        self.remote_task = Thread(target=self.remote_main, args=([]))

		# tcp_task.daemon = True
        self.tcp_task.start()

		# remote_task.daemon = True
        self.remote_task.start()


    def RebotData(self):
        return  self._robot.getData()
    def RemoteData(self):
        return self._remote.getData()

    def DATE(self):
        print(datetime.now().date())
        return datetime.now().date()
    
    def TIME(self):
        TIME = datetime.now().time()
        AMPM = "AM"
        h = TIME.hour
        m = TIME.minute
        s = TIME.second
        if (h > 12):
            h -= 12
            AMPM = "PM"
        elif (h == 12):
            AMPM = "PM"
            time_str = str(h) + ":" + str(m) + ":" + str(s) + " " + AMPM
            print(time_str)
            return time_str
    
    def DATETIME(self):
        DATE = datetime.now().date()
        TIME = datetime.now().time()
        AMPM = "AM"
        h = TIME.hour
        m = TIME.minute
        s = TIME.second
        if (h > 12):
            h -= 12
            AMPM = "PM"
        elif (h == 12):
            AMPM = "PM"
            time_str = str(h) + ":" + str(m) + ":" + str(s) + " " + AMPM
            print(DATE, " ", time_str)
            return DATE, " ", time_str
    
    def tcp_connect(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.11.102'
        port = 5555
        self.tcp_socket.connect((host, port))
        self.tcp_socket.send('1'.encode())  # send to start connection
        connect_msg = self.tcp_socket.recv(1024).decode('ascii')
        print(connect_msg)
        if (connect_msg == "RAAD"):
            print("I am connected :)")
            return self.tcp_socket
    
    def encodeStatusData(self, str_data):
        data = str_data.replace('=', '')
        json_data = json.loads(data)
        self._robot.setData(True, json_data)
        return self._robot
    
    def readData(self):
        msg = self.tcp_socket.recv(1024)
        self._robot = self.encodeStatusData(msg.decode('ascii'))
        return self._robot
    
    def getRemoteData(self):
        msg = '={\"point_btn\":\"-1\",\"Fire_btn\":\"-1\",\"gun1_btn\":\"-1\",\"gun2_btn\":\"-1\",\"gun3_btn\":\"-1\",\"gun4_btn\":\"-1\",\"brake_btn\":\"-1\",\"drive_btn\":\"-1\",\"PTZ_btn\":\"-1\",\"mouse_btn\":\"-1\",\"silent_btn\":\"-1\",\"mic_btn\":\"-1\",\"mouseRL_btn\":\"-1\",\"speedUpDown_btn\":\"-1\",\"openClose_btn\":\"-1\",\"gripRL_btn\":\"-1\",\"handUpDown_btn\":\"-1\",\"armUpDown_btn\":\"-1\",\"armFB_btn\":\"-1\",\"armRotRL_btn\":\"-1\",\"R_Joystick1\":\"-1\",\"R_Joystick2\":\"-1\",\"L_Joystick1\":\"-1\",\"L_Joystick2\":\"-1\",\"L_Joystick3\":\"-1\"}='
        try:
            if (self._remote != None): msg = self._remote.string_data
        except:
            pass
        try:
            if(self.tcp_socket!=None): self.tcp_socket.send(msg.encode())
        except:
            self.tcp_socket = self.tcp_connect()


    
    def tcp_main(self):
        while True:
            try:
                self.readData()  # read data from robot
                self._robot.setLastSeen(self.DATETIME())
				#self._robot.printAllData()
                print(self._robot.getData())
                self._robot.getData()  # send data to robot
            except Exception as e:
				## disconnected
                print(e)
                self._robot.setData(False, None)
				#self._robot.printAllData()
                self.tcp_socket.close()
                print("reconnect again")
                try:
                    self.tcp_connect()
                except Exception as e:
                    print(e)

	### *** decode the data receive from serial into remote object
    def decodeData(self, string_data, json_data):
		# global remote
        self._remote.setStringData(string_data)
        self._remote.setJsonData(json_data)
        self._remote.setConnected(True)
        print(self._remote.getData())

	### *** read data from Serial
    def readRemoteData(self):
		# global remote_serial, remote
        try:
            if (self.remote_serial.inWaiting()):
                d = self.remote_serial.readline()
				#print(d)
                string_data = d.decode()
                json_data = json.loads(string_data)
				#print(json_data)
                self.decodeData(string_data, json_data)
        except Exception as e:
            print("exception: ", e)
            try:
                if (self.remote_serial == None):
                    self.remote_serial = Serial("COM3", 115200)  ## Serial connection
                else:
                    if self.remote_serial.isOpen(): self.remote_serial.close()
                    self.remote_serial.open()
            except Exception as e:
                print("no port .. reconnect : ", e)
                self._remote.setConnected(False)
                print(self._remote.connected)

	### *** main function for remote code
    def remote_main(self):
        while True:
            self.readRemoteData()
