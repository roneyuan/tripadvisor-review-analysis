import re
import time


def review_sentiment_analysis(str_review, neg, pos):
    #print str_review

    #negative_words = {}
    #positive_words = {}

    # neg = []
    # pos = []
    # negWord = []
    # posWord = []
    #
    #
    # with open('negative-words.txt', 'r') as n:
    #     for line in n:
    #         neg.append(line.strip())
    #         negWord.append("negative")
    #         #print line
    #
    # with open('positive-words.txt', 'r') as p:
    #     for line in p:
    #         pos.append(line.strip())
    #         posWord.append("postive")

    #negative_words = dict(zip(neg, negWord))
    #positive_words = dict(zip(pos, posWord))

    score = 0

    for words in str_review:
        if words in pos:
            score = score + 1
        elif words in neg:
            score = score - 1


    #print score

    if score > 0:
        #print "postive" + ": " + rating
        return "positive"
    elif score < 0:
        return "negative"
        #print "negative" + ": " + rating
    else:
        return "netrual"
        #print "neutral" + ": " + rating


    # if str_review in neg:
    #     print "negative"
    # elif str_review in pos:
    #     print "positive"
    # else:
    #     print "Skip"

    #print neg[9]
    #print pos[9]






def main():

    #f = open('24kData.txt', 'r')
    comment = []
    rating = []

    with open('24kData.txt', 'r') as f:
        for line in f:
            line2 = re.sub("[^\w]", " ", line.lower()).split()
            #print line2
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
            comment.append(line2)
            #rating.append(line2[0])
    #print comment[2][1:]
    #comment = comment[1:]
    #print comment[0]

    #print comment[9]
    negative_words = {}
    positive_words = {}


    #neg = []
    #pos = []
    #negWord = []
    #posWord = []

    with open('negative-words.txt', 'r') as n:
        for line in n:
            negative_words[line.strip().lower()] = "negative"

    with open('positive-words.txt', 'r') as p:
        for line in p:
            positive_words[line.strip().lower()] = "positive"

    negative_words["not"] = "negative"
    negative_words["dont"] = "negative"
    negative_words["wasnt"] = "negative"
    negative_words["isnt"] = "negative"
    negative_words["arent"] = "negative"
    negative_words["werent"] = "negative"
    negative_words["didnt"] = "negative"
    negative_words["wont"] = "negative"
    negative_words["doesnt"] = "negative"
    negative_words["aint"] = "negative"
    negative_words["hasnt"] = "negative"
    negative_words["havent"] = "negative"

    #print negative_words
    #print positive_words

    # with open('negative-words.txt', 'r') as n:
    #     for line in n:
    #         neg.append(line.strip())
    #         negWord.append("negative")
    #
    # with open('positive-words.txt', 'r') as p:
    #     for line in p:
    #         pos.append(line.strip())
    #         posWord.append("postive")

    # use for loop here
    accurate = 0
    wrong = 0
    notsure = 0
    for list in comment:
        #for words in list:
            #print words
        #print review_sentiment_analysis(list[1:])
        if review_sentiment_analysis(list[1:], negative_words, positive_words) == "positive":
            #match = 5
            if list[0] == "5":
                accurate = accurate + 1
            else:
                wrong = wrong + 1
        elif review_sentiment_analysis(list[1:], negative_words, positive_words) == "negative":
            #match = 1
            if list[0] == "1":
                accurate = accurate + 1
            else:
                wrong = wrong + 1
        elif review_sentiment_analysis(list[1:], negative_words, positive_words) == "netrual":
            notsure = notsure + 1


    print accurate
    print wrong
    print notsure
    per = accurate/24000.00
    print per


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))