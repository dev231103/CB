// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

library MathLib {

    function square(uint x) internal pure returns (uint) {
        return x * x;
    }

    function cube(uint x) internal pure returns (uint) {
        return x * x * x;
    }
}

contract AdvancedFeatures {

    using MathLib for uint;

    uint public result;

    event Computed(string operation, uint value);
    event ErrorHandled(string reason);

    error DivisionByZero();
    error UnderflowError(uint a, uint b);

    function computeSquare(uint x) public {
        result = x.square();
        emit Computed("square", result);
    }

    function computeCube(uint x) public {
        result = x.cube();
        emit Computed("cube", result);
    }

    function multiplyAssembly(uint a, uint b) public returns (uint product) {
        assembly {
            product := mul(a, b)
        }

        result = product;
        emit Computed("assemblyMultiply", result);
    }

    function safeDivide(uint a, uint b) public returns (uint) {
        if (b == 0) {
            emit ErrorHandled("Division by zero attempted");
            revert DivisionByZero();
        }

        result = a / b;
        emit Computed("safeDivide", result);
        return result;
    }

    function safeSubtract(uint a, uint b) public returns (uint) {
        if (b > a) {
            emit ErrorHandled("Underflow detected");
            revert UnderflowError(a, b);
        }

        result = a - b;
        emit Computed("safeSubtract", result);
        return result;
    }
}
