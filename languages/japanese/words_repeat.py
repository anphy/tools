# coding: utf-8 
import time
import pandas as pd 
import numpy as np


    
class Card:
    def __init__(self, item):
        self.item = item

    def _set_familiar(self, level):
        self.item["familiar"] = level
        self.item["last_show"] = int(time.time())
        self.item["show_cnt"] += 1
        print("************************")

    def show(self,field):
        print("word: %s"%self.item[field])
        level = raw_input("familiar:")
        print("pronunce:%s"%self.item["pronounce"])
        print("english:%s"%self.item["english"])
        if level == "":
            level = 10
        self._set_familiar(int(level))
    
    def get(self):
        return self.item


class Deck:
    def __init__(self, filepath):
        self.path = filepath
        df = pd.read_csv(self.path)
        if "familiar" not in df:
            df["familiar"] = 0
        if "show_cnt" not in df:
            df["show_cnt"] = 0
        if "last_show" not in df:
            df["last_show"] = 0
        timeNow = int(time.time())
        df["score"] = df["show_cnt"]*df["familiar"]/np.maximum(np.log(timeNow - df["last_show"]),1)
        df = df.sort_values(by=["score", "id"], ascending=True)
        self.df = df
    
    def start(self):
        try:
            print("start roll up...\n")
            for index, row in self.df.iterrows():
                card = Card(row)
                card.show("japanese")
                self.df.loc[index] = card.get()
        except Exception as inst:
            print("error:")
            print(inst)
        finally:
            self.save()
            print("exit")

    def save(self):
        print("save to:%s"%self.path)
        self.df.to_csv(self.path, columns=["id","japanese","pronounce","english","familiar","show_cnt","last_show","score"], index=False)


if __name__ == "__main__":
    path = "./nihongo.csv"
    deck = Deck(path)
    deck.start()