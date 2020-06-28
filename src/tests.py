from AES import*
from LookUps import*
from InputOutput import*


def test1(fileName):
    message = getMessage(fileName)
    printState(message)

    newMessage = invShiftRows(shiftRows(message))
    printState(newMessage)


def test2(fileName):
    message = getMessage(fileName)
    printState(message)

    newMessage = invMixColumns(mixColumnsMatrix(message))
    printState(newMessage)


def test3(fileName):
    message = getMessage(fileName)
    printState(message)

    newMessage = invSubBytes(subBytes(message))
    printState(newMessage)


def testFile(fileName, key):
    messageInBytes = getMessage(fileName)

    encryptedMessage = encryptMessage(messageInBytes, key)
    decryptedMessage = decryptMessage(encryptedMessage, key)
    writeMessage("enc_" + fileName, encryptedMessage)
    writeMessage("dec_" + fileName, decryptedMessage)

    return

