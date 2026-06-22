NFT_Interaction.sol// SPDX-License-Identifier: MIT
pragma solidity ^0.8.34;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract MyNFT is ERC721 {

    uint public tokenCount;

    constructor() ERC721("MyNFT", "MNFT") {}

    function mintNFT(address recipient) public returns (uint) {
        tokenCount++;
        _mint(recipient, tokenCount);
        return tokenCount;
    }
}
