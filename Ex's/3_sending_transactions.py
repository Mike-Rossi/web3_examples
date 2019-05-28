from web3 import Web3


ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())
print(web3.eth.blockNumber)

account_1 = "0xc93E1E4F77Eb503BDFA75a2E4dE24840E8e8089E"
account_2 = "0x103568c836F8F4c3272D1fB2b99Afc8e507F9503"

private_key = "1b928ed134a04f5f0b2b3308b621f43033702b891973ac18255886d6f79686cf" #signing transactions / authorizing transactions

# get the nonce

nonce = web3.eth.getTransactionCount(account_1)

# build transaction
tx = {
	'nonce': nonce,		#prevents you from sending transaction twice on etherium 
	'to': account_2,
	'value': web3.toWei(1, 'ether'),
	'gas': 200000, 		#units of gas, the limit, not in etherium, think of gallons of gas
	'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

# send transaction

# get transaction hash

