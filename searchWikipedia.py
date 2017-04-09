import requests
import json
import sys


WIKI_SUMMARY_URL = "https://simple.wikipedia.org/api/rest_v1/page/summary/{}?redirect=false"

manResponse = ""
startSentence = "Here, let me explain it to you."


def getSummaryFromWiki(query):
	formattedURL = WIKI_SUMMARY_URL.format(query)
	wikiRequest = requests.get(formattedURL)
	httpBody = wikiRequest.json()

	if (wikiRequest.status_code >= 400):
		return ["Wow that's a really complex topic, honey. I don't think you can handle it, why don't you try something simpler?"]
	else:
		wikiExtract = httpBody["extract"]
		abbrevExtract = wikiExtract.split(".")[:2]
		print(abbrevExtract)
		return abbrevExtract

def main():
	query = sys.argv[1]
	summary = getSummaryFromWiki(query)
	print(summary)


if __name__ == '__main__':
	main()
