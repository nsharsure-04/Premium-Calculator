# Premium Calculator – LLM Assignment

## Objective

To demonstrate how a complex task is built using small primitive functions in an LLM-friendly design.

---

## Complex Function

**Premium Calculator**

---

## Primitive Functions

- `extractData()`
- `lookupValue()`
- `applyFormula()`

---

## Workflow

1. Extract age, location, and coverage from the user profile.  
2. Get base rate using location.  
3. Get risk multiplier using age.  
4. Apply premium calculation formula.

**Formula:**  
`Premium = baseRate × riskMultiplier × coverage × 0.01`

---

## Project Description

This project calculates insurance premium based on user profile data and rates from lookup tables.

---

## How to Run

Run the Python script using:

```bash
python premium_calculator.py
