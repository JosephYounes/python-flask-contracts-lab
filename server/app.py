from flask import Flask, jsonify, make_response

app = Flask(__name__)

contracts = {
    "101": {"client": "Bob", "amount": 5000},
    "202": {"client": "Sarah", "amount": 12500}
}

customers = ["bob", "sarah", "alice"]

@app.route('/contract/<id>', methods=['GET'])
def get_contract(id):
    if id in contracts:
        return jsonify({
            "message": "Contract found",
            "data": contracts[id]
        }), 200
    return jsonify({"error": "Contract not found"}), 404


@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    customer_name = customer_name.lower()
    
    if customer_name in customers:
        return make_response("", 204)
    
    return jsonify({"error": "Customer not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)