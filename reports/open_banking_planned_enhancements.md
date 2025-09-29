# Planned Enhancements for the Open Banking NLP Analysis

This repository applies FinBERT to assess sentiment and BERTopic for topic modelling of Canadian open banking discourse.  To elevate it to a research‑grade project, we will incorporate quantitative evaluations, statistical analysis, and a structured report.

## 1. Quantitative Evaluation and Ablation

- **Forecasting benefit**: When using sentiment signals to enhance financial forecasting or risk detection, measure the improvement in predictive accuracy (e.g. MAE, RMSE) over a baseline model that excludes sentiment.  Perform an **ablation study** by training models with and without the FinBERT sentiment feature and reporting the difference.

- **Significance testing**: Use statistical tests such as the Diebold–Mariano test to determine whether the difference in forecasting errors with and without sentiment is statistically significant【751943000961771†L38-L57】.  Report confidence intervals for performance metrics to show uncertainty【520273785081046†L50-L63】.

- **Topic coherence**: Evaluate topic models using metrics like topic coherence or perplexity to ensure that the topics extracted by BERTopic meaningfully summarise the discourse.

## 2. Causal Interpretation

- **Causal framing**: If the sentiment score is used as a predictor for market risk or price movements, apply causal inference methods (e.g., Granger causality tests or CausalImpact) to assess whether sentiment spikes precede changes in financial variables.  This aligns the project with the broader goal of moving from prediction to causal reasoning.

## 3. Documentation and Reporting

- **Structured report**: Prepare a short report in the `reports/` directory that follows the structure: motivation → methods (data sources, FinBERT sentiment extraction, BERTopic, forecasting models) → results → discussion of findings and limitations.  This will make the project accessible to reviewers.

- **Figures and tables**: Include plots of sentiment trends over time, distributions of topics, and performance comparison charts.  Tables summarising model performance with and without sentiment will clearly show the added value of NLP.

By adding rigorous evaluation, significance testing and a well‑written report, this project will go beyond a demonstration of NLP tools and become a research‑oriented case study.
