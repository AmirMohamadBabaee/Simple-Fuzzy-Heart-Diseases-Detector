from fuzzification import bound_interval

def fuzzify_health(health_value):
    health_healthy  = bound_interval((1 - health_value)/0.75 , 1)
    health_sick1    = bound_interval(health_value , 2 - health_value)
    health_sick2    = bound_interval(health_value - 1 , 3 - health_value)
    health_sick3    = bound_interval(health_value - 2 , 4 - health_value)
    health_sick4    = bound_interval((health_value - 3)/0.75 , 1)
    
    health_dict = {
        'health': {
            'healthy'   : health_healthy,
            'sick_1'    : health_sick1,
            'sick_2'    : health_sick2,
            'sick_3'    : health_sick3,
            'sick_4'    : health_sick4
        }
    }
    return health_dict

def defuzzify_health(inference_dict :dict, step=1e-2):
    weighted_sum = 0    # numerator
    weights_sum = 0     # denominator
    for i in range(int(4/step) + 1):
        health_value = i * step
        max_value = -1
        health_dict = fuzzify_health(health_value)
        for h_key, h_value in health_dict['health'].items():
            max_value = max(max_value, min(h_value, inference_dict['health'][h_key]))
        
        weighted_sum += health_value * max_value
        weights_sum += max_value

    # Center of Mass
    com = weighted_sum / weights_sum 
    print('com:', com)
    com_health_dict = fuzzify_health(com)
    print('com_health_dict:', com_health_dict)
    max_variable = None
    max_value = -1
    for com_key, com_value in com_health_dict['health'].items():
        if max_value < com_value:
            max_value = com_value
            max_variable = com_key

    return max_variable
