# Naive-Bayes-Classifier
A Naive Bayes classifier for categorizing Hotel Reviews as True/Fake and Positive/Negative

## Overview
A naive Bayes classifier to identify hotel reviews as either true or fake, and either positive or negative using the word tokens as features for classification.

## Data
A set of training and development data is uploaded contatining the following files:

1) train-labeled.txt containing labeled training data with a single training instance (hotel review) per line (total 960 lines). The first 3 tokens in each line are:
  a) unique 7-character alphanumeric identifier
  b) label True or Fake
  c) label Pos or Neg
  These are followed by the text of the review.
  
2) dev-text.txt with unlabeled development data, containing just the unique identifier followed by the text of the review (total 320 lines).

3) dev-key.txt with the corresponding labels for the development data, to serve as an answer key.

## Programs
It contains two programs: nblearn.py that learns a naive Bayes model from the training data, and nbclassify.py that uses model to classify new data. 

The learning program is invoked in the following way:
```
> python nblearn.py train-labeled.txt
```
The argument is a single file containing the training data; the program learns a naive Bayes model, and writes the model parameters to a file called nbmodel.txt. 

The classification program will be invoked in the following way:
```
> python nbclassify.py dev-text.txt
```
The argument is a single file containing the test data file; the program reads the parameters of a naive Bayes model from the file nbmodel.txt, classify each entry in the test data, and writes the results to a text file called nboutput.txt in the same format as the answer key (dev-key.txt).

## Results on test data
Neg 0.94 0.94 0.94
True 0.88 0.84 0.86
Pos 0.94 0.94 0.94
Fake 0.85 0.89 0.87
Mean F1: 0.9031

{
'Neg': {'fp': 9, 'fn': 9, 'tp': 151}, 
'True': {'fp': 18, 'fn': 26, 'tp': 134}, 
'Pos': {'fp': 9, 'fn': 9, 'tp': 151}, 
'Fake': {'fp': 26, 'fn': 18, 'tp': 142}
}

## Accuracy
The model is 90.31% accurate in classifying test data calculated using above F1 measure.

