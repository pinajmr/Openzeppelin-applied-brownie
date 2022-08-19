from scripts.deploy_create import deploy_contract
from brownie import (PinaTokenERC20, exceptions)
from scripts.helpful_scripts import get_account
import pytest

def test_name_symbol():
    # Arrange
    contract_reto = deploy_contract(PinaTokenERC20)
    # Act
    name = contract_reto.name()
    symbol = contract_reto.symbol()
    # Assert
    assert name == "Pina Token"
    assert symbol == "PINA"

def test_total_supply():
    # Arrange
    contract_reto = deploy_contract(PinaTokenERC20)
    # Act
    total_supply = contract_reto.totalSupply()
    # Assert
    assert total_supply == 100 * 10 ** 18


def test_mint():
    # Arrange
    contract_reto = deploy_contract(PinaTokenERC20)
    account_not_admin = get_account(1)
    # Act
    tx = contract_reto.mint(account_not_admin ,1)
    tx.wait(1)
    # Assert
    assert contract_reto.balanceOf(account_not_admin) == 1
    with pytest.raises(exceptions.VirtualMachineError):
        contract_reto.mint(account_not_admin,1,{"from":account_not_admin})