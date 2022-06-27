from fuzzification import fuzzify
from inference import import_rules, rule_evaluation
from defuzzification import defuzzify_health

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        input_fuzzified = fuzzify(input_dict)
        rules_dict = import_rules('./rules.fcl')
        inference_dict = rule_evaluation(rules_dict, input_fuzzified)
        health_output = defuzzify_health(inference_dict)
        return health_output
