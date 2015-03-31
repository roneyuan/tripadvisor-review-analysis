import re
import time
import collections
#import nltk
#nltk.download()


def review_sentiment_analysis(str_review, neg, pos, may_neg):

    score = 0

    for words in str_review:
        if words in pos:
            score = score + 1
        elif words in neg:
            score = score - 2
        elif words in may_neg:
            score = score - 1

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"


def classification(reviews):

    print(reviews[1])
    #bagsofwords = [collections.Counter(for txt in reviews)]

    #print(bagsofwords[9])


def main():

    negative_words = {}
    positive_words = {}
    may_neg = {}

    accurate = 0
    wrong = 0
    notsure = 0

    with open('negative-words.txt', 'r') as n:
        for line in n:
            negative_words[line.strip().lower()] = "negative"

    with open('positive-words.txt', 'r') as p:
        for line in p:
            positive_words[line.strip().lower()] = "positive"

    may_neg["not"] = "negative"
    may_neg["dont"] = "negative"
    may_neg["wasnt"] = "negative"
    may_neg["isnt"] = "negative"
    may_neg["arent"] = "negative"
    may_neg["werent"] = "negative"
    may_neg["didnt"] = "negative"
    may_neg["wont"] = "negative"
    may_neg["doesnt"] = "negative"
    may_neg["aint"] = "negative"
    may_neg["hasnt"] = "negative"
    may_neg["havent"] = "negative"

    with open('24kData.txt', 'r') as f:
        for line in f:
            line2 = re.split('\W+', line.lower())
            try:
                if "don" in line2:
                    if line2[line2.index("don") + 1] == "t":
                        line2[line2.index("don")] = "dont"
                elif "didn" in line2:
                    if line2[line2.index("didn") + 1] == "t":
                        line2[line2.index("didn")] = "didnt"
                elif "wasn" in line2:
                    if line2[line2.index("wasn") + 1] == "t":
                        line2[line2.index("wasn")] = "wasnt"
                elif "weren" in line2:
                    if line2[line2.index("weren") + 1] == "t":
                        line2[line2.index("weren")] = "werent"
                elif "ain" in line2:
                    if line2[line2.index("ain") + 1] == "t":
                        line2[line2.index("ain")] = "aint"
                elif "aren" in line2:
                    if line2[line2.index("aren") + 1] == "t":
                        line2[line2.index("aren")] = "arent"
                elif "doesn" in line2:
                    if line2[line2.index("doesn") + 1] == "t":
                        line2[line2.index("doesn")] = "doesnt"
                elif "won" in line2:
                    if line2[line2.index("won") + 1] == "t":
                        line2[line2.index("won")] = "wont"
                elif "isn" in line2:
                    if line2[line2.index("isn") + 1] == "t":
                        line2[line2.index("isn")] = "isnt"
                elif "hasn" in line2:
                    if line2[line2.index("hasn") + 1] == "t":
                        line2[line2.index("hasn")] = "hasnt"
                elif "haven" in line2:
                    if line2[line2.index("haven") + 1] == "t":
                        line2[line2.index("haven")] = "havent"
            except IndexError:
                print "Index Out of range"

            if review_sentiment_analysis(line2[1:], negative_words, positive_words, may_neg) == "positive":
                if line2[0] == "5":
                    accurate = accurate + 1
                else:
                    wrong = wrong + 1
            elif review_sentiment_analysis(line2[1:], negative_words, positive_words, may_neg) == "negative":
                if line2[0] == "1":
                    accurate = accurate + 1
                else:
                     wrong = wrong + 1
            elif review_sentiment_analysis(line2[1:], negative_words, positive_words, may_neg) == "neutral":
                notsure = notsure + 1

    print accurate
    print wrong
    print notsure
    per = accurate/24000.00
    print per


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))