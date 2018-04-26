import sys
import string
import math

id_set = set()
pos_set = set()
neg_set = set()
fake_set = set()
true_set = set()
vocabulary = set()
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "so", "than", "too", "very", "can", "will", "just", "should", "now"]


def read_input():

    fin = open(sys.argv[1],'r')
    lines = fin.readlines()

    global id_set
    global pos_set
    global neg_set
    global fake_set
    global true_set
    global vocabulary

    pos_count = dict()
    neg_count = dict()
    true_count = dict()
    fake_count = dict()

    for line in lines:
        line = line.strip("\n")
        line = line.replace("'","")
        line = line.replace("-", "")
        for p in string.punctuation:
            line = line.replace(p, ' ')
        line = line.lower()

        line = line.split(" ")

        if line[0] != ' ':
            id_set.add(line[0])

        if line[1] == 'fake':
            fake_set.add(line[0])
        if line[1] == 'true':
            true_set.add(line[0])
        if line[2] == 'pos':
            pos_set.add(line[0])
        if line[2] == 'neg':
            neg_set.add(line[0])

        for j in range(3,len(line)):
            if line[j] != '' and line[j] not in stopwords:
                vocabulary.add(line[j])

                if line[1] == 'fake':
                    try:
                        fake_count[line[j]] += 1
                    except KeyError:
                        fake_count[line[j]] = 1

                if line[1] == 'true':
                    try:
                        true_count[line[j]] += 1
                    except KeyError:
                        true_count[line[j]] = 1

                if line[2] == 'pos':
                    try:
                        pos_count[line[j]] += 1
                    except KeyError:
                        pos_count[line[j]] = 1

                if line[2] == 'neg':
                    try:
                        neg_count[line[j]] += 1
                    except KeyError:
                        neg_count[line[j]] = 1

    fin.close()
    return fake_count, true_count, pos_count, neg_count


def compute_prob():
    fake_count, true_count, pos_count, neg_count = read_input()
    fo = open('nbmodel.txt', 'w+')

    prior_pos = math.log(len(pos_set)) - math.log(len(id_set))
    prior_neg = math.log(len(neg_set)) - math.log(len(id_set))
    prior_fake = math.log(len(fake_set)) - math.log(len(id_set))
    prior_true = math.log(len(true_set)) - math.log(len(id_set))

    fo.write("%f\n" % prior_pos)
    fo.write("%f\n" % prior_neg)
    fo.write("%f\n" % prior_fake)
    fo.write("%f\n" % prior_true)

    # Probability calculation for positive
    sum_pos = sum(pos_count.values())
    for word in vocabulary:
        try:
            prob = math.log((pos_count[word] + 1)) - math.log(sum_pos + len(vocabulary))
        except KeyError:
            prob = math.log(1) - math.log(sum_pos + len(vocabulary))
        fo.write("positive | " + word + " | %f\n" % prob)

    # Probability calculation for negative
    sum_neg = sum(neg_count.values())
    for word in vocabulary:
        try:
            prob = math.log((neg_count[word] + 1)) - math.log(sum_neg + len(vocabulary))
        except KeyError:
            prob = math.log(1) - math.log(sum_neg + len(vocabulary))
        fo.write("negative | " + word + " | %f\n" % prob)

    # Probability calculation for fake
    sum_fake = sum(fake_count.values())
    for word in vocabulary:
        try:
            prob = math.log((fake_count[word] + 1)) - math.log(sum_fake + len(vocabulary))
        except KeyError:
            prob = math.log(1) - math.log(sum_fake + len(vocabulary))
        fo.write("fake | " + word + " | %f\n" % prob)

    # Probability calculation for true
    sum_true = sum(true_count.values())
    for word in vocabulary:
        try:
            prob = math.log((true_count[word] + 1)) - math.log(sum_true + len(vocabulary))
        except KeyError:
            prob = math.log(1) - math.log(sum_true + len(vocabulary))
        fo.write("true | " + word + " | %f\n" % prob)


def main():
    compute_prob()


if __name__ == '__main__':
    main()