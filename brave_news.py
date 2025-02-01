import requests
from env import *


import requests
def brave_news_search(query, count=10):
    """
    News search using Brave News API
    
    Args:
        query (str): Search term
        count (int): Number of articles to return. The maximum is 50.
    
    Returns:
        list: List of news articles
    """
    
    url = f"https://api.search.brave.com/res/v1/news/search?q={query.replace(' ', '+')}&count={count}"
    
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": BRAVE_API_KEY
    }
    print(url)
    print('starting 1')    
    try:
        print(f"Searching for: {query}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        # Print raw response for debugging
        print(f"\nAPI Response Status: {response.status_code}")
        
        articles = data['results']
        print(f"Found {len(articles)} articles")
        
        return articles
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

