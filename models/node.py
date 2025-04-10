class Node:
    def __init__(self, name, shortTerm=None, longTerm=None, parent=None, children=None):
        self.name = name
        self.sentiment = 0.0
        self.shortTerm = shortTerm
        self.longTerm = longTerm
        self.parent = parent
        self.children = children or []
        
    def setSentiment(self, sentiment):
        self.sentiment = sentiment
        
    def setShortTermContext(self, embedding):
        self.shortTerm = embedding
        
    def setLongTermContext(self, embedding):
        self.longTerm = embedding
        
    def getSentiment(self):
        return self.sentiment
    
    def getShortTermContext(self):
        return self.shortTerm
    
    def getLongTermContext(self):
        return self.getLongTermContext
    
    def getParent(self):
        return self.parent
    
    
        
        
    
        