import urllib3
import json
import pandas as pd

"""
This is the basic Implementation of a webscrapper
"""

# Input Variables
url = "https://www.goodreads.com/choiceawards/best-books-2025"

    
#Parising URL with UrlLib
reponse = urllib3.request("GET",url)

if reponse.status == 200:
    json_text = reponse.data.decode("utf-8")
    print(json_text)
    with open("Book-Review.HTML","w",encoding='utf-8')as file:
        json.dump(json_text,file, indent=4, ensure_ascii= False)
        print("File Saved")
else:
    print(f"Failed to fetch data. HTTP Status: {reponse.status}")

