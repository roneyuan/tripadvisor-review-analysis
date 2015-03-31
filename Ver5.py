import re
import time


def review_sentiment_analysis(str_review, neg, pos):

    score = 0

    for words in str_review:
        if words in pos:
            score = score + 1
        elif words in neg:
            score = score - 1

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"


def analysis_for_neutral(str_review, classified_data):

    score = 0

    classfied_value = 0.0

    for words in str_review:
        classfied_value = classfied_value + classified_data[words]
        #print classfied_value

    #average = -53.823

    if classfied_value >= -53.823:
        return "positive"
    elif classfied_value < -53.823:
        return "negative"
    # elif classfied_value < -48.823 and classfied_value > -58.823:
    #     return "neutral"


    # if classfied_value >= -53.823 and classfied_value <= -53.823*2:
    #     score = score + 1
    # elif classfied_value > 53.823*2 and classfied_value <= 53.823*3:
    #     score = score + 2
    # elif classfied_value > 53.823*3 and classfied_value <= 53.823*4:
    #     score = score + 3
    # elif classfied_value < -53.823 and classfied_value >= -53.823*2:
    #     score = score - 1
    # elif classfied_value < -53.823*2 and classfied_value >= -53.823*3:
    #     score = score - 2
    # elif classfied_value < -53.823*3 and classfied_value >= -53.823*4:
    #     score = score - 3
    #
    # if score > 0:
    #     return "positive"
    # elif score < 0:
    #     return "negative"
    # else:
    #     return "neutral"


def classification(reviews):

    dict = {}
    value = 0.0
    for list in reviews:
        for words in list:

            if list[0] == "1":
                value = -0.0001
            elif list[0] == "5":
                value = 0.0001

            if words in dict:
                dict[words] = dict[words] + value
            else:
                dict[words] = value

    return dict


def main():

    comment = []
    rating = []

    with open('24kData.txt', 'r') as f:
        for line in f:
            line2 = re.sub("[^\w]", " ", line.lower()).split()

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
    negative_words["never"] = "negative"

    accurate = 0
    wrong = 0
    notsure = 0

    for list in comment:

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
        elif review_sentiment_analysis(list[1:], negative_words, positive_words) == "neutral":

            if analysis_for_neutral(list[1:], classified_data) == "positive":
                if list[0] == "5":
                    accurate = accurate + 1
                else:
                    wrong = wrong + 1
            elif analysis_for_neutral(list[1:], classified_data) == "negative":
                if list[0] == "1":
                    accurate = accurate + 1
                else:
                    wrong = wrong + 1
            elif analysis_for_neutral(list[1:], classified_data) == "neutral":
                notsure = notsure + 1

    print accurate
    print wrong
    print notsure
    per = accurate/24000.00
    print per


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))