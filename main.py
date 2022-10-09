# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from blockchain import *

app = Flask(__name__)

unique_id = str(uuid4).replace("-", "")
blockchainNew = blockchain()


@app.route("/newTransactions", methods = ["POST"])
def newTransaction():
    nodeData = request.get_json()
    try:
        index = blockchainNew.newTransaction(nodeData["sender"], nodeData["recipient"], nodeData["amount"])
        responseJson = {"message": f'transaction will be added to block {index}'}
        return jsonify(responseJson), 201 #jsonify creates response object from json message
    except:
        return "missing values", 400

@app.route("/mine", methods= ["GET"])
def mine():
    lastBlock = blockchainNew.lastBlock
    lastProof = lastBlock["proof"]
    proof = blockchainNew.proofWork(lastProof)
    blockchainNew.newTransaction("0", unique_id, 1)
    blockchainNew.__chain.append(blockchainNew.newBlock(proof))
    print("mined successfully")


@app.route("/chain", methods= ["GET"])
def chain():
    response = {
        "chain": blockchainNew.__chain,
        "length": len(blockchainNew.__chain)
    }
    return jsonify(response), 200 #200 means server nodes correct request


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
