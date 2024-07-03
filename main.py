from flask import Flask ,render_template

from newsapi import NewsApiClient

app= Flask(__name__)

@app.route('/')
def home():

    api_key="6594b1d2554649fe933ffd37be00e1ea"

    newsapi = NewsApiClient(api_key)

    top_headling = newsapi.get_top_headlines(sources='bbc-news')

    all_article = newsapi.get_everything(sources="bbc-news")

    t_articles= top_headling['articles']

    a_article = all_article['articles']

    news=[]
    desc=[]
    img=[]
    p_date=[]
    url=[]
    
    for i in range(len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])


        content = zip(news,desc,img,p_date,url)


    news_all = []
    desc_all = []
    img_all = []
    p_data_all = []
    url_all = []

    for j in range(len(a_article)):
        j_article = a_article[j]

        news_all.append(j_article['title'])
        desc_all.append(j_article['description'])
        img_all.append(j_article['urlToImage'])
        p_data_all.append(j_article['publishedAt'])
        url_all.append(j_article['url'])
        
        all = zip(news_all,desc_all,img_all,p_data_all,url_all)

    return render_template("index.html",contents=content,al=all)

if __name__ == "__main__":
    app.run(debug=True)
