#Importing all the functions to main

from ExtractTrain import training, output_list
from ExtractTest import test
from NaiveBayes import naivebayes_accuracy
from ExtractTrain import stop_words
from LogisticRegression import calculateaccuracy
from LogisticRegression import formequation

import sys



#Get the command line arguments

training_ham_folder=sys.argv[1]
training_spam_folder=sys.argv[2]
test_ham_folder=sys.argv[3]
test_spam_folder=sys.argv[4]

#print('************','Running Naive Bayes with out stop words', '***************')

weightvector,inputvector,positive,negative,negative_attribute_count,positive_attribute_count,wordlist_train,wordcount,train_output_list=training(training_ham_folder,training_spam_folder)
wordlist_test,wordpositions,output_list,test_attributelist=test(wordlist_train,test_ham_folder,test_spam_folder)


accuracy=naivebayes_accuracy(positive, negative, negative_attribute_count, positive_attribute_count, wordlist_train, wordcount, wordlist_test, wordpositions, output_list)

#print("******  Accuracy   *******")
print("\nNaive Bayes Accuracy:", accuracy*100)


#print('************','Running Logistic Regression with out stop words', '************')
Learning_Rate = 0.09
Lamda = 0.01
weight_matrix=formequation(inputvector, weightvector, train_output_list,0,15,Learning_Rate,Lamda)
logistic_accuracy=calculateaccuracy(weight_matrix,test_attributelist,output_list)


print("\nLogistic Regression Accuracy:",logistic_accuracy*100)

