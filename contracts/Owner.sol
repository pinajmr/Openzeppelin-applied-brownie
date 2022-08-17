// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract Owner is Ownable {
    uint public key;

    function forAll() public {
        key = 1;
    }

    function justOwner() public onlyOwner {
        key = 2;
    }
}
