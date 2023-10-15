def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]
    # res = []
    # for i in range(4):
    #     res_comp = [ord(x) for x in lst[i]]
    #     res.append(res_comp)
    # return res

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    text = ''
    for i in range(len(matrix)):
        for j in range(4):
            text += chr(matrix[i][j])
    return text

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

text = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'

mtr = bytes2matrix(text)

word = list(mtr[-1])

word.append(word.pop(0))

print(len(text))


