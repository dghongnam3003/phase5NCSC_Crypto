state = [[209, 79, 20, 106], [164, 43, 79, 182], [161, 196, 8, 66], [41, 143, 18, 221]]

round_key = [[9, 99, 11, 19], [119, 40, 176, 155], [111, 31, 173, 174], [46, 86, 94, 232]]


def add_round_key(s, k):
    res = []
    for i in range(4):
        for j in range(4):
            res.append(s[i][j]^k[i][j])
    return [res[4*i:4*(i+1)] for i in range(len(res)//4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    text = ''
    for i in range(len(matrix)):
        for j in range(4):
            text += chr(matrix[i][j])
    return text


print(add_round_key(state, round_key))
print(matrix2bytes(add_round_key(state, round_key)))

