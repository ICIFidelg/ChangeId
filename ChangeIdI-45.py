import minimalmodbus
import time
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("port", type=str, help="usb port where target is tied to")
parser.add_argument("old_id", type=str, help="the actual target's Id")
parser.add_argument("new_id",type=str, help="the new id it will have")
args = parser.parse_args()

port = args.port
i = args.old_id
new_i= args.new_id

try:
	i45 = minimalmodbus.Instrument(port,i,mode='rtu')
	i45.serial.baudrate = 9600
	i45.serial.timeout=3
	i45.debug=True
	InitAdd=1001
	i45.write_register(InitAdd,new_i, number_of_decimals=0, functioncode=16, signed=False)
except Exception as e:
	print(e) 

