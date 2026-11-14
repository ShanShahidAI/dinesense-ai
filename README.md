# DineSense AI — Smart Restaurant Experience Analyzer

**Course:** Artificial Intelligence  
**Team:** Shan (72387), Muhammad Salman (72373), Shaheryar Khan (72775)  
**University:** Riphah International University, Islamabad

A local Flask web application for demonstrating restaurant-review sentiment classification, aspect detection and improvement recommendations.

## Features

- Train and evaluate a TF-IDF + machine-learning sentiment classifier
- Analyze feedback for positive, negative and neutral sentiment
- Use **keyword-based rules** to identify Food, Service, Price and Ambience aspects
- Show model evaluation results and session-based review analytics in the browser
- Generate basic actionable suggestions

## Repository contents

| Path | Purpose |
| --- | --- |
| `app.py` | Local Flask web server and JSON endpoints |
| `src/train.py` | Training and model evaluation |
| `src/predict.py` | Review sentiment inference, keyword aspects and suggestions |
| `templates/` | Flask HTML template |
| `static/` | CSS and frontend JavaScript |
| `data/` | Sample training reviews and dataset notice |
| `models/` | Saved model and evaluation metrics |
| `docs/` | Project proposal, report, viva guide and development notes |
| `presentation/` | Semester project presentation |

## Run locally

Python **3.10+** recommended.

```bash
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Then:

```bash
python -m pip install -r requirements.txt
python -m src.train
python app.py
```

Open **http://127.0.0.1:5000**. Stop with Ctrl+C.

On Windows, `RUN_WINDOWS.bat` is also included in the original submission; inspect it before running. The application should be started through Flask, not by opening `templates/index.html` directly.

## Academic limitations and data provenance

The bundled `data/sample_reviews.csv` contains **120 hand-written educational samples**, not a representative collection of real customer reviews. The saved evaluation metrics are specific to these samples and **do not establish real-world accuracy**.

**Sentiment is trained ML; aspect identification and suggestions use rules.** This is not a fully trained aspect-based sentiment model. The included [developer guide](docs/DEVELOPMENT.md) explains the pipeline, dataset caveats, and viva demonstration.

## Project documentation

- [Project proposal — PDF](docs/DineSense_AI_Proposal.pdf)
- [Final project report — PDF](docs/DineSense_AI_Project_Report.pdf)
- [Presentation — PowerPoint](presentation/DineSense_AI_Presentation.pptx)

## Preservation

The uploaded archive's original folder hierarchy and cache files are preserved in branch `backup/before-ai-reorganization-2026-11-14`. This main branch removes generated `.pyc` caches and flattens unnecessary directory nesting. The source files themselves were moved without changing their Git blobs.

> **Status:** Source code and academic deliverables are present. This restructuring did not independently execute model training or run a deployment.
