# from flask import Flask, render_template, request, redirect

# app = Flask(__name__, template_folder='src')

# # In-memory list to store moods
# mood_db = []

# @app.route('/')
# def index():
#     return render_template('index.html', moods=mood_db)

# @app.route('/log', methods=['POST'])
# def log_mood():
#     mood = request.form.get('mood')
#     if mood:
#         mood_db.append(mood)
#     return redirect('/')

# @app.route('/clear')
# def clear_moods():
#     mood_db.clear()
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect
from collections import Counter

app = Flask(__name__, template_folder='src')

# In-memory list to store moods with comments
mood_db = []

@app.route('/')
def index():
    mood_summary = Counter([entry['mood'] for entry in mood_db])
    return render_template('index.html', moods=mood_db, mood_summary=mood_summary)

@app.route('/log', methods=['POST'])
def log_mood():
    mood = request.form.get('mood')
    comment = request.form.get('comment')
    if mood:
        mood_db.append({'mood': mood, 'comment': comment})
    return redirect('/')

@app.route('/clear')
def clear_moods():
    mood_db.clear()
    return redirect('/')

@app.route('/mood-summary')
def mood_summary():
    mood_summary = Counter([entry['mood'] for entry in mood_db])
    return render_template('mood_summary.html', mood_summary=mood_summary)

if __name__ == '__main__':
    app.run(debug=True)
