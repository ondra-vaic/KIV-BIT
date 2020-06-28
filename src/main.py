import AES
from tests import*
from InputOutput import*


def encrypt():
    inFileName = inputFileName("Please enter name of the file to encrypt: ")
    key = inputKey()
    outFileName = outputFileName()

    encryptedMessage = AES.encryptMessage(getMessage(inFileName), key)
    outPutMessage(outFileName, encryptedMessage)


def decrypt():
    inFileName = inputFileName("Please enter name of the file to decrypt: ")
    key = inputKey()
    outFileName = outputFileName()

    decryptedMessage = AES.decryptMessage(getMessage(inFileName), key)
    outPutMessage(outFileName, decryptedMessage)


def main():

    if choice("Encrypt [E] or Decrypt [D]?", "E", "D"):
        encrypt()
    else:
        decrypt()


main()

#testFile("m.txt", "josefvencasladek")
#testFile("Shea.jpg", "josefvencasladek")


