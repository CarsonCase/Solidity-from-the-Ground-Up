// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract HelloYul {

    function MyFunction(uint myValue) external pure{
        assembly{
            if eq(myValue, 25){
                stop()
            }
                revert(0,0)
        }
    }
}