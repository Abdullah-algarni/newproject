from googlesearch import *
word=input("enter the dork : ")
for ulr in search(word, stop=10):
    print(ulr)