from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class SentimentAnalyzer:
    """Aspect-Based Sentiment Analyzer (ABSA)"""
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
        self.model = AutoModelForSequenceClassification.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
    
    """
    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model
    """
    
       
    def analyze_sentiment(self, text, entity):
        inputs = self.tokenizer(f"{text} [SEP] {entity}", return_tensors="pt")
        outputs = self.model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1).detach().numpy()[0]

        score = probs[0] * -1 + probs[1] * 0 + probs[2] * 1
        
        return float(score)
