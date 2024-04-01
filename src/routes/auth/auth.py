from flask import Blueprint, render_template

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template('auth/registro.html')
    
    
@bp.route('/login', methods=['GET', 'POST'])
def login():
    return {
        'msg': ' Página de Login'
    }
    
    