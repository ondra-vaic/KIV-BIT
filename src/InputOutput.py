import os.path
import binascii


def printState(state):

    for i in range(0, 4):
        for j in range(0, 4):
            print('|', end=' ')
            print(hex(state[j * 4 + i]), end=" ")
        print("|\n", end="-----------------------------\n")

    print("**************")


def choice(message, Yes="Y", No="N"):
    yn = input(message + " [" + Yes + "/" + No + "] ").upper()

    while not (yn == Yes or yn == No):
        yn = input(message + " [" + Yes + "/" + No + "] ").upper()

    if yn == Yes:
        return True

    if yn == No:
        return False


def outPutMessage(outFileName, encryptedMessage):

    if choice("Output in Hex [H] or as characters [C]?", "H", "C"):
        writeMessage(outFileName, encryptedMessage, True)
        printMessage(encryptedMessage, 256, True)
    else:
        writeMessage(outFileName, encryptedMessage)
        printMessage(encryptedMessage, 256)


def printMessage(list, maximum=-1, outHex=False):

    maximum = len(list) if maximum == -1 or maximum > len(list) else maximum

    for i in range(0, maximum):
        if i % 16 == 0:
            print()

        c = hex(list[i]) if outHex else chr(list[i])
        print(c, end=' ')

    print()


def getMessage(fileName):
    with open(fileName, 'rb') as file:
        message = file.read()
        return bytearray(message)


def writeMessage(fileName, message, outHex=False):
    with open(fileName, 'wb') as file:
        if(outHex):
            file.write(binascii.hexlify(message))
        else:
            file.write(message)


def inputKey():
    key = input("Please enter 16 character password: ")
    while not len(key) == 16:
        key = input("Password length is not 16 please try again: ")

    return key


def inputFileName(prompt):
    inFileName = input(prompt)
    while not os.path.isfile(inFileName):
        inFileName = input("File name invalid please try again: ")

    return inFileName


def outputFileName():
    return input("Please enter name of the output file: ")


