import re
import time


def review_sentiment_analysis(str_review, neg, pos, may_neg, classified_data):

    score = 0

    classfied_value = 0.0
    #print str_review
    for words in str_review:
        classfied_value = classfied_value + classified_data[words]
        if words in pos:
            score = score + 2
        elif words in neg:
            score = score - 2
        elif words in may_neg:
            if classified_data[words] >= 0:
                score = score + 1
            else:
                score = score - 1


    #classfied_value2 = classfied_value2 + classfied_value

    #print classfied_value

    if classfied_value >= -0.004026083:
        score = score + 1
    elif classfied_value < -0.0040260803:
        score = score - 1

    # if classfied_value > 0 and classfied_value <= 100:
    #     score = score + 2
    # elif classfied_value > 100 and classfied_value <= 500:
    #     score = score + 3
    # elif classfied_value > 500:
    #     score = score + 4
    # elif classfied_value < 0 and classfied_value >= -100:
    #     score = score - 2
    # elif classfied_value < -100 and classfied_value >= -500:
    #     score = score -3
    # elif classfied_value < -500:
    #     score = score - 4

    if score > 0:
        return "positive", classfied_value
    elif score < 0:
        return "negative", classfied_value
    else:
        return "neutral", classfied_value


def classification(reviews):

    dict = {}
    value = 0.0
    for list in reviews:
        for words in list:
            #print list[0]
            if list[0] == "1":
                value = -0.0001
            elif list[0] == "5":
                value = 0.0001

            if words in dict:
                dict[words] = dict[words] + value
            else:
                dict[words] = value

    # Find average value
    average = 0
    for key in dict:
        average = average + dict[key]
    average = average/24000

    #print average

    return dict


def main():

    comment = []

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
            comment.append(line2)

    classified_data = classification(comment)

    negative_words = {}
    positive_words = {}
    may_neg = {}

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

    accurate = 0
    wrong = 0
    notsure = 0
    average = 0

    for list in comment:
        if review_sentiment_analysis(list[1:], negative_words, positive_words, may_neg, classified_data)[0] == "positive":
            if list[0] == "5":
                accurate = accurate + 1
            else:
                wrong = wrong + 1
        elif review_sentiment_analysis(list[1:], negative_words, positive_words, may_neg, classified_data)[0] == "negative":
            if list[0] == "1":
                accurate = accurate + 1
            else:
                wrong = wrong + 1
        elif review_sentiment_analysis(list[1:], negative_words, positive_words, may_neg, classified_data)[0] == "neutral":
            notsure = notsure + 1

        #average = average + average
        average = average + review_sentiment_analysis(list[1:], negative_words, positive_words, may_neg, classified_data)[1]
        #print average
        #average = average + average
        #print average

    print average/24000.00
    print accurate
    print wrong
    print notsure
    per = accurate/24000.00
    print per


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))