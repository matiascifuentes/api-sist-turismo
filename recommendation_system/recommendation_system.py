from efficient_apriori import apriori

def generate_association_rules(transactions, min_support, min_confidence):
	itemsets, rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence)
	return rules

def recommendations(service, rules, max_results):
	result = []
	for rule in rules:
		if len(result) == max_results:
			break
		if rule.lhs[0] == service:
			result.append(rule.rhs[0])
	return result