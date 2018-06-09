'''

Same as Extract train but deals with test

*****************To extract ham and spam from test set with stop words**************

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
        with open(files, 'r') as my_file:
            try:
                s = my_file.read()
            except:
                pass
            data.append(s);
    return data;


def getarrayintorequired_negaive(list, position):
    row_count = 1;
    row_value_temp = []
    for each_data in list:
        words_inlist = each_data.split()
        row_value_temp = []

        attribute_temp_value = []
        if row_count > 1:
            Attribute_list.insert(row_count - 1, attribute_temp_value)
            row_values.insert(row_count - 1, row_value_temp)
        row_itteration = 0;
        for words in words_inlist:

            if (len(words) <= 1) or (words == 'Subject:'):
                continue

            try:

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

                wordlist.insert(position, words)
                wordcount.insert(position, 1);
                positive_attribute_count.insert(position, 0);
                negative_attribute_count.insert(position, 1);
                row_values[row_count - 1].insert(row_itteration, words)
                Attribute_list[row_count - 1].insert(row_itteration, 1);
                position = position + 1;
                row_itteration = row_itteration + 1

        output_list.insert(row_count, "FALSE")
        row_count = row_count + 1;

    return len(list) + 1, position


def getarrayintorequired_positive(list, row_count, position):
    row_value_temp = []
    for each_data in list:
        words_inlist = each_data.split()
        row_value_temp = []

        attribute_temp_value = []
        if row_count > 1:
            Attribute_list.insert(row_count - 1, attribute_temp_value)
            row_values.insert(row_count - 1, row_value_temp)
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


def formrealattributes(wordlist_test):
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
        for word in wordlist_test:
            weightvector[i].insert(j, 0)
            try:
                index = row_values[i].index(word)
                value = Attribute_list[i][index]
                inputvector[i].insert(j, value)
            except:
                inputvector[i].insert(j, 0)
            j = j + 1
        i = i + 1
        j = 0
    return weightvector, inputvector


def test(wordlist_test, test_ham_folder, test_spam_folder):

    spam_list = Getfilesinfolder(test_spam_folder);
    ham_list = Getfilesinfolder(test_ham_folder);

    spam_array = getfilesintoarray(spam_list)
    ham_array = getfilesintoarray(ham_list)

    row_count, position = getarrayintorequired_negaive(spam_array, 0)
    getarrayintorequired_positive(ham_array, row_count, position)
    weightvector, inputvector = formrealattributes(wordlist_test)

    return row_values, Attribute_list, output_list, inputvector
'''
    print('\n*******************')
    print('\noutput_list\n', output_list)
    print('\nattribute list\n', Attribute_list)
    print('\nnegative attr count\n', negative_attribute_count)
    print('\nwordlist\n', wordlist)
    print('\nword count\n', wordcount)
    print('\nword_postn\n', word_position)
    print('\nposition\n', position)
    print('\npositive array row\n', positive_array_row)
    print('\nrow_count\n', row_count)
    print('\nrow values\n', row_values)
    print('\ntotal\n', total)
    print('\nnegative\n', negative)
    print('\npositive\n', positive)
    print('\nweigt matrix', weightmatrix)
    print('\ninput matrix', inputmatrix)
    print('\nlen(wc)\n', len(wordcount))
'''