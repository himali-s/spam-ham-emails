'''

***********To extract ham and spam from training set------with stop words***************

'''


import os
from test.test_trace import my_file_and_modname
from _csv import Error


output_list = [];
Attribute_list = [[]];
negative_attribute_count = []
positive_attribute_count = []
wordlist = [];
wordcount = [];
word_position = [];
position = 0;
positive_array_row = [];
row_count = 0;
Unwanted_words = {'-', ':', ',', '.', '/'}
row_values = [[]]



#To check for the folder in the path
def Getfilesinfolder(path):
    list = []
    for dir_entry in os.listdir(path):
        dir_entry_path = os.path.join(path, dir_entry)
    
        if os.path.isfile(dir_entry_path):
        
            list.append(dir_entry_path)
    
    return list;


def getfilesintoarray(list):
    data = []
    for files in list:
    #now opening  the  files in the list , reading it and putting the contents in the array
        with open(files, 'r') as my_file:
            try:
                s = my_file.read()
            except:
                pass
            data.append(s);
    # print('Reading Data from the file', data[0])
    return data;


def getarrayintorequired_negaive_train(list, position):
    '''To form bag of words for spam'''
    row_count = 1;
    row_value_temp = []
    for each_data in list:
        #each_data is each mail as separate and words_inlist is array of words in particular mail
        words_inlist = each_data.split()
        
        row_value_temp = []
        row_values.insert(row_count - 1, row_value_temp)
        
        attribute_temp_value = []
        if row_count > 1:
            Attribute_list.insert(row_count - 1, attribute_temp_value)
        row_itteration = 0;		
        for words in words_inlist:

            if (len(words) <= 1) or (words == 'Subject:'):
                continue

            try:
            #finds the index and increments the repsective counts
                index_location = wordlist.index(words)
                negative_attribute_count[index_location] = negative_attribute_count[index_location] + 1
                wordcount[index_location] = wordcount[index_location] + 1
                try:
                    row_index = row_values[row_count - 1].index(words)
                    Attribute_list[row_count - 1][row_index] = Attribute_list[row_count - 1][row_index] + 1
                except:
                    row_values[row_count - 1].insert(row_itteration, words)
                    Attribute_list[row_count - 1].insert(row_itteration, 1);
                    row_itteration = row_itteration + 1
            except:
                '''Wordlist consists of all words and wordcount has count of all words present. '''
                wordlist.insert(position, words)
                wordcount.insert(position, 1);
                '''Since this function is for spam, insert 1 for negative attribute count'''
                positive_attribute_count.insert(position, 0);
                negative_attribute_count.insert(position, 1);			#stores count of distinct words as they a
                row_values[row_count - 1].insert(row_itteration, words)
                Attribute_list[row_count - 1].insert(row_itteration, 1);
                position = position + 1;									#num of distinct words
                row_itteration = row_itteration + 1
        '''Output list has either True or False depends on wheter it is ham or spam'''
        output_list.insert(row_count, "FALSE")
        row_count = row_count + 1;						

    return len(list) + 1, position


def getarrayintorequired_positive_train(list, row_count, position):
    '''Bag of words for ham'''
    row_value_temp = []
    for each_data in list:
        words_inlist = each_data.split()
        row_value_temp = []

        row_values.insert(row_count - 1, row_value_temp)

        attribute_temp_value = []
        if row_count > 1:
            Attribute_list.insert(row_count - 1, attribute_temp_value)
        row_itteration = 0;
        for words in words_inlist:

            if (len(words) <= 1) or (words == 'Subject:'):
                continue

            try:
                index_location = wordlist.index(words)
                positive_attribute_count[index_location] = positive_attribute_count[index_location] + 1
                wordcount[index_location] = wordcount[index_location] + 1
                try:
                    row_index = row_values[row_count - 1].index(words)
                    Attribute_list[row_count - 1][row_index] = Attribute_list[row_count - 1][row_index] + 1
                except:
                    row_values[row_count - 1].insert(row_itteration, words)
                    Attribute_list[row_count - 1].insert(row_itteration, 1);
                    row_itteration = row_itteration + 1
            except:

                wordlist.insert(position, words)
                wordcount.insert(position, 1);
                positive_attribute_count.insert(position, 1);
                negative_attribute_count.insert(position, 0);
                row_values[row_count - 1].insert(row_itteration, words)
                Attribute_list[row_count - 1].insert(row_itteration, 1);
                position = position + 1;
                row_itteration = row_itteration + 1

        output_list.insert(row_count, "TRUE")
        row_count = row_count + 1;


def formrealattributes_train():

    '''Here form a matrix with respect to the extracted values with that position so that in future , if u can find the position, then it will be easy
    to get the count values for calcualtion'''

    inputvector = [[]]
    weightvector = [[]]
    i = 0
    j = 0
    for row in Attribute_list:
        if i >= 1:
            samplematrix = []
            weightvector.insert(i, samplematrix)
            samplevector = []
            inputvector.insert(i, samplevector)
        for word in wordlist:
            weightvector[i].insert(j, 0)
            try:
                index = row_values[i].index(word)
                value = Attribute_list[i][index];
                inputvector[i].insert(j, value);
            except:
                inputvector[i].insert(j, 0)
            j = j + 1;
        i = i + 1;
        j = 0;
    return weightvector, inputvector




def training(training_ham_folder, training_spam_folder):
    '''Get all the file names with full path in a list'''
    spam_list = Getfilesinfolder(training_spam_folder)
    ham_list = Getfilesinfolder(training_ham_folder)

    '''Now read each file in the list and extract the data'''
    spam_array = getfilesintoarray(spam_list)
    ham_array = getfilesintoarray(ham_list)

    '''Look for spam data and its positions'''
    row_count, position = getarrayintorequired_negaive_train(spam_array, 0)
    negative = len(Attribute_list)
    getarrayintorequired_positive_train(ham_array, row_count, position)
    total = len(Attribute_list)
    positive = total - negative
    weightmatrix, inputmatrix = formrealattributes_train()

    '''Now return all the count, matrix values to the main'''
    return weightmatrix, inputmatrix, positive, negative, negative_attribute_count, positive_attribute_count, wordlist, wordcount, output_list



'''

****Parse the stop words text file ***********

'''
#from ExtractTrain import wordlist

def stop_words(stop_wrords_file):
    stop_words_list=[]
    words_list=[]
    with open(stop_wrords_file,'r') as my_file:
                try:
                    s=my_file.read()
                    words_list=s.split()
                    
                    for each_word in wordlist:
                        stop_words_list.append(each_word)
                except:
                    pass
    return words_list