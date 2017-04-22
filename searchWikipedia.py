import requests
import json
import sys


WIKI_SUMMARY_URL = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&continue=&titles={}&redirects=1&exsentences=3&exlimit=4&explaintext=1&exsectionformat=plain"
#https://simple.wikipedia.org/api/rest_v1/page/summary/{}?redirect=false
#"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={}&exsentences=3&explaintext=1"

manResponse = ""
startSentence = "Here, let me explain it to you."


def getSummaryFromWiki(query):
	print(query)
	formattedURL = WIKI_SUMMARY_URL.format(query)
	print(formattedURL)
	wikiRequest = requests.get(formattedURL)
	httpBody = wikiRequest.json()
	pageData = httpBody["query"]["pages"]
	if ("-1" in pageData):
		return "Wow that's really complex. I'm sure if I tried to explain this too much blood would go to your brain and not your lady parts" 
	else:
		
		queryResult = pageData.values()
		resultList = list(queryResult)
		extract = resultList[0]["extract"]
		print(type(extract))
		'''delete this!! dont want to do IO'''
		resText = open("./res.txt", "wb")
		resText.write(extract.encode("utf8"))
		''''''
		resText.close()
		return extract
		# abbrevExtract = extra.split(".")[:3]
		# extractString = abbrevExtract[0] + "." + abbrevExtract[1] + "." + abbrevExtract[2] + "."
		# return extractString


def main():
	query = sys.argv[1]
	summary = getSummaryFromWiki(query)
	#print(summary)


if __name__ == '__main__':
	main()
