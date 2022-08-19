// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/access/AccessControl.sol";

contract Reto1Control is AccessControl {
    uint256 number;

    bytes32 public constant ROL_ADMIN = keccak256("ROL_ADMIN");
    bytes32 public constant ROL_WRITER = keccak256("ROL_WRITER");

    constructor() {
        _setupRole(ROL_ADMIN, _msgSender());
    }

    function store(uint256 num) public onlyRole(ROL_WRITER) {
        number = num;
    }

    function retrieve() public view returns (uint256) {
        return number;
    }

    function addRoleWriter(address _newWriter) public onlyRole(ROL_ADMIN) {
        _grantRole(ROL_WRITER, _newWriter);
    }

    function deleteRoleWriter(address _writer) public onlyRole(ROL_ADMIN) {
        _revokeRole(ROL_WRITER, _writer);
    }
}
