class Resultclass:
    def __init__(self,name,win,time):
        self.name=name
        self.win=win
        self.time=time
    def __str__(self):
        return "%s,%s,%s" % (self.name,self.win,self.time)


