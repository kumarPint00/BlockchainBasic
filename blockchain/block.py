from hashlib import sha256
from datetime import datetime

class Block():
    def __init__(self, data, previousBlockHash):
        self.timestamp = datetime.utcnow()
        self.data = data
        self.previousBlockHash = previousBlockHash
        self.calculateValidHash()

    def IsHashValid(self, hash):
        return (hash.startswith('0'*3))
    
    def calculateValidHash(self):
        hash=''
        nonce=0

        while (not self.IsHashValid(hash)):
            temp=self.to_string()+str(nonce)
            hash= sha256(temp.encode()).hexdigest()
            nonce+=1
        self.hash=hash
    def to_string(self):
        return "{0}\t{1}\t{2}".format(self.data, self.timestamp, self.previousBlockHash)