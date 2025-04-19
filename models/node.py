class SentimentNode:
    def __init__(self, name, shortTerm=None, longTerm=None, parent=None, children=None):
        self.name = name
        self.sentiment = 0.0
        self.shortTerm = shortTerm
        self.longTerm = longTerm
        self.parent = parent
        self.children = children or []
        
    def setSentiment(self, sentiment):
        self.sentiment = sentiment
        
    def getSentiment(self):
        return self.sentiment
        
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
    
    def setParent(self, parent):
        self.parent = parent
        
    def addChild(self, child):
        self.children.append(child)
    
    def getParent(self):
        return self.parent
    
    def getChildren(self):
        return self.children
    
    
        