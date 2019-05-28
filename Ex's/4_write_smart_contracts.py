import json
from web3 import Web3

#Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org


#Set a default account to sign transactions - this account is unlocked with Ganache
web3.eth.defaultAccount = web3.eth.accounts[0]

#Greeer contract ABI
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

#Greeter contract address - convert to checksum address
address = web3.toChecksumAddress("0xe1825610403521781b2164ccca83fba2d684e54b")

#Iniialize contract
contract = web3.eth.contract(address=address, abi=abi)

#Read the default greeting
print(contract.functions.greet().call())

#Set a new greeting
tx_hash = contract.functions.setGreeting('BYE').transact()

print(tx_hash)		#test for a transaction has to see if its working

#Wait for transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)		#stops excecuting code until we get a receipt

#Display the new greeting value
print('Updated greeting: {}'.format(
	contract.functions.greet().call()
))