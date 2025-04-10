class Updater:
    def update(self, node):
        """Simple average sentiment implementation"""
        children = node.getChildren()
        if len(children) == 0:
            return 
        
        for child in children:
            self.update(child)
        
        avg_sentiment = sum(c.sentiment for c in children) / len(children)
        node.setSentiment(avg_sentiment)