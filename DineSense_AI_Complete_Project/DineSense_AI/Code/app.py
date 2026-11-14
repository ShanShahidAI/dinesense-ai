"""DineSense AI local Flask application. Run: python app.py"""
import json
from pathlib import Path
from flask import Flask,render_template,request,jsonify
from src.predict import analyze
ROOT=Path(__file__).resolve().parent
app=Flask(__name__)
@app.get('/')
def home():return render_template('index.html')
@app.get('/api/metrics')
def metrics():
 p=ROOT/'models'/'metrics.json'
 return jsonify(json.loads(p.read_text(encoding='utf-8')) if p.exists() else {'error':'Train the model first'})
@app.post('/api/analyze')
def api_analyze():
 try:return jsonify(analyze((request.get_json(silent=True) or {}).get('review','')))
 except (ValueError,FileNotFoundError) as exc:return jsonify({'error':str(exc)}),400
if __name__=='__main__':app.run(host='127.0.0.1',port=5000,debug=False)
