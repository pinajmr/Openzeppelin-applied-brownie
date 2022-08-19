from scripts.helpful_scripts import get_account
from brownie import (Owner, Roles, network, config)

def deploy_contract(contract):
    account = get_account()
    contract_created = contract.deploy({'from': account},
        publish_source=config["networks"][network.show_active()].get("verify",False))
    print("Deploying ...")
    print(f"{contract} deployed at {contract_created.address}")
    return contract_created

def main():
    deploy_contract(Owner)
    deploy_contract(Roles)
    