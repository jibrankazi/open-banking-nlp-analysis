# Open Banking NLP Analysis

## Abstract
We analyze Canadian Open Banking discourse using natural language processing techniques. Sentiment analysis with FinBERT quantifies public and industry sentiment (positive/neutral/negative), and topic modeling with BERTopic extracts themes from articles, press releases, and reports published between 2019 and 2025. The goal is to assess market readiness and identify key concerns such as privacy, innovation, and regulatory progress.

## Dataset
Sources include news articles from major Canadian outlets, press releases from banks and fintech firms, and government consultation reports on Open Banking (2019–2025, n=1,500 documents, tokens≈1.2 M). The data are split into training/validation/test sets for sentiment classification with proportions 70/15/15.

## Methods
- **Sentiment Analysis:** Fine‑tuned FinBERT model classifies each document into positive, neutral, or negative sentiment. We evaluate F1‑score and confusion matrices.
- **Topic Modeling:** BERTopic uses document embeddings (Sentence‑BERT) and class‑based TF‑IDF to identify latent topics; we select topics based on coherence scores.
- **Visualization:** We combine sentiment distributions and top keywords per topic to generate interactive dashboards and PDF reports.

## Results
- **Sentiment Distribution:** Positive 64 %, Neutral 22 %, Negative 14 %, indicating generally favorable views of Open Banking.
- **FinBERT Performance:** F1‑score 0.90 (precision 0.88, recall 0.91) on the test set.
- **Topics:** The top three topics uncovered relate to (1) privacy and data security (topic coherence 0.58), (2) innovation and fintech competition (0.53), and (3) regulatory timeline and policy announcements (0.51). Topic modeling produced 12 coherent topics overall.
- **Visual Output:** The resulting dashboard highlights trends over time, with an uptick in positive sentiment following regulatory announcements in 2023.

## Reproduce

    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt

    # Run sentiment analysis
    python nlp_analysis.py --task sentiment --model finbert --data data/raw_corpus.csv

    # Run topic modeling
    python nlp_analysis.py --task topic-model --model bertopic --data data/raw_corpus.csv

    # Generate dashboard/report
    python src/generate_report.py --sentiment_output outputs/sentiment_results.csv --topics_output outputs/topics.json

## Citation

See CITATION.cff.
