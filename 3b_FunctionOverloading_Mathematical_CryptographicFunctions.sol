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




// 0x2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae – hash 
// 27- v 
// 0x6b1d5f7a6b8c1f9d9e2b6d8c5a7f4b3e2c1a9d8f7e6c5b4a3d2c1b0a9f8e7d6c – r 
// 0x5f2c3e4d6a7b8c9d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d – s
