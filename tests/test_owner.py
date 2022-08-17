from scripts.helpful_scripts import (
    get_account,
)
from scripts.deploy_owner import deploy_owner
from brownie import (exceptions)
import pytest

# Every one can call forAll
def test_forAll():
    # Arrange
    owner_contract = deploy_owner()
    account = get_account(3)
    # Act
    tx = owner_contract.forAll({"from": account})
    tx.wait(1)
    # Assert
    assert owner_contract.key() == 1

#This test is fail becasuse is call for other than not owener
def test_justOwner():
    # Arrange
    owner_contract = deploy_owner()
    account = get_account(index=1)
    # Act
    # Assert 
    # with brownie.reverts():
    #     result = owner_contract.justOwner({"from": account})
    with pytest.raises(exceptions.VirtualMachineError):
        owner_contract.justOwner({"from": account})
    

# This test is passed becasuse is call is the owner
def test_justOwnerTrue():
    # Arrange
    owner_contract = deploy_owner()
    account = get_account()
    # Act
    tx = owner_contract.justOwner({"from": account})
    tx.wait(1)
    # Assert
    assert owner_contract.key() == 2
