def extractData(userProfile, fields):
    return {field: userProfile[field] for field in fields}


def lookupValue(table, key, valueField):
    return table[key][valueField]


def applyFormula(formula, variables):
    return eval(formula, {}, variables)


def premiumCalculator(userProfile, ratesTable, riskTable):
    data = extractData(userProfile, ['age', 'location', 'coverage'])

    baseRate = lookupValue(ratesTable, data['location'], 'baseRate')
    riskMultiplier = lookupValue(riskTable, data['age'], 'riskMultiplier')

    premium = applyFormula(
        'baseRate * riskMultiplier * coverage * 0.01',
        {
            'baseRate': baseRate,
            'riskMultiplier': riskMultiplier,
            'coverage': data['coverage']
        }
    )

    return premium


userProfile = {
    'age': 30,
    'location': 'city',
    'coverage': 500000
}

ratesTable = {
    'city': {'baseRate': 1.2}
}

riskTable = {
    30: {'riskMultiplier': 1.1}
}

print("Premium:", premiumCalculator(userProfile, ratesTable, riskTable))
