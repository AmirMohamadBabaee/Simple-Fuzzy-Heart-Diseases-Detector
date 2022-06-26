import re

def rule_extractor(rule):
    match_parts = re.match(r'RULE\s(?P<rule_num>\d+):\sIF\s*\((?P<rule_hypothesis>.+)\)\sTHEN\s(?P<rule_conclusion>.+);', rule)
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


if __name__ == "__main__":
    import_rules('./rules.fcl')