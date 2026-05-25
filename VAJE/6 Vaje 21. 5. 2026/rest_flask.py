import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/getall', methods=['GET'])
def queryall():
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        return jsonify(records)
#        return jsonify({'error': 'data not found'})

@app.route('/', methods=['POST'])
def create():
    record = json.loads(request.data)
    with open('data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/', methods=['PUT'])
def update():
    record = json.loads(request.data)
    new_records = []
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['ime'] == record['ime']:
            r['visina'] = record['visina']
        new_records.append(r)
        
    print(new_records)
    with open('data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/', methods=['DELETE'])
def delete():
    record = json.loads(request.data)
    new_records = []
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['ime'] == record['ime']:
                continue
            new_records.append(r)
    with open('data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

app.run(host='0.0.0.0',debug=True, port=5000, use_reloader=False)
