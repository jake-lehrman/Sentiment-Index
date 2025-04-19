from models.node import SentimentNode
from models.tree import SentimentTree
from models.updater import AverageUpdater

def main():
    # Root Node
    marketNode = SentimentNode("Market")
    
    # Level 2 Nodes
    macroNode = SentimentNode("Macro")
    macroNode.setSentiment
    companiesNode = SentimentNode("Companies")
    
    # Level 3 Nodes
    inflationNode = SentimentNode("Inflation")
    employmentNode = SentimentNode("Employment")
    techNode = SentimentNode("Tech")
    energyNode = SentimentNode("Energy")
    
    # Level 4 Nodes
    cpiNode = SentimentNode("CPI")
    supplyChainNode = SentimentNode("SuplyChain")
    wagesNode = SentimentNode("Wages")
    unemploymentRateNode = SentimentNode("Unemployment Rate")
    aiNode = SentimentNode("AI")
    oilNode = SentimentNode("Oil")
    solarNode = SentimentNode("Solar")
    
    # Set Children and parents
    marketNode.addChild(macroNode)
    marketNode.addChild(companiesNode)
    macroNode.setParent(marketNode)
    companiesNode.setParent(macroNode)
    
    macroNode.addChild(inflationNode)
    macroNode.addChild(employmentNode)
    inflationNode.setParent(macroNode)
    employmentNode.setParent(macroNode)
    
    companiesNode.addChild(techNode)
    companiesNode.addChild(energyNode)
    techNode.setParent(companiesNode)
    energyNode.setParent(companiesNode)
    
    inflationNode.addChild(cpiNode)
    inflationNode.addChild(supplyChainNode)
    cpiNode.setParent(inflationNode)
    supplyChainNode.setParent(inflationNode)
    
    employmentNode.addChild(wagesNode)
    employmentNode.addChild(unemploymentRateNode)
    wagesNode.setParent(employmentNode)
    unemploymentRateNode.setParent(employmentNode)
    
    techNode.addChild(aiNode)
    aiNode.setParent(techNode)
    
    energyNode.addChild(oilNode)
    energyNode.addChild(solarNode)
    oilNode.setParent(energyNode)
    solarNode.setParent(energyNode)
    
    # Create Tree
    updater = AverageUpdater()
    tree = SentimentTree(marketNode, updater)
    
    # Create set of article nodes with sentiment
    article1 = SentimentNode("Article 1")
    article1.setSentiment(0.34)
    
    article2 = SentimentNode("Article 2")
    article2.setSentiment(-0.45)
    
    article3 = SentimentNode("Article 3")
    article3.setSentiment(0.84)
    
    article4 = SentimentNode("Article 4")
    article4.setSentiment(-0.21)
    
    article5 = SentimentNode("Article 5")
    article5.setSentiment(0.06)
    
    article6 = SentimentNode("Article 6")
    article6.setSentiment(-0.49)
    
    article7 = SentimentNode("Article 7")
    article7.setSentiment(-0.30)
    
    article8 = SentimentNode("Article 8")
    article8.setSentiment(0.39)
    
    article9 = SentimentNode("Article 9")
    article9.setSentiment(0.53)
    
    article10 = SentimentNode("Article 10")
    article10.setSentiment(0.70)
    
    # Assign parents to each article
    cpiNode.addChild(article1)
    article1.setParent(cpiNode)
    
    supplyChainNode.addChild(article2)
    article2.setParent(supplyChainNode)
    
    supplyChainNode.addChild(article3)
    article3.setParent(supplyChainNode)
    
    wagesNode.addChild(article4)
    article4.setParent(wagesNode)
    
    unemploymentRateNode.addChild(article5)
    article5.setParent(unemploymentRateNode)
    
    aiNode.addChild(article6)
    article6.setParent(aiNode)
    
    aiNode.addChild(article7)
    article7.setParent(aiNode)
    
    oilNode.addChild(article8)
    article8.setParent(oilNode)
    
    oilNode.addChild(article9)
    article9.setParent(oilNode)
    
    solarNode.addChild(article10)
    article10.setParent(solarNode)
    
    # Update Sentiments
    tree.update()
    
    print(f"Market Sentiment: {marketNode.getSentiment()}")
    print("-----")
    print(f"Macro Sentiment: {macroNode.getSentiment()}")
    print("-----")
    print(f"Companies Sentiment: {companiesNode.getSentiment()}")
    print("-----")
    print(f"Inflation Sentiment: {inflationNode.getSentiment()}")
    print("-----")
    print(f"Employment Sentiment: {employmentNode.getSentiment()}")
    print("-----")
    print(f"Tech Sentiment: {techNode.getSentiment()}")
    print("-----")
    print(f"Energy Sentiment: {energyNode.getSentiment()}")
    print("-----")
    print(f"CPI Sentiment: {cpiNode.getSentiment()}")
    print("-----")
    print(f"Supply Chain Sentiment: {supplyChainNode.getSentiment()}")
    print("-----")
    print(f"Wages Sentiment: {wagesNode.getSentiment()}")
    print("-----")
    print(f"Unemployment Rate Sentiment: {unemploymentRateNode.getSentiment()}")
    print("-----")
    print(f"AI Sentiment: {aiNode.getSentiment()}")
    print("-----")
    print(f"Oil Sentiment: {oilNode.getSentiment()}")
    print("-----")
    print(f"Solar Sentiment: {solarNode.getSentiment()}")
    
    
if __name__ == "__main__":
    main()   