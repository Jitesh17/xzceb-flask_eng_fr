from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator",template_folder='final_project/templates')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    print(textToTranslate)
    translatedText = translator.englishToFrench(textToTranslate)
    print(translatedText)
    return translatedText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    print(textToTranslate)
    translatedText = translator.frenchToEnglish(textToTranslate)
    print(translatedText)
    return translatedText

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
