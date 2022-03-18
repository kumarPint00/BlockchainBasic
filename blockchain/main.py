from blockchain import Blockchain

blockchain = Blockchain()

blockchain.addNewBlock("first block")
blockchain.addNewBlock("second block")
blockchain.addNewBlock("third block")
blockchain.addNewBlock("fourth block")
blockchain.addNewBlock("fifth block")
blockchain.addNewBlock("six block")
blockchain.addNewBlock("seven block")
blockchain.addNewBlock("eighth block")
blockchain.addNewBlock("nineth block")
blockchain.addNewBlock("tenth block")


for block in blockchain.getBlocks():
    print()
    print('\t'+block.to_string())
print()

