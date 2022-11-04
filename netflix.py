file = "./netflix/ViewingActivity.csv"
import json
with open(file,'r',encoding="utf-8")  as f:
        f = f.read().splitlines()

for x in range(len(f)):
    f[x] = f[x].split(",")

dico = {}

class Manager:
    def __init__(self,profile,started,duration,title,bookmark,latest_bookmark):
        self.profile = profile
        self.started = started
        self.duration = duration
        self.bookmark = bookmark
        self.latest_bookmark = latest_bookmark
        self.type = "type"
        self.title = title
        self.content = None
        toR = ["Saison","Partie"]
        if "pisode" in self.title:
            ver = False
            for x in toR:
                if x in self.title:
                    to_cut = self.title.index(x)
                    ver = True
            if ver == True:
                crop =  self.title[:to_cut]
                self.type = "Shows"
                self.content = Show(profile,started,duration,title,bookmark,latest_bookmark).__dict__
                if crop not in dico:
                    dico[crop] = {}
                dico[crop].update({self.content["ep"]:self.content})
            else:
                self.content = item(profile,started,duration,title,bookmark,latest_bookmark).__dict__
                dico[self.title]  = self.content
        else:
            self.type = "Movies"
            self.content = item(profile,started,duration,title,bookmark,latest_bookmark).__dict__
            dico[self.title]  = self.content
        

class item:
    def __init__(self,profile,started,duration,title,bookmark,latest_bookmark):
        self.profile = profile
        self.started = started
        self.duration = duration
        self.bookmark = bookmark
        self.latest_bookmark = latest_bookmark
        self.type = "type"
        self.title = title

class Show(item):
    def __init__(self, profile, started, duration, title, bookmark, latest_bookmark):
        super().__init__(profile, started, duration, title, bookmark, latest_bookmark)
        self.ep = self.title[self.title.index("Épisode"):self.title.index(")")]

f.sort()
for toRemove in f:
    if "(Bande-annonce)" not in toRemove[4]:
        if len(toRemove[5]) ==0:
            item_var = Manager(toRemove[0],toRemove[1],toRemove[2],toRemove[4],toRemove[8],toRemove[9])
   
print("break")
  
with open("datas_netflix_treated.json", "w",encoding="utf-8") as f:
    json.dump(dico,f,indent=4)

print("break")
