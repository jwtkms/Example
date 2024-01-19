# import os
# import time
# folder = '//KnowLedge77/Work - Dsystems/ПРОЕКТЫ/Система сейсмомониторинга СКИФ/Data/SKIF_Data_05.12.2023/Curiosity/Y2023/M09/D20/H22'
# spl = folder.split('/')
# # print(spl)

# # print(spl[-1])
# # print(spl[-2])
# # print(spl[-3])


# class holder:
# 	def __init__(self):
# 		self.currFolder = ''
# 		self.folderNum = ''
# 		self.path = ''

# 	def checkNextFolder(self):
# 		intFolder = int(self.folderNum[1:])
# 		intFolder += 1
# 		strFolder = ''
# 		if intFolder < 10:
# 			strFolder = 'H0' + str(intFolder)
# 		else:
# 			strFolder = 'H' + str(intFolder)
		
# 		if intFolder > 23:
# 			intFolder = 0
# 			spl = self.path.split('/')
# 			strFolder = 'H00'
# 			month = int(spl[-3][1:])
# 			day = int(spl[-2][1:])
# 			year = int(spl[-4][1:])
			
# 			if day == 30:
# 				if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
# 					day += 1
# 				else:
# 					day = 1
# 					month += 1
# 			else:
# 				if day == 31:
# 					day = 1
# 					if month != 12:
# 						month += 1
# 					else:
# 						month = 1
# 						year += 1
# 			day += 1
# 			strDay = ''
# 			strMonth = ''
# 			strYear = 'Y' + str(year)

# 			if day < 10:
# 				strDay = 'D0' + str(day)
# 			else:
# 				strDay = 'D' + str(day)

# 			if month < 10:
# 				strMonth = 'M0' + str(month)
# 			else:
# 				strMonth = 'M' + str(month)

# 			# self.path.replace(spl[-1], hour)
# 			self.path = self.path.replace(spl[-2], strDay)
# 			self.path = self.path.replace(spl[-3], strMonth)
# 			self.path = self.path.replace(spl[-4], strYear)
# 			print(self.path)

# 		print(intFolder, strFolder)
# 		if os.path.isfile(H.path + H.folderNum + '/CH0.DAT'):
# 			self.folderNum = strFolder
# 			print(os.path.isfile(H.path + H.folderNum + '/CH0.DAT'))
# 		else:
# 			# print('XYETA')
# 			return 0
			

# H = holder()


# H.currFolder = folder
# H.folderNum = H.currFolder[-3:]
# H.path = H.currFolder[0:len(H.currFolder)-3]
	
# c = True

# while c:
# 	H.checkNextFolder()
# 	# time.sleep(1)
	
import subprocess

try:
    subprocess.check_output('nvidia-smi')
    print('Nvidia GPU detected!')
except Exception: # this command not being found can raise quite a few different errors depending on the configuration
    print('No Nvidia GPU in system!')