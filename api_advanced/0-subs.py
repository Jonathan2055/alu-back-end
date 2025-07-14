#!/usr/bin/python3
"""Importing request modula"""
import requests

def num_of_subscribers(subreddit):
    url= "https://www.reddit.com/r/"+subreddit+"/about.json"
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/your_username)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
