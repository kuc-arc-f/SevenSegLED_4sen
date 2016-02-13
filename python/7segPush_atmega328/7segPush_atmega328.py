import threading
import serial
import time
import sys
import traceback
import datetime

mDevice = "/dev/ttyAMA0"

mOK_CODE=1
mNG_CODE=0

ER_STAT_000="000"
ER_STAT_101="101"
ER_STAT_102="102"
ER_STAT_103="103"

sHEAD="res_dat="

if __name__ == "__main__":
    ret_base= "000000000000000000000000"
    ser=serial.Serial(mDevice ,9600)
    from datetime import datetime
    while True:
    	sTime = datetime.now().strftime("%H%M")
    	print("time=" +sTime)
    	#sSend="tmp=00"+ sTime
    	ser.write("tmp=00"  + sTime)
    	time.sleep(5.0)


