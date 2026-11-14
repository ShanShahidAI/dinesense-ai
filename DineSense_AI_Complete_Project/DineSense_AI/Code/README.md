# DineSense AI — Restaurant Feedback Analyzer

**Group:** Shan (72387), Muhammad Salman (72373), Shaheryar Khan (72775)  
**Course:** Artificial Intelligence | **Instructor:** Anees Tariq | **University:** Riphah International University, Islamabad

## What it does
Local browser application for restaurant review analysis. Uses a trained TF-IDF + ML classifier for sentence sentiment (positive/negative/neutral), rule-based keyword matching for Food, Service, Price and Ambience, and rule-based suggestions. Displays browser-session analytics and real test-split model scores.

## Run on Windows / macOS / Linux
1. Install Python 3.10 or newer. Open terminal **inside the `Code` folder**.
2. `python -m venv .venv`
3. Windows: `.venv\Scripts\activate` | macOS/Linux: `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python -m src.train`
6. `python app.py`
7. Open **http://127.0.0.1:5000** in Chrome.

Stop the server with Ctrl+C. No internet needed after installation. Do not open `index.html` directly; Flask serves the pages and API.

## Important academic honesty and limitations
- `data/sample_reviews.csv` is **120 original, hand-written educational examples**, not an external research dataset and not actual restaurant customers. It is provided so the project runs without downloading anything else.
- Accuracy measured on this small, artificial dataset does **not** establish real-world quality. Do not claim it does.
- Aspect detection is **keyword rules**, not a trained aspect-based classifier. Multi-aspect and negation cases can fail.
- For the instructor's real-world dataset requirement, download a properly licensed restaurant dataset (for example SemEval-2014 Task 4 restaurant data), review its terms, convert the annotated data to `review,aspect,sentiment` CSV and run `python -m src.train --data data/your_reviews.csv`. The simple training script trains **sentiment only**; aspect annotations are retained for later analysis, but not trained as aspect labels.
- Do not report external dataset evaluation until you have actually run it. Keep train/test separation and document the source and cleaning choices.
- No API keys, database, paid services or hardware are required.

## Code map
- `app.py`: Flask routes and JSON API
- `src/train.py`: TF-IDF, two ML models, evaluation and saved model
- `src/predict.py`: sentiment inference, keyword aspect detection, suggestions
- `templates/index.html`: website structure
- `static/style.css`: responsive styling
- `static/app.js`: browser interaction, charts, result rendering
- `models/metrics.json`: real evaluation from included demo data

## Suggested team responsibilities
Shan — dataset collection, cleaning, problem statement. Muhammad Salman — training, comparison, metrics. Shaheryar Khan — website, Flask integration, GitHub, presentation. All three should understand the full pipeline; verify actual contributions before submission.

## Viva demonstration
1. Explain the problem. 2. Show `data/sample_reviews.csv`. 3. Show `src/train.py` and saved metrics. 4. Run the browser app. 5. Analyze a review. 6. Explain aspect keywords vs ML sentiment. 7. Show Model Results and limitations.
