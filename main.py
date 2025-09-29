# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from chuvash_conjugator import conjugate_chuvash

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/conjugate", methods=["POST"])
def conjugate():
    word = request.form.get("word", "").strip()
    person = request.form.get("person")
    plural = request.form.get("plural") == "on"

    # Basit input validation
    if not word:
        return render_template("index.html", error="Lütfen bir kelime girin.")
    if person not in ['1sg','2sg','3sg','1pl','2pl','3pl']:
        return render_template("index.html", error="Lütfen geçerli bir şahıs seçin.")
    if len(word) > 120:
        return render_template("index.html", error="Kelime çok uzun (maks 120 karakter).")

    result = conjugate_chuvash(word, person, plural)
    return render_template("index.html", word=word, result=result, person=person, plural=plural)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)), debug=False)

