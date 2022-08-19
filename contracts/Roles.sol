// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/AccessControl.sol";

contract Roles is AccessControl {
    bytes32 public constant ROL_ADMIN = keccak256("ROL_ADMIN");
    bytes32 public constant ROL_USER = keccak256("ROL_USER");

    constructor() {
        _setupRole(ROL_ADMIN, _msgSender());
    }

    function soloAdmin() public onlyRole(ROL_ADMIN) {
        // do something
    }

    function soloUser() public {
        require(
            hasRole(ROL_USER, _msgSender()),
            "This function is only for user role"
        );
    }

    function agregarRol(bytes32 _rol, address account) public {
        require(
            hasRole(ROL_ADMIN, _msgSender()),
            "This function is only for admin role"
        );
        _grantRole(_rol, account);
    }
}
