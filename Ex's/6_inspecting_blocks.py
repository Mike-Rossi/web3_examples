from web3 import Web3

# Main Focus: Being able to read info from the block chain and display it somewhere

# Fill in infura API key here

infura_url = "https://mainnet.infura.io/v3/da966af98520486b9cda846d5d354ef9"
web3 = Web3(Web3.HTTPProvider(infura_url))

# fetches most recent blocknumber
print(web3.eth.blockNumber)

latest = web3.eth.blockNumber
print(latest)

print(web3.eth.getBlock(latest))  # gets all info about latest block

for i in range(0, 10):
    print(web3.eth.getBlock(latest - i))  # info about latest 10 blocks

# gets transaction from specific block
hash = "0xc5252c3647c58c5cc636ec9afa40b656c8e225b91dcecab43d0204120f4c021f"
# the 2 refers to the transaction we want to see
print(web3.eth.getTransactionByBlock(hash, 2))
