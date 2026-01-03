# Extract specified fields from the user profile dictionary
def extractData(userProfile, fields):
    return {field: userProfile[field] for field in fields}


# Lookup a specific value from a nested table dictionary
def lookupValue(table, key, valueField):
    return table[key][valueField]


# Evaluate a formula string with given variable mappings
def applyFormula(formula, variables):
    return eval(formula, {}, variables)


# Main function to calculate insurance premium
def premiumCalculator(userProfile, ratesTable, riskTable):
    # Extract age, location, and coverage from user profile
    data = extractData(userProfile, ['age', 'location', 'coverage'])

    # Get base rate from rates table based on location
    baseRate = lookupValue(ratesTable, data['location'], 'baseRate')

    # Get risk multiplier from risk table based on age
    riskMultiplier = lookupValue(riskTable, data['age'], 'riskMultiplier')

    # Calculate premium using the formula
    premium = applyFormula(
        'baseRate * riskMultiplier * coverage * 0.01',
        {
            'baseRate': baseRate,
            'riskMultiplier': riskMultiplier,
            'coverage': data['coverage']
        }
    )

    return premium


# Example user profile data
userProfile = {
    'age': 30,
    'location': 'city',
    'coverage': 500000
}

# Rates table based on location
ratesTable = {
    'city': {'baseRate': 1.2}
}

# Risk table based on age
riskTable = {
    30: {'riskMultiplier': 1.1}
}

# Calculate and print the premium
print("Premium:", premiumCalculator(userProfile, ratesTable, riskTable))
