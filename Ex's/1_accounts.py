from web3 import Web3

#Fill in infura API key here

infura_url = "https://mainnet.infura.io/v3/da966af98520486b9cda846d5d354ef9"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)


#Fill in your (the guy's) account here

balance = web3.eth.getBalance("0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9")

print(web3.fromWei(balance, "ether"))