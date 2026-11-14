"""Hybrid demo: ML sentiment + transparent keyword-based aspect matching."""
import re
from pathlib import Path
import joblib
ROOT=Path(__file__).resolve().parents[1]
KEYWORDS={
 'Food':['food','meal','burger','pizza','dessert','chicken','soup','pasta','dish','chef','taste','flavor','menu','rice','sandwich','salad'],
 'Service':['service','staff','waiter','server','order','manager','team','served','request'],
 'Price':['price','bill','cost','money','expensive','cheap','affordable','overpriced','value','discount','charged','receipt','cashier'],
 'Ambience':['ambience','atmosphere','seating','decor','interior','lighting','music','dirty','clean','table','room','vibe','hall','walls','chairs','window']}
ADVICE={'Food':'Review food quality and consistency.','Service':'Improve staff response time and customer care.','Price':'Review menu prices and value for money.','Ambience':'Improve cleanliness, comfort and atmosphere.'}
_model=None

def get_model():
 global _model
 if _model is None:
  path=ROOT/'models'/'sentiment_model.joblib'
  if not path.exists():raise FileNotFoundError('Model missing. Run: python -m src.train')
  _model=joblib.load(path)
 return _model

def split_review(text):
 # Split on sentence boundaries and common contrast connectors.
 return [s.strip(' .,!') for s in re.split(r'[.!?;]+|\b(?:but|however|although)\b|,\s*(?:and|but)\s+',text,flags=re.I) if s.strip(' .,!')]

def analyze(text):
 if not isinstance(text,str) or not text.strip():raise ValueError('Enter a review first.')
 if len(text)>3000:raise ValueError('Review is too long (max 3000 characters).')
 model=get_model();results=[]
 for segment in split_review(text):
  matched=[name for name,words in KEYWORDS.items() if any(re.search(r'\b'+re.escape(w)+r'\b',segment,re.I) for w in words)]
  if not matched:matched=['General']
  label=str(model.predict([segment])[0]);confidence=float(max(model.predict_proba([segment])[0])) if hasattr(model,'predict_proba') else None
  for aspect in matched:results.append({'aspect':aspect,'sentiment':label,'text':segment,'confidence':round(confidence,3) if confidence is not None else None})
 counts={x:sum(r['sentiment']==x for r in results) for x in ['positive','negative','neutral']}
 overall='Mixed' if counts['positive'] and counts['negative'] else max(counts,key=counts.get).title()
 suggestions=list(dict.fromkeys(ADVICE[r['aspect']] for r in results if r['sentiment']=='negative' and r['aspect'] in ADVICE))
 return {'overall':overall,'aspects':results,'counts':counts,'suggestions':suggestions or ['Keep monitoring customer feedback.'],'disclaimer':'Predictions are estimates. Aspect tags are rule-based; confidence is not guaranteed calibration.'}
