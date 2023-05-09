from flask import Blueprint, request, jsonify

# Create a Blueprint object for the routes
api_bp = Blueprint('api', __name__)

@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Extract the required fields from the request
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    # Perform validation checks
    if not email or not password or not confirm_password:
        return jsonify({'error': 'Email, password, and confirm password are required.'}), 400

    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match.'}), 400

    # Store the user's information in the database or perform any other necessary operations

    # Return a success message
    return jsonify({'message': 'Registration successful.'}), 200
