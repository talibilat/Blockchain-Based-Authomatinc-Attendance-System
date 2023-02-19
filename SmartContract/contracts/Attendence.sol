// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/** 
 * @title Attendence
 */
contract Attendence {

    string  filehash;
    uint256 public uploaddate;

    function setUpdateDate(uint256 _uploaddate) public {
        uploaddate = _uploaddate;
    }

    function getUploadDate() public view returns (uint _uploaddate) {
        return uploaddate;
    }

    function setFile(string memory _filehash)  public  {
        filehash = _filehash;
    }

    function getFile() public view returns (string memory _filehash) {
        return filehash;
    }


}