// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/introspection/ERC165Checker.sol";
import "@openzeppelin/contracts/interfaces/IERC20.sol";
import "@openzeppelin/contracts/interfaces/IERC721.sol";

contract Reto3Instropeccion {
    function isTokenERC20(address _contractAddress) public view returns (bool) {
        return
            ERC165Checker.supportsInterface(
                _contractAddress,
                type(IERC20).interfaceId
            );
    }

    function isTokenERC721(address _contractAddress)
        public
        view
        returns (bool)
    {
        return
            ERC165Checker.supportsInterface(
                _contractAddress,
                type(IERC721).interfaceId
            );
    }
}
