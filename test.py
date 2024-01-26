def get_hash(key):
    return sum([ord(j) * ((i + (i-1)) | 3) for i, j in enumerate(key)]) if sum([ord(j) * ((i + (i-1)) | 3) for i, j in enumerate(key)]) > 0 else sum([ord(j) * ((i + (i-1)) | 3) for i, j in enumerate(key)]) * -1
x = ''
for i in range(1000):
    x += f'i({i}) = {get_hash(f'{i}')}\n'

print(x)