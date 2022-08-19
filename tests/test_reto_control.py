


from scripts.deploy_create import deploy_contract
from brownie import (Reto1Control, exceptions)
from scripts.helpful_scripts import get_account
import pytest


def test_assign_role():
    # Arrange
    contract_reto = deploy_contract(Reto1Control)
    account_writer = get_account(1)
    account_admin = get_account(0)
    admin = contract_reto.ROL_ADMIN()
    # Act
    tx = contract_reto.addRoleWriter(account_writer,{"from":account_admin})
    tx.wait(1)
    writer = contract_reto.ROL_WRITER()
    # Assert
    assert contract_reto.hasRole(admin,account_admin) == True
    assert contract_reto.hasRole(writer,account_writer) == True

def test_only_writter():
    # Arrange
    contract_reto = deploy_contract(Reto1Control)
    account_writer = get_account(1)
    account_admin = get_account(0)
    # Act
    tx = contract_reto.addRoleWriter(account_writer,{"from":account_admin})
    tx.wait(1)
    tx2 = contract_reto.store(10,{"from":account_writer})
    tx2.wait(1)
    # Assert
    assert contract_reto.retrieve() == 10


def test_deleteRole_Writer():
    # Arrange
    contract_reto = deploy_contract(Reto1Control)
    account_writer = get_account(1)
    account_admin = get_account(0)
    writer = contract_reto.ROL_WRITER()
    # Act
    tx = contract_reto.addRoleWriter(account_writer,{"from":account_admin})
    tx.wait(1)
    # Assert
    assert contract_reto.hasRole(writer,account_writer) == True
    # Act 2
    tx2 = contract_reto.deleteRoleWriter(account_writer,{"from":account_admin})
    # Assert 2
    assert contract_reto.hasRole(writer,account_writer) == False


def test_only_admin_addRole():
    # Arrange
    contract_reto = deploy_contract(Reto1Control)
    account_admin = get_account(0)
    account_writer = get_account(1)
    new_writer = get_account(2)
    # Assert 1
    with pytest.raises(exceptions.VirtualMachineError):
        contract_reto.addRoleWriter(new_writer,{"from":account_writer})
    # Act
    tx = contract_reto.addRoleWriter(account_writer,{"from":account_admin})
    tx.wait(1)
    # Assert 2
    with pytest.raises(exceptions.VirtualMachineError):
        contract_reto.addRoleWriter(new_writer,{"from":account_writer})