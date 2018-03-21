from app import app
from flask import render_template, request, redirect

from process_data.sentence import Sentence
from tagger.tagger_str import tag_sent


@app.route('/', methods=['POST', 'GET'])
def index():
    sent_str = ''
    sentence = Sentence('demo_app', [])
    if request.method == "POST":
        result = request.form
        sent_str = result.get('exampleSentence', '')
        sentence = tag_sent(sent_str)
    return render_template('index.html',
                           title="Demo for NER-Tagging in german",
                           sent_str=sent_str,
                           sentence=[(word.token, word.outer_label_pred)
                                     for word in sentence.sent])
