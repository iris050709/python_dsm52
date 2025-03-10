from flask import Blueprint, jsonify, request
from controllers.userController import get_all_users, get_user_by_id, create_user, update_user, delete_user, login_user

##EL PAYLOAD SON DATOS QUE SE ENVIAN

# Creación del Blueprint / ruta definida para usuarios
user_bp = Blueprint('users', __name__)

# RUTA DE LISTA DE USUARIOS
@user_bp.route('/', methods=['GET'])
def index():
    user = get_all_users()
    return jsonify(user)  # Devuelve la lista de usuarios en formato JSON

# VER UN USUARIO EN ESPECIFICO
@user_bp.route('/<int:user_id>', methods=['GET'])
def show(user_id):
    user_response = get_user_by_id(user_id)
    return user_response  # Devuelve la información del usuario específico

# CREAR UN USUARIO
@user_bp.route('/', methods=['POST']) #EL ARROBA ES UN DECORADOR
def user_Store():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    print(f"NAME {name} --- EMAIL {email} --- PASSWORD {password}")
    new_user = create_user(name, email, password)
    return jsonify(new_user)

# ACTUALIZAR USUARIO POR ID
@user_bp.route('/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"message": "El nombre y el correo electrónico son obligatorios"}), 400

    # Llamar a la función update_user
    updated_user = update_user(user_id, name, email)
    return updated_user  # Ya devuelve un JSON con error en la función update_user


# ELIMINAR UN USUARIO POR ID
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    try:
        # Llamar a la función delete_user
        result = delete_user(user_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar el usuario: {str(e)}"}), 500
    
@user_bp.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    return login_user(data['email'], data['password'])
