import requests
import string
from bs4 import BeautifulSoup


def get_quote():
	url = input()
	r = requests.get(url)

	if r.status_code != 200:
		print("Invalid quote resource!")
	else:
		try:
			content = r.json()["content"]
			print(content)
		except KeyError:
			print("Invalid quote resource!")


def get_film_title():
	url = input()
	r = requests.get(url, headers={"accept-language": "en-US,en;q=0.9,uk;q=0.8,ru;q=0.7"})
	soup = BeautifulSoup(r.content, 'html.parser')

	if r.status_code != 200:
		print("Invalid movie page!")
	elif 'title' not in url.strip('/'):
		print("Invalid movie page!")
	else:
		film_info = {}
		title = soup.find('div',{'class': 'star-rating-widget'})['data-title']
		description = soup.find('div',{'class': 'summary_text'}).text.strip()
		film_info['title'] = title
		film_info['description'] = description
		print()
		print(film_info)


def save_article(name, url):
	list_of_marks = string.punctuation
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'html.parser')
	article_body = soup.find("div", {"class": "article__body"}).text.strip()

	title1_new = [letter for letter in name if letter not in list_of_marks]
	title1_new2 = ''.join(title1_new)
	title1_new3 = '_'.join(title1_new2.split())
	file_name = title1_new3 + ".txt"

	with open(f"file_name", 'wb') as f:
		f.write(article_body.encode("utf-8"))
	return file_name


def get_articles():
	url = "https://www.nature.com/nature/articles"
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'html.parser')

	articles = soup.find_all('article')
	articles_to_parse = []

	for article in articles:
		news_type = article.find('span', attrs={"data-test":"article.type"}).text.strip()
		if news_type == "News":
			articles_to_parse.append(article)

	return articles_to_parse


def parse_articles(articles):
	if articles:
		list_of_saved_articles = []
		for article in articles:
			article_data = article.find('a', attrs={"data-track-action":"view article"})
			article_title= article_data.text.strip()
			article_url = article_data.get('href')
			url2 = "https://www.nature.com" + article_url
			article_parsed = save_article(article_title, url2)
			list_of_saved_articles.append(article_parsed)
		return list_of_saved_articles
	else:
		return False


articles_parsed = parse_articles(get_articles())
if articles_parsed:
	print(f"Saved articles:  {sorted(articles_parsed)}")




##def get_articles():
##	url = "https://www.nature.com/nature/articles"
##	r = requests.get(url)
##	soup = BeautifulSoup(r.content, 'html.parser')
##
##	news = soup.find_all('span', attrs={"data-test":"article.type"})
##	titles = soup.find_all('a', attrs={"data-track-action":"view article"})
##
##	list_of_saved_articles = []
##	for new, title in zip(news, titles):
##                if new.text.strip() == 'News':
##                        article_title = title.text.strip()
##			article_link = title.get('href')
##			url2 = "https://www.nature.com" + article_link
##			article = save_article(article_title, url2)
##			list_of_saved_articles.append(article)
##
##	return list_of_saved_articles


##def get_articles():
##        list_of_saved_articles = []
##        url = "https://www.nature.com/nature/articles"
##        r = requests.get(url)
##        soup = BeautifulSoup(r.content, 'html.parser')
##
##        articles = soup.find_all('article')
##        articles_to_parse = []
##        
##        for article in articles:
##                news_type = article.find('span', attrs={"data-test":"article.type"}).text.strip()
##                if news_type == "News":
##                        article_data = article.find('a', attrs={"data-track-action":"view article"})
##                        article_title= article_data.text.strip()
##                        article_url = article_data.get('href')
##                        url2 = "https://www.nature.com" + article_url
##                        article_parsed = save_article(article_title, url2)
##                        list_of_saved_articles.append(article_parsed)
##
##        return list_of_saved_articles
