from flask import Flask, render_template, request , redirect
import json

app = Flask(__name__)


def getSongs():
    with open('songs.json', 'r' , encoding='utf-8') as file:
        songs = json.load(file)
    for song in songs:
        song[2]=song[2].strip().split('\n')
    return songs

songs = getSongs()

@app.route('/')
def index():
    return render_template('index.html', songs = songs)

@app.route('/lyric')
def lyric():
    id = int(request.args['id'])
    return render_template('lyric.html', song = songs[id])

@app.route('/search')
def search():
    title = request.args['q']
    print(title)
    id = -1
    
    for song in songs:
        if (title.lower() in song[2].lower()) or (title.lower() in song[0].lower()):
            id = songs.index(song)
            break

    if id!=-1:
        url = '/lyric?id='+str(id)
        return redirect(url)
    else:
        print(request.url)
        return render_template('error.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
