import hashlib


def hashgen(data):
    result = hashlib.sha256(data.encode())
    # converts to hexadecimal and return
    return result.hexdigest()


class Block:
    def __init__(self,data,hash,prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash


class BlockChain:
    def __init__(self):
        hashprev = hashgen('oldHash?')
        hashStart = hashgen('newHash')

        arr = Block('newData', hashStart, hashprev)
        self.chain = [arr]

    def addBlock(self, data):
        # -1 means last data added, stores Start hash
        prev_hash = self.chain[-1].hash
        new_hash = hashgen(prev_hash + data)
        blo = Block(data, new_hash, prev_hash)
        self.chain.append(blo)


fast = BlockChain()
fast.addBlock('p')
fast.addBlock('a')
fast.addBlock('n')


for blo in fast.chain:
    print(blo.__dict__)

