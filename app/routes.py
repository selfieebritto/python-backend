from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

from app.controllers.AccountController import get_all_users, register_user, validate_user
# Create a Blueprint object for the routes
api_bp = Blueprint('api', __name__)

health_check_bp = Blueprint('health_check', __name__)


@health_check_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

@api_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = validate_user(username, password)
    print(user)

    if user:
        access_token = create_access_token(identity=username)
        return {'access_token': access_token}, 200

    return {'message': 'Invalid username or password'}, 401


@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Extract the required fields from the request
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    print(data)

    # Perform validation checks
    if not email or not password or not confirm_password:
        return jsonify({'error': 'Email, password, and confirm password are required.'}), 400

    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match.'}), 400

    # Store the user's information in the database or perform any other necessary operations
    register_user(email,password)
    # Return a success message
    return jsonify({'message': 'Registration successful.'}), 200

@api_bp.route('/getAllUsers', methods=['GET'])
@jwt_required()
def getAllUsers():
    current_user = get_jwt_identity()
    return jsonify(get_all_users())
