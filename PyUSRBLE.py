from bluepy.btle import *

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

class uart:
	def __init__(self, deviceAddr):
		self.dev = Peripheral(deviceAddr)

	def read(self,timeout=2):
		resp = self.dev._getResp(['ntfy','ind'], timeout=timeout)
		return resp
		
	def write(self,val,hnd=0x0011):
		try:
			self.dev.writeCharacteristic(hnd,val)
			return True
		except:
			return False
	def close(self):
		self.dev.disconnect()

def scanBLE(timeout=5):
	scanner = Scanner().withDelegate(ScanDelegate())
	print("Scanning...")
	devices = scanner.scan(timeout)
	for dev in devices:
		#print("Device %s, RSSI=%d dB" % (dev.addr, dev.rssi))
		for chara in dev.getScanData():
			if chara[2].startswith('USR-BLE'):
				print("Device %s(RSSI=%d db) is %s" % (dev.addr, dev.rssi, chara[2]))
	print("-- Scan done --")	
			
if __name__ == '__main__':
	scanBLE()

