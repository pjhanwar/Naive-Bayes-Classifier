import sys
import string
from decimal import *

stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "so", "than", "too", "very", "can", "will", "just", "should", "now"]


def read_model():
    pos_dict = dict()
    neg_dict = dict()
    true_dict = dict()
    fake_dict = dict()

    fin = open('nbmodel.txt','r')
    lines = fin.readlines()
    for index,line in enumerate(lines):
        line = line.strip("\n")
        if index == 0:
            prior_pos = Decimal(line)

        elif index == 1:
            prior_neg = Decimal(line)

        elif index == 2:
            prior_fake = Decimal(line)

        elif index == 3:
            prior_true = Decimal(line)

        else:
            line = line.split(" | ")
            if line[0] == 'positive':
                pos_dict[line[1]] = Decimal(line[2])
            elif line[0] == 'negative':
                neg_dict[line[1]] = Decimal(line[2])
            elif line[0] == 'true':
                true_dict[line[1]] = Decimal(line[2])
            elif line[0] == 'fake':
                fake_dict[line[1]] = Decimal(line[2])

    fin.close()
    return prior_pos, prior_neg, prior_fake, prior_true, pos_dict, neg_dict, true_dict, fake_dict


def naive_bayes():
    prior_pos, prior_neg, prior_fake, prior_true, pos_dict, neg_dict, true_dict, fake_dict = read_model()

    ft = open(sys.argv[1],'r')
    fo = open("nboutput.txt",'w+')
    lines = ft.readlines()

    for line in lines:
        tline = line
        output = ""
        pos_val = prior_pos
        neg_val = prior_neg
        true_val = prior_true
        fake_val = prior_fake

        tline = tline.strip("\n")
        tline = tline.split(" ")
        id = tline[0]
        output += id

        line = line.strip("\n")
        line = line.replace("'", "")
        line = line.replace("-", "")
        for p in string.punctuation:
            line = line.replace(p, ' ')
        line = line.lower()
        line = line.split(" ")

        for j in range(1,len(line)):
            if line[j] not in stopwords:
                if line[j] in pos_dict:
                    pos_val += Decimal(pos_dict[line[j]])
                if line[j] in neg_dict:
                    neg_val += Decimal(neg_dict[line[j]])
                if line[j] in true_dict:
                    true_val += Decimal(true_dict[line[j]])
                if line[j] in fake_dict:
                    fake_val += Decimal(fake_dict[line[j]])

        if true_val > fake_val:
            output += " True"
        else:
            output += " Fake"

        if pos_val > neg_val:
            output += " Pos"
        else:
            output += " Neg"

        fo.write(output + "\n")


def main():
    naive_bayes()


if __name__ == '__main__':
    main()