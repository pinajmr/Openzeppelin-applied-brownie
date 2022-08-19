from brownie import Reto2Token, exceptions
from scripts.deploy_create import deploy_contract
from scripts.helpful_scripts import get_account
import pytest

def test_pause_and_unpause():
    # Arrange
    account_admin = get_account(0)
    account_not_owner = get_account(1)
    contract_reto = deploy_contract(Reto2Token)
    # Act
    #Assert 1
    assert contract_reto.paused() == False
    tx = contract_reto.pause({"from":account_admin})
    tx.wait(1)
    # Assert 2
    assert contract_reto.paused() == True 

    # Act 2
    tx2 = contract_reto.unpause({"from":account_admin})
    tx2.wait(1)
    # Assert 3
    assert contract_reto.paused() == False
    with pytest.raises(exceptions.VirtualMachineError):
        contract_reto.pause({"from":account_not_owner})


