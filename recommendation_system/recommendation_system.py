from efficient_apriori import apriori

def generate_association_rules(transactions, min_support, min_confidence):
	itemsets, rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence)
	return rules