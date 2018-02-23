from app import app
from flask import render_template, request

from process_data.sentence import Sentence
from tagger.tagger_str import tagger, tag_sent


@app.route('/', methods=['POST', 'GET'])
def index():
    sent_str=''
    sentence = Sentence('demo_app', [])
    if request.method == "POST":
        result = request.form
        sent_str = result.get('exampleSentence', '')
        sentence = tag_sent(sent_str)
    return render_template('index.html',
                           title="NER-Tagging in german",
                           sent_str=sent_str,
                           sentence=zip(sentence.tokens, sentence.outer_labels_pred, sentence.poss))
