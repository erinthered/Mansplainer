import requests
import json 

WIKI_SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/{}?redirect=false"

manResponse = ""

#@Mansplain.route("/", methods=["POST"])
def getSummaryFromWiki(query):
	formattedURL = WIKI_SUMMARY_URL.format(query)
	wikiRequest = requests.get(formattedURL)
	httpBody = wikiRequest.json()
	
	if (wikiRequest.status_code >= 400):
		print("Error page not found")
		return None
	else:
		wikiExtract = httpBody["extract"]
		return wikiExtract

def splitSummary(wikiSummary):
	return wikiSummary.split(".")

def main():
	query = "mountain"
	summary = getSummaryFromWiki(query)
	print(summary)


if __name__ == '__main__':
	main()