import re

def rule_extractor(rule):
    match_parts = re.match(r'RULE\s*(?P<rule_num>\d+):\s*IF\s*\((?P<rule_hypothesis>.+)\)\sTHEN\s(?P<rule_conclusion>.+);', rule)
    match_dict = match_parts.groupdict()
    rule_num = match_dict['rule_num']
    hypothesis = match_dict['rule_hypothesis']
    conclusion = match_dict['rule_conclusion']
    hypothesis_first_pattern_match = re.match(r'\s*(?P<hypothesis_var>\w+)\s*IS\s*(?P<hypothesis_val>\w+)\s*', hypothesis)
    hypothesis_second_pattern_match = re.match(r'\s*(?P<hypothesis_first_var>\w+)\s*IS\s*(?P<hypothesis_first_val>\w+)\s*\)\s*(?P<operator>\w+)\s*\(\s*(?P<hypothesis_second_var>\w+)\s*IS\s*(?P<hypothesis_second_val>\w+)\s*', hypothesis)
    if hypothesis_second_pattern_match:
        rule_hypothesis = hypothesis_second_pattern_match.groupdict()
    else:
        rule_hypothesis = hypothesis_first_pattern_match.groupdict()
    conclusion_pattern_match = re.match(r'\s*(?P<conclusion_var>\w+)\s*IS\s*(?P<conclusion_val>\w+)\s*', conclusion)
    rule_conclusion = conclusion_pattern_match.groupdict()
    if hypothesis_second_pattern_match:
        rule_dict = {
            'rule_hypothesis': {
                rule_hypothesis['hypothesis_first_var']: rule_hypothesis['hypothesis_first_val'],
                rule_hypothesis['hypothesis_second_var']: rule_hypothesis['hypothesis_second_val'],
                'operator': rule_hypothesis['operator']
            },
            'rule_conclusion': {
                rule_conclusion['conclusion_var']: rule_conclusion['conclusion_val']
            }
        }
    else:
        rule_dict = {
            'rule_hypothesis': {
                rule_hypothesis['hypothesis_var']: rule_hypothesis['hypothesis_val']
            },
            'rule_conclusion': {
                rule_conclusion['conclusion_var']: rule_conclusion['conclusion_val']
            }
        }
    return rule_num, rule_dict

def import_rules(rules_path):
    rules = None
    rules_dict = {}
    with open(rules_path, 'r') as f:
        rules = f.readlines()
    rules = [rule for rule in rules if rule != '\n']
    for rule in rules:
        rule_num, single_rule_dict = rule_extractor(rule)
        rules_dict[rule_num] = single_rule_dict
    # print(rules_dict)
    return rules_dict

def rule_evaluation(rules_dict :dict, input_fuzzified_dict : dict):
    conclusion_dict = {
        'health': {
            'healthy': 0,
            'sick_1' : 0,
            'sick_2' : 0,
            'sick_3' : 0,
            'sick_4' : 0,
        }
    }
    for rule_num, rule in rules_dict.items():
        rule_power = 0

        if rule['rule_hypothesis'].get('operator'):
            hypothesis  = rule['rule_hypothesis']
            conclusion  = rule['rule_conclusion']

            hypothesis_first_variable       = list(hypothesis.keys())[0]
            hypothesis_first_value          = hypothesis[hypothesis_first_variable]
            hypothesis_second_variable      = list(hypothesis.keys())[1]
            hypothesis_second_value         = hypothesis[hypothesis_second_variable]
            hypothesis_operator             = hypothesis['operator']

            first_variable_rule_power       = input_fuzzified_dict[hypothesis_first_variable][hypothesis_first_value]
            second_variable_rule_power      = input_fuzzified_dict[hypothesis_second_variable][hypothesis_second_value]

            if hypothesis_operator.upper() == 'AND':    # compute min of values
                rule_power = min(first_variable_rule_power, second_variable_rule_power)
            elif hypothesis_operator.upper() == 'OR':   # compute max of values
                rule_power = max(first_variable_rule_power, second_variable_rule_power)
            else:
                return

            conclusion_variable     = list(conclusion.keys())[0]
            conclusion_value        = list(conclusion.values())[0]
            conclusion_current_value = conclusion_dict[conclusion_variable][conclusion_value]
            conclusion_dict[conclusion_variable][conclusion_value] = max(rule_power, conclusion_current_value)
            
        else:
            hypothesis  = rule['rule_hypothesis']
            conclusion  = rule['rule_conclusion']

            hypothesis_variable     = list(hypothesis.keys())[0]
            hypothesis_value        = list(hypothesis.values())[0]
            rule_power              = input_fuzzified_dict[hypothesis_variable][hypothesis_value]

            conclusion_variable     = list(conclusion.keys())[0]
            conclusion_value        = list(conclusion.values())[0]
            conclusion_current_value = conclusion_dict[conclusion_variable][conclusion_value]
            conclusion_dict[conclusion_variable][conclusion_value] = max(rule_power, conclusion_current_value)

    print('inference_dict:', conclusion_dict)
    return conclusion_dict


if __name__ == "__main__":
    rules_dict = import_rules('./rules.fcl')
    print(rules_dict)