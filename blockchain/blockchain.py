from block import Block

class Blockchain():
    def __init__(self):
        self.Block = []
        self.setGenesisBlock()
    
    
    def setGenesisBlock(self):
        data = "Genesis\t"
        prevHash='0'*64
        genesisBlock = Block(data,prevHash)
        self.Block.append(genesisBlock)

    def getLastHash(self):
        lastBlock= self.Block[-1]
        lastHash=lastBlock.hash
        return lastHash
    
    def addNewBlock(self,data):
        prevHash= self.getLastHash()
        newBlock=Block(data,prevHash)
        self.Block.append(newBlock)
    
    def getBlocks(self):
        return self.Block
        