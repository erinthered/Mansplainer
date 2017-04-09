# import nltk
# from nltk import pos_tag
# from nltk.tokenize import sent_tokenize, word_tokenize

import requests
<<<<<<< HEAD
import json 
import sys
=======
import json
>>>>>>> 72dbba66ffec30f964a3685253f327b63ac0eff9

WIKI_SUMMARY_URL = "https://simple.wikipedia.org/api/rest_v1/page/summary/{}?redirect=false"

manResponse = ""
startSentence = "Here, let me explain it to you."


def getSummaryFromWiki(query):
<<<<<<< HEAD
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

	
=======
    formattedURL = WIKI_SUMMARY_URL.format(query)
    wikiRequest = requests.get(formattedURL)
    httpBody = wikiRequest.json()

    if (wikiRequest.status_code >= 400):
        print("Error page not found")
        return None
    else:
        wikiExtract = httpBody["extract"]
        abbrevExtract = wikiExtract.split(".")[:2]
        print(abbrevExtract)
        return abbrevExtract


>>>>>>> 72dbba66ffec30f964a3685253f327b63ac0eff9
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



<<<<<<< HEAD
def main():
	query = sys.argv[1]
	summary = getSummaryFromWiki(query)
	print(summary)
=======
#def main():
#	query = "mountain"
#	summary = getSummaryFromWiki(query)
#	print(summary)
>>>>>>> 72dbba66ffec30f964a3685253f327b63ac0eff9


#if __name__ == '__main__':
#	main()
