class SentimentTree:
    def __init__(self, root, updater):
        self.root = root
        self.updater = updater
        
    def update(self):
        """Update Sentiment and Embeddings"""
        self.updater.update(self.root)