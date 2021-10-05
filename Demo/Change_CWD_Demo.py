import os

newSearchPath = "C:\\Users\\adrian\\Documents\\GLS\\Sewsan\\Python\\Test"

#os.chdir(newSearchPath)

# the chdir can be modified with an append to the search directory

if not newSearchPath in sys.path: 
	sys.path.append("C:\\Users\\adrian\\Documents\\GLS\\Sewsan\\Python\\Test")

print(str(len(sys.path)))
print(os.getcwd())

#Ensure that temp.py and temp2.py ar in the above mentioned directory


from temp import TestFunction
from temp2 import TestFunction2

TestFunction()   
TestFunction2()

#temp.py
#
#def TestFunction():
#	print("Hello world!")

#temp2.py1111111
#
#def TestFunction2():
#	print("Hello world Again")