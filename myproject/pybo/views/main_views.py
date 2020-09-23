# ---------------------------------------- [edit] ---------------------------------------- #
from flask import Blueprint, url_for
from werkzeug.utils import redirect

# ---------------------------------------- [edit] ---------------------------------------- #


bp = Blueprint('main', __name__, url_prefix='/')

# ---------------------------------------- [edit] ---------------------------------------- #
@bp.route('/hello')
def hello_pybo():
    return 'hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))


# ---------------------------------------- [edit] ---------------------------------------- #