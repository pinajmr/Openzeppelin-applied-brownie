from scripts.helpful_scripts import get_account
from brownie import (Owner, Roles, network, config)

def deploy_owner():
    account = get_account()
    owner = Owner.deploy({'from': account},
        publish_source=config["networks"][network.show_active()].get("verify",False))
    print("Deploying ...")
    print(f"Owner deployed at {owner.address}")
    return owner

def deploy_roles():
    account = get_account()
    roles = Roles.deploy({'from': account},
        publish_source=config["networks"][network.show_active()].get("verify",False))
    print("Deploying ...")
    print(f"Owner deployed at {roles.address}")
    return roles


def main():
    deploy_owner()
    deploy_roles()