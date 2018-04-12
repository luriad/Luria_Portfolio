# Muon Data Collection
# Programmer: David Luria

import os
import usbtmc
import time
instr = usbtmc.Instrument(0x1ab1,0x04b1)
fileNum = 1
#set up instrument
instr.write(":WAV:SOUR CHAN1")
instr.write(":WAV:MODE NORM")
#Start cosmic ray recording
instr.write("FUNC:WRM REC")
instr.write("FUNC:WREC:OPER REC")
print("Now collecting data...")
n = 0
while instr.ask(":FUNC:WREC:OPER?") == u'REC':
	time.sleep(600)
	n += 10
	print(str(n) + " minutes passed")
print("Data collection finished")
#Make the first sequential directory "Run #" that we don't have
while os.path.exists("./Run " + str(fileNum)):
	fileNum += 1
	if not os.path.exists("./Run " + str(fileNum)):
		os.mkdir("./Run " + str(fileNum))
		fileNum += 1
#cd into that directory
os.chdir("./Run " + str(fileNum))
#Select particles that look like muons
instr.write("FUNC:WRM ANAL")
instr.write("FUNC:WAN:STAR")
print("Analyzing data")
time.sleep(60)
totalFrames = int(instr.ask(":FUNC:WAN:EFC?"))
instr.write(":FUNC:WAN:SET:SST:")
print("Saving muons")
#Loop to collect and save all muon frames
for i in range(totalFrames):
	instr.write(":WAV:FORM ASC")
	data = instr.ask(":WAV:DATA?")
	file = open("Muon_10_4_17_" + str(i+1),"w")
	file.write(data)
	file.close()
	time.sleep(0.1)
	instr.write(":FUNC:WAN:NEXT")
os.chdir("../")
print("Next data set...")
