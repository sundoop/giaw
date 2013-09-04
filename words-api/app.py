#!env/bin/python

from flask import Flask, jsonify,abort, make_response

app = Flask(__name__)


words = [

    {
        'id':1,
        'title':'',
        'meaning':''
    },
    {
        'id':2,
        'title':'',
        'meaning':''
    },
    {
        'id':3,
        'title':'',
        'meaning':''
    },
    {
        'id':4,
        'title':'',
        'meaning':''
    },

]

@app.route('/')
def index():
    return "hello world!"


@app.route('/words/api/v1.0/words', methods = ['GET'])
def get_words():
    return jsonify({'words':words})


@app.route('/words/api/v1.0/words/<int:word_id>', methods = ['GET'])
def get_word(word_id):
    word = filter(lambda w: w['id'] == word_id, words)
    if len(word) == 0:
        abort(404)

    return jsonify({'word':words[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not happening'}), 404)

if __name__ == "__main__":
    app.run(debug=True)