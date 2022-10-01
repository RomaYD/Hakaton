import flask
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from logic import emotion, color
from DB import Messages, Base
app = Flask(__name__)


engine = create_engine('sqlite:///base_of_users.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)



@app.route('/accept', methods=['POST'])
def accept():
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    session = DBSession()
    emot = emotion(request.json['messages'])
    color_text = color(emot)
    message = Messages(messages=request.json['messages'], Date_Time=str(datetime.datetime.now().time()), username=request.json['username'], user_id=request.json['user_id'], emotion=color_text)
    session.add(message)
    session.commit()
    return flask.jsonify({'success': 'OK'})



@app.route('/get/', methods=['GET'])
def get_messeges():
    session = DBSession()
    users = session.query(Messages).all()
    if not users:
        return flask.jsonify({'error': 'Not found'})
    users.reverse()
    list_json = []
    for i in users:
        list_json.append(i.to_dict(only=('id', 'messages', 'Date_Time', 'username', 'user_id', 'emotion')))
    return flask.jsonify(
            {
                'messages': list_json

                # 'user': users.to_dict(only=('id', 'messages'))
            }
        )


if __name__ == '__main__':
    app.run(debug=True)



















































