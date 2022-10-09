import hashlib
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request


class blockchain():
    def __init__(self):
        self.__chain = []
        self.__currentTransactions = []
        self.newBlock(previousHash = 1, proof=100)

    def newBlock(self, proof, previousHash=None):
        block = {
            "index" : len(self.__chain) + 1,
            "timestamp": time(),
            "transactions": self.__currentTransactions,
            "proof": proof,
            "previoushash": previousHash or self.hash(self.__chain[-1])
        }

        self.__currentTransactions = []
        self.__chain.append(block)
        return block

    #returns index of the new block
    def newTransaction(self, sender, recipient, amount):
        self.__currentTransactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })
        return self.lastBlock["index"] + 1

    @staticmethod
    def hash(self, block):
        blockString = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(blockString).hexdigest()


    @property
    def lastBlock(self):
        return self.__chain[-1]

    def proofWork(self, lastProof):
        proof = 0
        while True:
            attempt = f'{lastProof}{proof}'.encode()
            hashNew = hashlib.sha256(attempt).hexdigest()
            if hashNew[:4] == "0000":
                return proof
            else:
                proof += 1




