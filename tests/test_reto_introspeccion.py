from scripts.deploy_create import deploy_contract
from brownie import Reto3Instropeccion, ERC20Mock, ERC721Mock
import time 

def test_isTokenERC20():
    # Arrange
    contract_ERC20 = deploy_contract(ERC20Mock)
    contract_introspeccion = deploy_contract(Reto3Instropeccion)
    # Act
    time.sleep(60)
    tx = contract_introspeccion.isTokenERC20(contract_ERC20.address)
    
    # Assert
    assert tx == True

def test_isTokenERC721():
    # Arrange
    contract_ERC721 = deploy_contract(ERC721Mock)
    contract_introspeccion = deploy_contract(Reto3Instropeccion)
    
    time.sleep(60)
    # Act
    tx = contract_introspeccion.isTokenERC721(contract_ERC721.address)
    
    # Assert
    assert tx == True
