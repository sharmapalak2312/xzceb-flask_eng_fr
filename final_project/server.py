import machinetranslation as machine
from flask import Flask, render_template, request
import json
from deep_translator import MyMemoryTranslator


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = machine.translator.english_to_french(textToTranslate)
    return render_template("index.html", translated_text=translated_text)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = machine.translator.french_to_english(textToTranslate)
    return render_template("index.html", translated_text=translated_text)

@app.route("/")
def renderIndexPage():
    # render index.html
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
