#! python

def listToString(list):
    listString = ""
    for str in list[:-1]:
        listString += (str+", ")
    listString += ("and "+list[-1])
    print(listString)

spam = ['apples', 'bananas', 'tofu', 'cats']
listToString(spam)
