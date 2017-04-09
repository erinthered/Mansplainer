import nltk 
from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize

import requests
import json 

WIKI_SUMMARY_URL = "https://simple.wikipedia.org/api/rest_v1/page/summary/{}?redirect=false"

manResponse = ""
startSentence = "Here, let me explain it to you."


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

	
def getTokenizedWord(sentence):
	return word_tokenize(sentence)

def getTaggedText(text):
	tokenizedText = getTokenizedWord(text)
	tagged = pos_tag(tokenizedText)
	return tagged

""""""
def getNounPhrase(taggedText):
	grammar = '''NP: {<JJ>*<NNP>*<NN>?}'''
	grammar2 = '''NP:	{<DT>?<JJ>?<NN>}'''
	cp = nltk.RegexpParser(grammar2)
	result = cp.parse(taggedText)
	leaves = []
	for subtree in result.subtrees(filter=lambda x: x.label()=="NP"):
		leaves.append(subtree.leaves())
	return leaves



def main():
	query = "mountain"
	summary = getSummaryFromWiki(query)

	tagSum = getTaggedText(summary)
	print (tagSum)

	nounPhr = getNounPhrase(tagSum)
	for leaf in nounPhr:
		print(leaf)


if __name__ == '__main__':
	main()