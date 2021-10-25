#coding: utf-8
from random import shuffle

def split_dict_to_app():
    with open("./dict.txt","r") as f:
        lines = f.readlines()
    words = [line.split(",")[0]+"\n" for line in lines]
    shuffle(words)
    shuffle(words)
    length = len(words)
    offset = 0
    while 1:
        end = (offset + 1)*5000
        if end > length:
            end = length
        vocabs = words[offset*5000:end]
        with open("./%d.txt"%offset, "wb") as f:
            f.writelines(vocabs)
        if end >= length:
            break
        offset = offset + 1

if __name__ == "__main__":
    split_dict_to_app()
    