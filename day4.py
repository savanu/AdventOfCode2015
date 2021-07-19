import hashlib

input = 'ckczppom'

def calc(numZeros):
    base = hashlib.md5()
    base.update(input.encode())

    num = 1
    done = False

    while not done:
        h = base.copy()
        h.update(str(num).encode())

        hash = h.hexdigest()

        if hash[0:numZeros] == ('0' * numZeros):
            done = True
        
        num += 1
    
    print(num - 1)

calc(5)
calc(6)