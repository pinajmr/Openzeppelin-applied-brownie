from brownie import (
    accounts,
    network,
    config
)

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]
FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork","mainnet-fork-dev"]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    elif id:
        return accounts.load(id)
    if( network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])