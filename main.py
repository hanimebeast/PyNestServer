import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

def load_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None
    
def get_value_at_path(data_dict, keys):
    try:
        for key in keys:
            if "::" in key:
                operator, threshold = key.split('::')
                if "from:" in operator or "to:" in threshold:
                    from_value = int(operator.split("from:")[1]) if "from:" in operator else None
                    to_value = int(threshold.split("to:")[1]) + 1 if "to:" in threshold else None
                    data_dict = data_dict[from_value:to_value]
                elif "et:" in key:
                    key_name, Qfilter = operator, threshold.split("et:")[1]
                    data_dict = [item for item in data_dict if str(item.get(key_name)) == Qfilter]
                elif "gt:" in key:
                    key_name, threshold_value = operator, int(threshold.split("gt:")[1])
                    data_dict = [item for item in data_dict if item.get(key_name) > threshold_value]
                elif "lt:" in key:
                    key_name, threshold_value = operator, int(threshold.split("lt:")[1])
                    data_dict = [item for item in data_dict if item.get(key_name) < threshold_value]
            else:
                data_dict = data_dict[int(key)]
    except (KeyError, IndexError, ValueError) as e:
        return None
    return data_dict

@app.route('/', methods=['GET'])
@app.route('/<path:keys>', methods=['GET'])
def nested_data(keys=""):
    if keys == "":
        return jsonify(data)
    try:
        keys_list = keys.split('/')
        data_result = get_value_at_path(data, keys_list)
        return jsonify(data_result) if data_result is not None else jsonify({"error": "Invalid path, index out of range, or remove trailing slash."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python main.py <json_file_path>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), json_file_path))

    data = load_data_from_file(absolute_path)

    if data is None:
        print(f"Error: Unable to load data from file: {absolute_path}")
        sys.exit(1)

    app.run(port="8080", debug=True)
