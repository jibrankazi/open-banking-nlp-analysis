# Open Banking NLP Analysis

## Project Overview
This repository contains a Natural Language Processing (NLP) project that analyzes the public and industry discourse surrounding **Open Banking** in Canada. The goal is to gauge market readiness by extracting sentiment and key themes from news articles, press releases, and government reports between 2019 and 2025. We leverage FinBERT for sentiment analysis and BERTopic for topic modeling to identify prevailing opinions and highlight the most‑discussed issues such as privacy concerns, innovation opportunities, and regulatory progress.

## Objectives
- Collect and preprocess a diverse corpus of Open Banking‑related texts from publicly available sources.
- Perform sentiment analysis using FinBERT to classify each document as positive, neutral, or negative.
- Apply BERTopic to uncover latent topics and see how they evolve over time.
- Combine sentiment and topics to understand how different themes are perceived in the market.
- Visualize results in an interactive Power BI dashboard and summarize findings in a business‑oriented PDF brief.

## Data Sources
- **News articles**: Articles from major Canadian news outlets and fintech blogs covering Open Banking (via a news API such as GNews or NewsAPI).
- **Press releases**: Official announcements from banks, fintech associations, and government agencies.
- **Government reports**: Public consultation documents and Budget announcements about Open Banking.

Only publicly available content is used; ensure compliance with API terms of service.

## Tech Stack
- Python 3.9/3.10
- Transformers (FinBERT via HuggingFace) for sentiment analysis.
- BERTopic for topic modeling.
- spaCy & NLTK for text preprocessing.
- pandas, numpy, matplotlib, seaborn for data handling and plots.
- Power BI for dashboard creation.

## Installation
1. **Clone this repository**:
   ```bash
   git clone https://github.com/jibrankazi/open-banking-nlp-analysis.git
   cd open-banking-nlp-analysis
   ```
2. **Set up a virtual environment and install dependencies**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Download spaCy language models** (optional, if using spaCy):
   ```bash
   python -m spacy download en_core_web_sm
   ```
4. **Obtain API keys**: Register for any news APIs you plan to use (e.g. NewsAPI) and store your keys in a `.env` file or environment variables. **Do not hard‑code secrets** in the code.

## Usage
- **Data collection**: Use `src/data_ingestion.py` (to be added) to fetch articles and documents via APIs or web scraping. This module writes raw text and metadata to a CSV in `data/raw/`.
- **NLP analysis**: Run `nlp_analysis.py` or the Jupyter notebook `notebooks/open_banking_nlp.ipynb` to clean the text, perform sentiment analysis with FinBERT, and apply BERTopic for topic modeling. The script/notebook saves processed data and model outputs to `data/processed/`.
- **Visualization**: Import the processed dataset into Power BI using the `.pbix` template provided in `dashboards/` (to be added) to explore sentiment trends and topic distributions.
- **Report**: Read the business summary in `reports/` for a high‑level overview of the findings and recommendations.

## Repository Structure
```
open-banking-nlp-analysis/
├── nlp_analysis.py      # High-level pipeline script orchestrating sentiment and topic modeling.
├── requirements.txt     # Python dependencies.
├── README.md            # Project documentation (this file).
├── src/                 # Modular Python code (data ingestion, preprocessing, models) – to be populated.
├── data/
│   ├── raw/             # Raw scraped text (not committed to version control).
│   └── processed/       # Cleaned text, sentiment scores, topic assignments.
├── notebooks/           # Jupyter notebooks for exploratory work and analysis.
├── dashboards/          # Power BI .pbix files and supporting assets.
└── reports/
    └── open_banking_summary.pdf  # Final business brief.
```

## Notes
- Large raw text files and proprietary API keys are not stored in the repository.
- Adjust model hyperparameters in `nlp_analysis.py` or the notebook as needed.
- When publishing the Power BI dashboard, ensure only aggregated results are displayed to respect content usage rights.
