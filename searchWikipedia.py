# import nltk 
# from nltk import pos_tag
# from nltk.tokenize import sent_tokenize, word_tokenize

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
		return ["Wow that's really complex topic, honey."]
	else:
		wikiExtract = httpBody["extract"]
		abbrevExtract = wikiExtract.split(".")[:2]
		print(abbrevExtract)			
		return abbrevExtract

	
# def getTokenizedWord(sentence):
# 	return word_tokenize(sentence)

# def getTaggedText(text):
# 	tokenizedText = getTokenizedWord(text)
# 	tagged = pos_tag(tokenizedText)
# 	return tagged

# """"""
# def getNounPhrase(taggedText):
# 	grammar = '''NP: {<JJ>*<NNP>*<NN>?}'''
# 	grammar2 = '''NP:	{<DT>?<JJ>?<NN>}'''
# 	cp = nltk.RegexpParser(grammar2)
# 	result = cp.parse(taggedText)
# 	leaves = []
# 	for subtree in result.subtrees(filter=lambda x: x.label()=="NP"):
# 		leaves.append(subtree.leaves())
# 	return leaves



def main():
	query = sys.argv[1]
	summary = getSummaryFromWiki(query)
	print(summary)


if __name__ == '__main__':
	main()