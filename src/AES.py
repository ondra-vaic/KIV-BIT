from LookUps import*


def stringToBytes(keyString):
    return bytearray(keyString, 'utf-8')


def rot(chars, shift):

    charsCopy = chars.copy()

    for i in range(0, len(chars)):
        chars[i] = charsCopy[(shift + i) % 4]

    return chars


def lookUp(chars, table):
    for i in range(0, len(chars)):
        chars[i] = table[chars[i]]

    return chars


def subBytes(chars):
    return lookUp(chars, subBytesLU)


def invSubBytes(chars):
    return lookUp(chars, invSubBytesLU)


def rcon(chars, i):
    chars[0] ^= rconLU[i]
    return chars


def xor(a, b):
    for i in range(0, len(a)):
        a[i] ^= b[i]

    return a


def createSubKey(key, i):

    lastColumnTransformed = rcon(subBytes(rot(key[-4:], 1)), i)
    firstCol = key[:4]

    newKey = xor(firstCol, lastColumnTransformed)

    for i in range(1, 4):
        prevCol = newKey[((i - 1) * 4):(i * 4)]
        currentCol = key[(i * 4):((i + 1) * 4)]
        newKey.extend(xor(prevCol, currentCol))

    return newKey


def createKeys(keyString):
    keys = [stringToBytes(keyString)]

    for i in range(0, 10):
        keys.append(createSubKey(keys[i], i + 1))

    return keys


def shiftRows(state):

    stateCopy = state.copy()

    for i in range(0, 4):
        for j in range(0, 4):
            state[i + j * 4] = stateCopy[i + ((j + i) % 4) * 4]

    return state


def galoiMultiplication(a, b):
    if(b == 1):
        return a
    else:
        return galoisLU[b][a]


def mixColumns(state):
    return gMultiplication(state, mixColumnsMatrix)


def invMixColumns(state):
    return gMultiplication(state, invMixColumnsMatrix)


def gMultiplication(state, matrix):

    for i in range(0, 4):
        stateColumn = state[i * 4:(i + 1) * 4]
        state[i * 4:(i + 1) * 4] = [0, 0, 0, 0]
        for j in range(0, 4):
            for k in range(0, 4):
                state[i * 4 + j] ^= galoiMultiplication(stateColumn[k], matrix[j][k])

    return state


def invShiftRows(state):
    stateCopy = state.copy()

    for i in range(0, 4):
        for j in range(0, 4):
            state[i + j * 4] = stateCopy[i + ((j - i) % 4) * 4]

    return state


def encryptBlock(block, keys):
    state = xor(block, keys[0])  # first state

    for i in range(1, 10):
        state = xor(mixColumns(shiftRows(subBytes(state))), keys[i])

    state = xor(shiftRows(subBytes(state)), keys[10])

    return state


def decryptBlock(message, keys):
    state = message.copy()
    state = xor(state, keys[10])

    for i in reversed(range(1, 10)):
        state = invMixColumns(xor(invSubBytes(invShiftRows(state)), keys[i]))

    state = xor(invSubBytes(invShiftRows(state)), keys[0])

    return state


def encryptMessage(message, key):

    encryptedMessage = bytearray()
    keys = createKeys(key)

    numBytes = len(message)
    incompleteBlockLength = numBytes % 16

    message.extend(bytearray(16 - incompleteBlockLength))
    numBlocks = len(message) // 16

    for i in range(0, numBlocks):
        encryptedMessage.extend(
            encryptBlock(message[i * 16:(i + 1) * 16], keys)
        )

    return encryptedMessage


def decryptMessage(message, key):
    decryptedMessage = bytearray()
    keys = createKeys(key)

    numBlocks = len(message) // 16

    for i in range(0, numBlocks):
        decryptedMessage.extend(decryptBlock(message[i * 16:(i + 1) * 16], keys))

    return decryptedMessage
