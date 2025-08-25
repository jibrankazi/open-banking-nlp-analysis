"""
Data ingestion module for Open Banking NLP Analysis.

This module provides functions to fetch Open Banking-related articles and documents
from public sources such as news APIs and web pages. The functions return pandas
DataFrames and save raw text to CSV files. API keys should be provided via environment
variables or passed into functions.
"""

import os
from typing import List, Dict, Optional
import requests
import pandas as pd
from bs4 import BeautifulSoup


def fetch_newsapi_articles(api_key: str, query: str, from_date: str, to_date: str, page_size: int = 100) -> pd.DataFrame:
    """
    Fetch articles matching a query from the NewsAPI.

    Parameters:
        api_key (str): NewsAPI key.
        query (str): Search keywords.
        from_date (str): ISO date string for start (YYYY-MM-DD).
        to_date (str): ISO date string for end (YYYY-MM-DD).
        page_size (int): Number of articles per page (max 100).

    Returns:
        pd.DataFrame: DataFrame with columns ['source', 'author', 'title', 'description', 'content', 'publishedAt', 'url'].
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": page_size,
        "apiKey": api_key,
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    articles = data.get("articles", [])
    records = []
    for art in articles:
        records.append({
            "source": art.get("source", {}).get("name"),
            "author": art.get("author"),
            "title": art.get("title"),
            "description": art.get("description"),
            "content": art.get("content"),
            "publishedAt": art.get("publishedAt"),
            "url": art.get("url"),
        })
    return pd.DataFrame(records)


def fetch_press_release(url: str) -> Optional[str]:
    """
    Scrape the text content from a press release web page.

    Parameters:
        url (str): URL to the press release.

    Returns:
        Optional[str]: The extracted text content, or None if failed.
    """
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        paragraphs = [p.get_text(separator=" ", strip=True) for p in soup.find_all("p")]
        return " ".join(paragraphs)
    except Exception as e:
        print(f"Failed to fetch press release from {url}: {e}")
        return None


def save_texts_to_csv(texts: List[Dict[str, str]], output_path: str) -> None:
    """
    Save a list of text records to a CSV file.

    Parameters:
        texts (List[Dict[str, str]]): List of dictionaries with text and metadata.
        output_path (str): Destination CSV path.
    """
    df = pd.DataFrame(texts)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    # Example usage
    api_key = os.getenv("NEWS_API_KEY")
    if api_key:
        df = fetch_newsapi_articles(api_key, "open banking Canada", "2019-01-01", "2025-12-31")
        save_texts_to_csv(df.to_dict(orient="records"), "data/raw/news_articles.csv")
