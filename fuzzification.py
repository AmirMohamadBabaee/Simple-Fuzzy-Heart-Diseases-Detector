def bound_interval(value1, value2):
    return max(min(value1, value2), 0)

def fuzzify_age(age):
    age_young   = bound_interval((38 - age)/9 , 1)
    age_mild    = bound_interval((age - 33)/5 , (45 - age)/7)
    age_old     = bound_interval((age - 40)/8 , (58 - age)/10)
    age_veryold = bound_interval((age - 52)/8 , 1)
    return age_young, age_mild, age_old, age_veryold

def fuzzify_blood_pressure(blood_pressure):
    blood_pressure_low      = bound_interval((134 - blood_pressure)/23 , 1)
    blood_pressure_medium   = bound_interval((blood_pressure - 127)/12 , (153 - blood_pressure)/14)
    blood_pressure_high     = bound_interval((blood_pressure - 142)/15 , (172 - blood_pressure)/15)
    blood_pressure_veryhigh = bound_interval((blood_pressure - 154)/17 , 1)
    return blood_pressure_low, blood_pressure_medium, blood_pressure_high, blood_pressure_veryhigh

def fuzzify_blood_sugar(blood_sugar):
    blood_sugar_veryhigh = bound_interval((blood_sugar - 105)/15 , 1)
    return blood_sugar_veryhigh

def fuzzify_cholesterol(cholesterol):
    cholesterol_low         = bound_interval((197 - cholesterol)/46 , 1)
    cholesterol_medium      = bound_interval((cholesterol - 188)/27 , (250 - cholesterol)/35)
    cholesterol_high        = bound_interval((cholesterol - 217)/46 , (307 - cholesterol)/44)
    cholesterol_veryhigh    = bound_interval((cholesterol - 281)/66 , 1)
    return cholesterol_low, cholesterol_medium, cholesterol_high, cholesterol_veryhigh

def fuzzify_heart_rate(heart_rate):
    heart_rate_low      = bound_interval((141 - heart_rate)/41 , 1) 
    heart_rate_medium   = bound_interval((heart_rate - 111)/41 , (194 - heart_rate)/42)
    heart_rate_high     = bound_interval((heart_rate - 152)/58 , 1)
    return heart_rate_low, heart_rate_medium, heart_rate_high

def fuzzify_ECG(ecg):
    ECG_normal      = bound_interval((0.4 - ecg)/0.4 , 1)
    ECG_abnormal    = bound_interval((ecg - 0.2)/0.8 , (1.8 - ecg)/0.8)
    ECG_hypertrophy = bound_interval((ecg - 1.4)/0.5 , 1)
    return ECG_normal, ECG_abnormal, ECG_hypertrophy

def fuzzify_old_peak(old_peak):
    old_peak_low        = bound_interval(2-old_peak , 1)
    old_peak_risk       = bound_interval((old_peak - 1.5)/1.3 , (4.2 - old_peak)/1.4)
    old_peak_terrible   = bound_interval((old_peak - 2.5)/1.5 , 1)
    return old_peak_low, old_peak_risk, old_peak_terrible

def fuzzify_exercise(exercise):
    """"
    Singleton Fuzzifier

    exercise == 0   : is prohibited
    exercise == 1   : is allowed
    """
    if exercise == 0:
        exercise_fuzzified = (1, 0)
    elif exercise == 1:
        exercise_fuzzified = (0, 1)
    else:
        return
    return exercise_fuzzified

def fuzzify_thallium(thallium):
    """"
    Singleton Fuzzifier
    """
    if thallium == 3:
        thallium_fuzzified = (1, 0, 0)
    elif thallium == 6:
        thallium_fuzzified = (0, 1, 0)
    elif thallium == 7:
        thallium_fuzzified = (0, 0, 1)
    else:
        return
    return thallium_fuzzified

def fuzzify_sex(sex):
    """
    Singleton Fuzzifier

    sex == 0    : Male
    sex == 1    : Female
    """
    if sex == 0:
        sex_fuzzified = (1, 0)
    elif sex == 1:
        sex_fuzzified = (0, 1)
    else:
        return
    return sex_fuzzified

def fuzzify_chest_pain(chest_pain):
    """
    Singleton Fuzzifier

    chest_pain == 1 : Typical Angina
    chest_pain == 2 : Atypical Angina
    chest_pain == 3 : Non-anginal Pain
    chest_pain == 4 : Asymptomatic
    """
    if chest_pain == 1:
        chest_pain_fuzzified = (1, 0, 0, 0)
    elif chest_pain == 2:
        chest_pain_fuzzified = (0, 1, 0, 0)
    elif chest_pain == 3:
        chest_pain_fuzzified = (0, 0, 1, 0)
    elif chest_pain == 4:
        chest_pain_fuzzified = (0, 0, 0, 1)
    else:
        return
    return chest_pain_fuzzified