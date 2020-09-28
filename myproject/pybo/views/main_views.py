# ---------------------------------------- [edit] ---------------------------------------- #
from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect
from pybo.models import Question

# ---------------------------------------- [edit] ---------------------------------------- #


bp = Blueprint('main', __name__, url_prefix='/')

# ---------------------------------------- [edit] ---------------------------------------- #
@bp.route('/hello')
def hello_pybo():
    return 'hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # ---------------------------------------- [edit] ---------------------------------------- #
    question = Question.query.get_or_404(question_id)

    return render_template('question/question_detail.html', question=question)