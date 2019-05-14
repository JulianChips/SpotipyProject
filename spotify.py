import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import MySpotify as sp

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/spotify.sqlite"

db = SQLAlchemy(app)

class Features(db.Model):
	__tablename__ = "features"

	id = db.Column(db.Integer, primary_key=True)
	artist = db.Column(db.String(64))
	album = db.Column(db.String(64))
	song = db.Column(db.String(64))
	danceability = db.Column(db.Float)
	energy = db.Column(db.Float)
	key = db.Column(db.Integer)
	loudness = db.Column(db.Float)
	mode = db.Column(db.Float)
	speechiness = db.Column(db.Float)
	acousticness = db.Column(db.Float)
	instrumentalness = db.Column(db.Float)
	liveness = db.Column(db.Float)
	valence = db.Column(db.Float)
	tempo = db.Column(db.Float)
	uri = db.Column(db.String(64))
	duration_ms = db.Column(db.Integer)
	time_signature = db.Column(db.Integer)

	def __repr__(self):
		return '<Feature %r>' % (self.song)

@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		db.drop_all()
		db.create_all()
		artist = request.form["artist"]
		album = request.form["album"]
		song = request.form["song"]
        # return jsonify(result)#redirect("/", code=302)
		results = sp.get_song_features(sp.get_song_uri(song,album,artist))[0]
		features = Features(artist=artist,album=album,song=song,danceability=results.get("danceability"),
			energy=results.get("energy"),key=results.get("key"),loudness=results.get("loudness"),mode=results.get("mode"),
			speechiness=results.get("speechiness"),acousticness=results.get("acousticness"),instrumentalness=results.get("instrumentalness"),
			liveness=results.get("liveness"),valence=results.get("valence"),tempo=results.get("tempo"),uri=results.get("uri"),
			duration_ms=results.get("duration_ms"),time_signature=results.get("time_signature"))
		db.session.add(features)
		db.session.commit()
		return redirect("/", code=302)
	return render_template("index.html",)

@app.route("/api/features")
def features():	
	results = db.session.query(Features.artist,Features.album,Features.song,Features.danceability,Features.energy,Features.key,
		Features.loudness,Features.mode,Features.speechiness,Features.acousticness,Features.instrumentalness,Features.liveness,
		Features.valence,Features.tempo,Features.uri,Features.duration_ms,Features.time_signature).all()
	data = []
	for result in results:
		data.append({
			"artist": result[0],
			"album": result[1],
			"song": result[2],
			"danceability": result[3],
			"energy": result[4],
			"key": result[5],
			"loudness": result[6],
			"mode": result[7],
			"speechiness": result[8],
			"acousticness": result[9],
			"instrumentalness": result[10],
			"liveness": result[11],
			"valence": result[12],
			"tempo": result[13],
			"uri": result[14],
			"duration_ms": result[15],
			"time_signature": result[16],
			})
	return jsonify(data)

if __name__ == "__main__":
	app.run()