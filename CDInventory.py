#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Muhammad Mannan 2021-Aug-04 Modified File
#------------------------------------------#

# Declare variabls
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
dicRow={}
# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        print()
        # TODO Add the functionality of loading existing data
        print('ID, CD Title, Artist')
        objFile=open(strFileName,'r')
        for row in objFile:
            lstRow = row.strip().split(',') #Here we import the data into memory in the way we want
            dicRow = {'Id':int(lstRow[0]), 'Title': lstRow[1], 'Artist':lstRow[2]} #Here we add our imported data into our 2d table
            lstTbl.append(dicRow.values())
            print(lstRow)
        print('Data loaded from inventory file')
        objFile.close()
        print()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        print()
        strID = input('Enter an ID: ') #Here we ask for each entry's information
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        print()
        intID = int(strID)
        dicRow={'Id':intID, 'Title': strTitle, 'Artist':strArtist} #Here we store each entry as a dictionary
        lstTbl.append(dicRow.values()) #Here we add our manually entered data into our 2d table
    elif strChoice == 'i':
        print()
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        entrynumber=0
        for row in lstTbl:
            entrynumber+=1
            print('Entry ' + str(entrynumber) + ': ') #Here we print out each entry in memory
            print(*row, sep = ', ')
        if len(lstTbl)==0:
            print()
            print('No current data to display \nEither (a) Add CD or (l) Load data from inventory file') #If there is nothing in memory we tell the user
        print()
    elif strChoice == 'd':
        print()
        # TODO Add functionality of deleting an entry
        userinput=(input('Which entry would you like to remove: ')) #Here we ask the user which entry they would like to delete from memory
        userinput=int(userinput)-1
        del lstTbl[userinput]
        print('\nInventory entries have been updated \nEntry ' + str((userinput+1)) + ' has been updated')
        print()
        pass
    elif strChoice == 's':
        print()
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row:
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        userchoice=input('Would you like to keep editing your current data in memory? \n(If no then data loaded into memory will be cleared): ') #Here we ask the user if they plan on editing the data in memory again or weather or not they want to stop editing what is in memory and instead edit what they have saved so we do not create duplicate loaded entries
        if (userchoice.lower() == 'yes'):
            pass
        elif (userchoice.lower() == 'no'):
            print('Data will now be cleared from memory')
            lstTbl = []
        print()
    else:
        print('Please choose either l, a, i, d, s or x!')   

