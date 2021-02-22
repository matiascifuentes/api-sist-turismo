from efficient_apriori import apriori
from rule import Rule
import json

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

def save_rules_to_file(rules):
	data = {}
	data['rules'] = []
	for rule in rules:
		data['rules'].append(Rule(rule.lhs[0],rule.rhs[0],rule.support,rule.confidence,rule.lift).json())

	with open('rules.json', 'w') as file:
		json.dump(data, file)



