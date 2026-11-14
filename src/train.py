"""Train and evaluate baseline sentiment models using a labeled CSV.
Run: python -m src.train --data data/sample_reviews.csv
This bundled dataset is ORIGINAL EDUCATIONAL DEMO DATA, not SemEval.
For academic evaluation replace it with an independently sourced labeled dataset.
"""
import argparse, json
from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix, classification_report
ROOT = Path(__file__).resolve().parents[1]

def train(data_path, model_dir=None):
    df = pd.read_csv(data_path).dropna(subset=['review','sentiment','aspect']).drop_duplicates(subset=['review'])
    df['sentiment'] = df['sentiment'].astype(str).str.lower().str.strip()
    df = df[df['sentiment'].isin(['positive','negative','neutral'])]
    if len(df)<30 or df['sentiment'].value_counts().min()<3:
        raise ValueError('Need >=30 labeled rows and >=3 examples per sentiment.')
    X_train, X_test, y_train, y_test = train_test_split(df.review,df.sentiment,test_size=0.25,random_state=42,stratify=df.sentiment)
    models = {'Logistic Regression': LogisticRegression(max_iter=1500,random_state=42), 'Naive Bayes': MultinomialNB()}
    results={}; pipelines={}
    for name,est in models.items():
        pipe=Pipeline([('tfidf',TfidfVectorizer(ngram_range=(1,2),lowercase=True)),('model',est)])
        pipe.fit(X_train,y_train)
        pred=pipe.predict(X_test)
        p,r,f,_=precision_recall_fscore_support(y_test,pred,average='macro',zero_division=0)
        labels=['negative','neutral','positive']
        results[name]={'accuracy':round(float(accuracy_score(y_test,pred)),4),'precision_macro':round(float(p),4),'recall_macro':round(float(r),4),'f1_macro':round(float(f),4),'confusion_matrix':confusion_matrix(y_test,pred,labels=labels).tolist(),'labels':labels,'classification_report':classification_report(y_test,pred,zero_division=0)}
        pipelines[name]=pipe
    winner=max(results,key=lambda n:results[n]['f1_macro'])
    out=Path(model_dir) if model_dir else ROOT/'models';out.mkdir(parents=True,exist_ok=True)
    joblib.dump(pipelines[winner],out/'sentiment_model.joblib')
    summary={'selected_model':winner,'dataset_rows':len(df),'train_rows':len(X_train),'test_rows':len(X_test),'dataset_file':str(Path(data_path).name),'dataset_type':'original educational demo data' if 'sample_reviews' in str(data_path) else 'user supplied labeled dataset; verify source and license','results':results,'caution':'Small synthetic demo set; scores are NOT real-world performance. Aspect detection uses rules, not a trained aspect classifier.'}
    (out/'metrics.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print('Training complete. Selected:',winner)
    for n,metrics in results.items():print(n,'accuracy:',metrics['accuracy'],'macro F1:',metrics['f1_macro'])
    return summary

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--data',default=str(ROOT/'data'/'sample_reviews.csv'));args=parser.parse_args();train(args.data)
