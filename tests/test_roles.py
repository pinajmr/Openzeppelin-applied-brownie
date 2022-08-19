


# Check deployer if it is role admin
from scripts.deploy_create import deploy_contract
from  scripts.helpful_scripts import get_account
from brownie import (exceptions,Roles,Reto1Control)
import pytest

def test_role_admin():
    #Arrange
    roles_contract = deploy_contract(Roles)
    account = get_account()
    ROL_ADMIN = roles_contract.ROL_ADMIN()
    #Act 
    # Assert
    # Check if the user has the role admin
    assert roles_contract.hasRole(ROL_ADMIN,account) == True

# Add role user
def test_role_add_user():
    #Arrange
    roles_contract = deploy_contract(Roles)
    account_admin = get_account()
    account_user = get_account(index=1)
    account_new_user = get_account(index=2)
    #Act
    ROL_USER = roles_contract.ROL_USER()
    tx = roles_contract.agregarRol(ROL_USER,account_user,{"from":account_admin})
    tx.wait(1)
    # Assert
    # Check if the user has the role user
    assert roles_contract.hasRole(ROL_USER,account_user) == True
    # Check if the user can access to soloUser function
    assert roles_contract.soloUser({"from":account_user})
    # Check if the user role cannot access to agregarRol function
    with pytest.raises(exceptions.VirtualMachineError):
        roles_contract.agregarRol(ROL_USER,account_new_user,{"from":account_new_user})

