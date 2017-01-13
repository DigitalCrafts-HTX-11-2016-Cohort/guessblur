from flask import Flask, render_template, url_for, session, request, redirect
from random import randint
import pg

db = pg.DB(host="localhost", user="postgres", passwd="rocket", dbname="GuessBlur")

app = Flask(__name__)

scores = db.query(
    'select * from scores where score > 0 order by score desc limit 5').namedresult()


@app.route('/', methods=['GET'])
def index():
    scores = db.query(
        'select * from scores where score > 0 order by score desc limit 5').namedresult()
    return render_template('index.html', scores=scores)


@app.route('/start_game', methods=['POST'])
def start_game():
    # starting the session to keep track of points
    name = request.form.get('name')
    session['name'] = name
    session['points'] = 0
    session['missed'] = 0
    session['attempts'] = 3
    return redirect('/play')


@app.route('/play', methods=['GET', 'POST'])
def number():
    scores = db.query(
        'select * from scores where score > 0 order by score desc limit 5').namedresult()
    # picking a random image using SQL script and a random description using randint
    s = randint(1, 2)
    img = db.query('select * from images order by random() limit 1').namedresult()
    return render_template("play1.html", s=s, img=img, scores=scores)


@app.route('/selection', methods=['POST', 'GET'])
def selection():
    action = request.args.get('action')
    print "action=" + action
    if action == 'Yes':
        # player recieves points upon guessing correctly
        session['points'] = session.get('points', 0) + 1
        return '{"success": "True", "points": "%d"}' % session['points']
    elif action == 'No':
        # if the player gets 3 wrong, they lose
        session['missed'] = session.get('missed') + 1
        session['attempts'] = session.get('attempts') - 1
        return '{"success": "False", "points": "%d", "misses": "%d"}' % (session['points'], session['missed'])


@app.route('/game_over')
def game_over():
    scores = db.query(
        'select * from scores where score > 0 order by score desc limit 5').namedresult()
    return render_template('/game_over.html', scores=scores)


@app.route('/about')
def about():
    scores = db.query(
        'select * from scores where score > 0 order by score desc limit 5').namedresult()
    return render_template('/about.html', scores=scores)


@app.route('/end_game', methods=['POST', 'GET'])
def end_game():
    # takes the player's name and points and inserts them into a table
    name = session.get('name')
    score = session.get('points')
    db.insert('scores',
              name=name,
              score=score)
    # end the session
    del session['name']
    return redirect('/')


@app.route('/highscores', methods=['GET'])
def highscores():
    # SQL script to display the top ten scores
    scores = db.query(
        'select * from scores where score > 0 order by score desc limit 10').namedresult()
    return render_template('scores.html', scores=scores)


app.secret_key = 'whaaaaaaa'

if __name__ == '__main__':
    app.run(debug=True)
