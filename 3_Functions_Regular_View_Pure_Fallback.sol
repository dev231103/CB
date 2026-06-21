// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FunctionTypesDemo {

    uint public count;
    string public message;

    constructor() {
        count = 0;
        message = "Hello, Ethereum!";
    }

    function incrementCount() public {
        count += 1;
    }

    function getCount() public view returns (uint) {
        return count;
    }

    function add(uint a, uint b) public pure returns (uint) {
        return a + b;
    }

    fallback() external payable {
        message = "Fallback function called";
    }

    receive() external payable {
        message = "Receive function called";
    }
}
