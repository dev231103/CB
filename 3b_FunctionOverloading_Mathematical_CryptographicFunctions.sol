// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AdvancedFunctionDemo {

    uint public result;

    function calculate(uint a, uint b) public pure returns (uint) {
        return a + b;
    }

    function calculate(uint a, uint b, uint c) public pure returns (uint) {
        return a + b + c;
    }

    function multiply(uint a, uint b) public pure returns (uint) {
        return a * b;
    }

    function divide(uint a, uint b) public pure returns (uint) {
        require(b != 0, "Division by zero");
        return a / b;
    }

    function power(uint base, uint exponent) public pure returns (uint) {
        return base ** exponent;
    }

    function getKeccak256(string memory input) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(input));
    }

    function getSha256(string memory input) public pure returns (bytes32) {
        return sha256(abi.encodePacked(input));
    }

    function getRipemd160(string memory input) public pure returns (bytes20) {
        return ripemd160(abi.encodePacked(input));
    }

    function recoverSigner(
        bytes32 messageHash,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) public pure returns (address) {
        return ecrecover(messageHash, v, r, s);
    }

    function getEthSignedMessageHash(string memory message)
        public
        pure
        returns (bytes32)
    {
        bytes32 msgHash = keccak256(abi.encodePacked(message));

        return keccak256(
            abi.encodePacked(
                "\x19Ethereum Signed Message:\n32",
                msgHash
            )
        );
    }
}
