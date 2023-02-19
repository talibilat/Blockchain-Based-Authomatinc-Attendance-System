const Attendence = require('../../models/attendence.model')
const Web3 = require('web3');
const Provider = require('@truffle/hdwallet-provider');
// const MyContract = require('./build/contracts/MyContract.json');
const address = '';
const privateKey = 'e62770ce1ea677bf80215bc87297f10f8be572d4fa52ac178d910e38c8c6ea77';
const infuraUrl = ''; 

//Upload File to the node server first then it will upload to the ipfs and return the hash for the file
// This generated hash then write on the blockchain
exports.uploadFile = async (req, res, next) => {
    try {
        const cms = await CMS.findOne({slug:req.body.slug}, { __v: 0, createdAt: 0, updatedAt: 0}).lean(true)
        if (cms)
            return res.json({ success: true, message: 'CMS retrieved successfully', cms })
        else
            return res.json({ success: false, message: settings })
    } catch (error) {
        return next(error)
    }
}

exports.readFile=async(req,res,next)=>{
    try {
        const cms = await CMS.findOne({slug:req.body.slug}, { __v: 0, createdAt: 0, updatedAt: 0}).lean(true)
        if (cms)
            return res.json({ success: true, message: 'CMS retrieved successfully', cms })
        else
            return res.json({ success: false, message: settings })
    } catch (error) {
        return next(error)
    }

}



//Hard way (web3#signTransaction() + web3#sendSignedTransaction())
exports.init1 = async () => {
  const web3 = new Web3(infuraUrl);
  const networkId = await web3.eth.net.getId();
  const myContract = new web3.eth.Contract(
    MyContract.abi,
    MyContract.networks[networkId].address
  );

  const tx = myContract.methods.setData(1);
  const gas = await tx.estimateGas({from: address});
  const gasPrice = await web3.eth.getGasPrice();
  const data = tx.encodeABI();
  const nonce = await web3.eth.getTransactionCount(address);

  const signedTx = await web3.eth.accounts.signTransaction(
    {
      to: myContract.options.address, 
      data,
      gas,
      gasPrice,
      nonce, 
      chainId: networkId
    },
    privateKey
  );
  console.log(`Old data value: ${await myContract.methods.data().call()}`);
  const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
  console.log(`Transaction hash: ${receipt.transactionHash}`);
  console.log(`New data value: ${await myContract.methods.data().call()}`);
}

//Slightly easier (web3#sendTransaction())
exports.init2 = async () => {
  const web3 = new Web3(infuraUrl);
  const networkId = await web3.eth.net.getId();
  const myContract = new web3.eth.Contract(
    MyContract.abi,
    MyContract.networks[networkId].address
  );
  web3.eth.accounts.wallet.add(privateKey);

  const tx = myContract.methods.setData(2);
  const gas = await tx.estimateGas({from: address});
  const gasPrice = await web3.eth.getGasPrice();
  const data = tx.encodeABI();
  const nonce = await web3.eth.getTransactionCount(address);
  const txData = {
    from: address,
    to: myContract.options.address,
    data: data,
    gas,
    gasPrice,
    nonce, 
    chain: 'rinkeby', 
    hardfork: 'istanbul'
  };

  console.log(`Old data value: ${await myContract.methods.data().call()}`);
  const receipt = await web3.eth.sendTransaction(txData);
  console.log(`Transaction hash: ${receipt.transactionHash}`);
  console.log(`New data value: ${await myContract.methods.data().call()}`);
}

//Easy way (Web3 + @truffle/hdwallet-provider)
exports.init3 = async () => {
  const provider = new Provider(privateKey, 'https://rinkeby.infura.io/v3/74aa9a15e2524f6980edb8a377301f3c'); 
  const web3 = new Web3(provider);
  const networkId = await web3.eth.net.getId();
  const myContract = new web3.eth.Contract(
    MyContract.abi,
    MyContract.networks[networkId].address
  );

  console.log(await myContract.methods.data().call());
  console.log(`Old data value: ${await myContract.methods.data().call()}`);
  const receipt = await myContract.methods.setData(3).send({ from: address });
  console.log(`Transaction hash: ${receipt.transactionHash}`);
  console.log(`New data value: ${await myContract.methods.data().call()}`);
}



