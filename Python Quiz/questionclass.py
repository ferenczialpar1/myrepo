class Questions:
    def __init__(self,diff,question,a,b,c,d,correct):
        self.diff=diff
        self.question=question
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.correct=correct
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s" % (self.diff,self.question,self.a,self.b,self.c,self.d,self.correct)


