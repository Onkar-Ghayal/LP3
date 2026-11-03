// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {

    mapping(address => uint256) private balances;

    // Deposit money
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
    }

   function withdraw(uint256 amount) public {
    require(amount > 0, "Amount must be greater than zero");
    require(balances[msg.sender] >= amount, "Insufficient balance");

    balances[msg.sender] -= amount;

    (bool success, ) = payable(msg.sender).call{value: amount}("");
    require(success, "Transfer failed");
}

    // Show balance
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}