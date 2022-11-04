
class Manager:
    def __init__(self,profile,started,duration,title,bookmark,latest_bookmark):
        self.profile = profile
        self.started = started
        self.duration = duration
        self.bookmark = bookmark
        self.latest_bookmark = latest_bookmark
        self.title = title
        self.content = None


        toR = ["Saison","Partie"]
        if "pisode" in self.title:
            to_cut = 0
            ver = False
            for x in toR:
                if x in self.title:
                    to_cut = self.title.index(x)
                    type_sea = self.title[to_cut:to_cut + len(x) +2]
                    ver = True

            if ver == False:
                to_cut = self.title.index(f"\u00c9pisode")

            crop =  self.title[:to_cut]
            self.content = Show(profile,started,duration,title,bookmark,latest_bookmark).__dict__

            if crop not in dico:
                dico[crop] = {}
            if ver == False:
                dico[crop].update({self.content["ep"]:self.content})
            else:
                if type_sea not in dico[crop]:
                    dico[crop][type_sea]={}
                dico[crop][type_sea].update({self.content["ep"]:self.content})

         
        else:
            self.content = item(profile,started,duration,title,bookmark,latest_bookmark).__dict__
            dico[self.title]  = self.content
        

class item:
    def __init__(self,profile,started,duration,title,bookmark,latest_bookmark):
        self.profile = profile
        self.started = started
        self.duration = duration
        self.bookmark = bookmark
        self.latest_bookmark = latest_bookmark
        self.type = "Movie"
        self.title = title

class Show(item):
    def __init__(self, profile, started, duration, title, bookmark, latest_bookmark):
        super().__init__(profile, started, duration, title, bookmark, latest_bookmark)
        index_ep = self.title.index("pisode")
        self.ep = self.title[index_ep-1:index_ep + len("episode")+1]


file = "./netflix/ViewingActivity.csv"
import json
with open(file,'r',encoding="utf-8")  as f:
        f = f.read().splitlines()

for x in range(len(f)):
    f[x] = f[x].split(",")

dico = {}


f.sort()
for toRemove in f:
    if "(Bande-annonce)" not in toRemove[4]:
        if len(toRemove[5]) ==0:
            item_var = Manager(toRemove[0],toRemove[1],toRemove[2],toRemove[4],toRemove[8],toRemove[9])
   
print("break")
  
with open("datas_netflix_treated.json", "w",encoding="utf-8") as f:
    json.dump(dico,f,indent=4)

print("break")
