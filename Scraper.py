from bs4 import BeautifulSoup
import requests

	
def Google(q):
	page = requests.get("https://www.google.com/search?q={}".format(q))
	soup = BeautifulSoup(page.content, 'html.parser')
	message = ""
	results = soup.findAll("div", attrs={"class":"g"})
	for result in results:
		h3 = result.find("h3", attrs={"class":"r"}, recursive=True)
		if h3 != None:
			a = h3.find("a")
			txt = h3.text
			#remove images and news (change based on your language)
			if not txt.startswith("Εικόνες") and not txt.startswith("Ειδήσεις"):
				link = a.get("href")
				link = link.replace("/url?q=","") #remove useless URL stuff from the start
				link = link[:link.rfind("&sa=U")] #...and from the end
				message += "{}\n{}\n\n".format(txt,link)
				if len(message) > 1600: #discord can only send message up to 2000 characters
					break
	return message
	