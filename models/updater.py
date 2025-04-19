class Updater:
    def update(self, node):
        pass

class AverageUpdater(Updater):
    def update(self, node):
        """Simple average sentiment implementation"""
        children = node.getChildren()
        if len(children) == 0:
            return 
        
        for child in children:
            self.update(child)
        
        avg_sentiment = sum(c.sentiment for c in children) / len(children)
        node.setSentiment(avg_sentiment)
        
class WeightedUpdater(Updater):
    def __init__(self, weights):
        self.weights = weights
        
    def update(self, node):
        children = node.getChildren()
        
        if len(children) == 0:
            return 
        
        for child in children:
            self.update(child)
            
        sentiment = sum(self.weights[c] * c.sentiment for c in children) / sum(self.weights[c] for c in children)