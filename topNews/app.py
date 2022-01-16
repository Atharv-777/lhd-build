from urllib import request
from flask import Flask, render_template, request
import requests


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():

    url = "https://newsapi.org/v2/everything?q=Apple&from=2022-01-16&sortBy=popularity&apiKey="
    api="b48566b0966043be84c9c75bc2be375c"
    url += api
    request = requests.get(url)
    newsData = request.json()
    
    img = []
    title = []
    url = []
    for i in range(len(newsData['articles'][:6])):
        # newsList[i] = newsData['articles'][i]['author'], newsData['articles'][i]['title'], newsData['articles'][i]['description'], newsData['articles'][i]['urlToImage'], newsData['articles'][i]['url']
        img.append(newsData['articles'][i]['urlToImage'])
        title.append(newsData['articles'][i]['title'])
        url.append(newsData['articles'][i]['url'])
    print(newsData)
    return render_template('index.html', img=img, title=title, url=url)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)