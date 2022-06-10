#import qrcode is the module that we use to import images of qrcode after we assign them value 
#pip install qrcode is required to use this code
#
#
import qrcode

def mainMenu():
        navigation = ["1. Create A label","2. Print Label","3. Exit Program"]
        for i in range(0,3):
                print(navigation[i])
def menuSelection():
        askUser = str(input("Please Select Category From Menu: "))
        return askUser
def selection(ms,labelID,pngFileName):
        if ms == str(1):
                print('\n')
                #print("label creating is now working")
                labelSerialNumber = str(input("Enter Employee ID Here: "))
                labelID.append(str(labelSerialNumber))
                employeeName = str(input("Enter Employee Name Here: "))
                pngFileName.append(employeeName)
                print(pngFileName)
                print(labelID)
                print("Badge is now ready for printing.")
                print('\n')
        elif ms == str(2):
                #print("label printing menu is now working")
                x = 0
                print('\n')
                while(x < len(labelID)):
                        qr = qrcode.make(labelID[x])
                        qr.save(pngFileName[x])
                        x+=1     
        elif ms == str(3):
                print("Program has terminated.")
                exit()
#-----------------------------------main------------------------------------------
labelID = []
pngFileName = []
while(True):
        mainMenu()
        ms = menuSelection()
        selection(ms,labelID,pngFileName)
        #print(labelID)



        












		










