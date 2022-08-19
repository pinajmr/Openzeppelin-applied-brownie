// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/governance/TimelockController.sol";

contract TimeControl is TimelockController {
    string public key;
    bytes32 public constant MODERATOR_ROLE = keccak256("MODERATOR_ROLE");

    constructor(
        string memory _key,
        uint256 _minDelay,
        address[] memory proposers,
        address[] memory executors
    ) TimelockController(_minDelay, proposers, executors) {
        key = _key;
        _setupRole(DEFAULT_ADMIN_ROLE, _msgSender());
    }

    function changeKey(string memory _key)
        public
        onlyRoleOrOpenRole(TIMELOCK_ADMIN_ROLE)
    {
        key = _key;
    }
}
