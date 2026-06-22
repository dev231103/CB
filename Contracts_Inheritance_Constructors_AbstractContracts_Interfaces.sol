// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IVehicle {
    function startEngine() external pure returns (string memory);
}

abstract contract Machine {

    string public manufacturer;

    constructor(string memory _manufacturer) {
        manufacturer = _manufacturer;
    }

    function getManufacturer() public view returns (string memory) {
        return manufacturer;
    }

    function operate() public view virtual returns (string memory);
}

contract Car is Machine, IVehicle {

    string public model;

    constructor(string memory _manufacturer, string memory _model)
        Machine(_manufacturer)
    {
        model = _model;
    }

    function operate() public view override returns (string memory) {
        return string(abi.encodePacked("Driving ", model));
    }

    function startEngine() public pure override returns (string memory) {
        return "Engine started";
    }

    function getCarInfo() public view returns (string memory, string memory) {
        return (manufacturer, model);
    }
}

contract ElectricCar is Car {

    uint public batteryLevel;

    constructor(
        string memory _manufacturer,
        string memory _model,
        uint _batteryLevel
    ) Car(_manufacturer, _model) {
        batteryLevel = _batteryLevel;
    }

    function recharge() public {
        batteryLevel = 100;
    }

    function getElectricCarInfo()
        public
        view
        returns (string memory, string memory, uint)
    {
        return (manufacturer, model, batteryLevel);
    }
}
