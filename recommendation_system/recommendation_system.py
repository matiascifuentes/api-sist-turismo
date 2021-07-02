from efficient_apriori import apriori
from recommendation_system.rule import Rule
from recommendation_system.utils import get_itemset_historico_sesiones, get_itemset_historico_listas
import json

def generate_association_rules(transactions, min_support, min_confidence):
	itemsets, rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence)
	return rules

def recommendations(service, rules, max_results):
	result = []
	for rule in rules:
		if len(result) == max_results:
			break
		if rule.lhs == service:
			result.append(rule.rhs)
	return result

def save_rules_to_file(rules):
	min_lift = 1
	rules = sorted(rules, key=lambda rule: rule.lift, reverse=True)
	rules = filter(lambda rule: rule.lift > min_lift, rules)
	data = {}
	data['rules'] = []
	for rule in rules:
		data['rules'].append(Rule(rule.lhs[0],rule.rhs[0],rule.support,rule.confidence,rule.lift).json())

	with open('rules.json', 'w') as file:
		json.dump(data, file)	#json.dump(data, file, indent=4)

def get_rules_from_file():
	rules = []
	try:
		with open('rules.json') as file:
			data = json.load(file)
			for rule in data['rules']:
				rules.append(Rule(rule['lhs'],rule['rhs'],rule['support'],rule['confidence'],rule['lift']))
		return True, rules
	except:
		return False, rules

def get_rules_from_sessions(user_id):
	rules = []
	try:
		min_lift = 1
		itemset = get_itemset_historico_sesiones(user_id,1000)
		rules_aux = generate_association_rules(itemset,0.1,0.3)
		rules_aux = sorted(rules_aux, key=lambda rule: rule.lift, reverse=True)
		rules_aux = filter(lambda rule: rule.lift > min_lift, rules_aux)
		for rule in rules_aux:
			rules.append(Rule(rule.lhs[0],rule.rhs[0],rule.support,rule.confidence,rule.lift))
		return True, rules
	except:
		return False, rules

def save_rules():
	try:
		itemset = get_itemset_historico_listas()
		rules = generate_association_rules(itemset,0.1,0.1)
		save_rules_to_file(rules)
		return True
	except:
		return False