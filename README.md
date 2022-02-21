Reddit Coin Data Agreggator

Technologies & Tools used:

![](https://img.shields.io/badge/Code-Python-blue?logo=Python&logoColor=yellow)
![](https://img.shields.io/badge/Code-Pandas-blue?logo=pandas&logoColor=yellow)
![](https://img.shields.io/badge/Code-JupyterNotebook-blue?logo=Jupyter&logoColor=yellow)
![](https://img.shields.io/badge/Code-GitHub-blue?logo=GitHub&logoColor=yellow)

The objective of this program is to be a content agreggator for Reddit submissions based on the arguments passed to the API.
Here as an example I'm using it to get daily submissions for the top 50 cryptocurrencies on CoinMarketCap.
So first it uses the CoinMarketCap API to get all the criptocurrencies listed on the website.
Then we filter the dataset to get only the top 50 highest marketcap coins.
Using the names from the coin dataset, we use the reddit PushShift API to get the submissions for each coin in the list. 
In this example I'm getting only 50 posts from each coin, but you may pass whatever number you want as long as it's supported by the reddit API.
The program writes a CSV with 'Coin name','Title','Link','Number of comments' for each submission in reddit for each coin.

In the future I intend to write an NLP algorithm to do a sentiment analysis on the content of the submissions, to get more relevant information from the posts.
