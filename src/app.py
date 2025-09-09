import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_members():
    
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_single_member(member_id):
    
    member = jackson_family.get_member(member_id)
    if member is None:
        raise APIException('Member not found', status_code=404)
    return jsonify(member), 200

@app.route('/member', methods=['POST'])
def add_member():
    
    request_body = request.get_json()
    
    
    if not request_body or 'first_name' not in request_body or 'age' not in request_body:
        raise APIException('First name and age are required', status_code=400)
    
    jackson_family.add_member(request_body)
    return jsonify({"message": "Member added successfully"}), 201

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    
    member = jackson_family.delete_member(member_id)
    if member is None:
        raise APIException('Member not found', status_code=404)
    return jsonify({"done": True}), 200



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
