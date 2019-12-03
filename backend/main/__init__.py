import json
from flask import render_template, Blueprint, request
from backend.lib.single_word import SINGLEWORD

main = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path="/static")


@main.route('/getCurve', methods=['GET'])
def get_curve():
    words = request.args.getlist('words[]')
    # print(SINGLEWORD.get_curve(words))
    return SINGLEWORD.get_curve(words)


@main.route('/getCandidate', methods=['GET'])
def get_candidate():
    query = request.args['query']
    return json.dumps(SINGLEWORD.get_candidate_words(query), ensure_ascii=False)

# @main.route('/', defaults={'path': ''})
# @main.route('/<path:path>')
# def index(path):
#     return render_template('index.html')
