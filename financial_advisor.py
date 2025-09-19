 # sales tax 
sales_tax_rates = {
    "Alabama": 4.00, "Alaska": 0.00, "Arizona": 5.60, "Arkansas": 6.50, "California": 6.00,
    "Colorado": 2.90, "Connecticut": 6.35, "Delaware": 0.00, "Florida": 6.00, "Georgia": 4.00,
    "Hawaii": 4.00, "Idaho": 6.00, "Illinois": 6.25, "Indiana": 7.00, "Iowa": 6.00,       
    "Kansas": 6.50, "Kentucky": 6.00, "Louisiana": 4.45, "Maine": 5.50, "Maryland": 6.00,
    "Massachusetts": 6.25, "Michigan": 6.00, "Minnesota": 6.875, "Mississippi": 7.00, "Missouri": 4.23,
    "Montana": 0.00, "Nebraska": 5.50, "Nevada": 6.85, "New Hampshire": 0.00, "New Jersey": 6.625,
    "New Mexico": 5.13, "New York": 4.00, "North Carolina": 4.75, "North Dakota": 5.00, "Ohio": 5.75,
    "Oklahoma": 4.50, "Oregon": 0.00, "Pennsylvania": 6.00, "Rhode Island": 7.00, "South Carolina": 6.00,
    "South Dakota": 4.50, "Tennessee": 7.00, "Texas": 6.25, "Utah": 6.10, "Vermont": 6.00,
    "Virginia": 5.30, "Washington": 6.50, "West Virginia": 6.00, "Wisconsin": 5.00, "Wyoming": 4.00
}

# income tax
state_income_tax_rates = {
    "Alabama": {"type": "graduated", "rates": "2% – 5%"},
    "Alaska": {"type": "none", "rates": "N/A"},
    "Arizona": {"type": "flat", "rates": "2.5%"},
    "Arkansas": {"type": "graduated", "rates": "0% – 3.9%"},
    "California": {"type": "graduated", "rates": "1% – 13.3%"},
    "Colorado": {"type": "flat", "rates": "4.4%"},
    "Connecticut": {"type": "graduated", "rates": "2% – 6.99%"},
    "Delaware": {"type": "graduated", "rates": "2.2% – 6.6%"},
    "Florida": {"type": "none", "rates": "N/A"},
    "Georgia": {"type": "flat", "rates": "5.39%"},
    "Hawaii": {"type": "graduated", "rates": "1.4% – 11%"},
    "Idaho": {"type": "flat", "rates": "5.695%"},
    "Illinois": {"type": "flat", "rates": "4.95%"},
    "Indiana": {"type": "flat", "rates": "3%"},
    "Iowa": {"type": "flat", "rates": "3.8%"},
    "Kansas": {"type": "graduated", "rates": "5.2% – 5.58%"},
    "Kentucky": {"type": "flat", "rates": "4%"},
    "Louisiana": {"type": "flat", "rates": "3%"},
    "Maine": {"type": "graduated", "rates": "5.8% – 7.15%"},
    "Maryland": {"type": "graduated", "rates": "2% – 5.75%"},
    "Massachusetts": {"type": "flat", "rates": "5%"},
    "Michigan": {"type": "flat", "rates": "4.25%"},
    "Minnesota": {"type": "graduated", "rates": "5.35% – 9.85%"},
    "Mississippi": {"type": "flat", "rates": "4.4%"},
    "Missouri": {"type": "graduated", "rates": "2% – 4.8%"},
    "Montana": {"type": "graduated", "rates": "4.7% – 5.9%"},
    "Nebraska": {"type": "graduated", "rates": "2.46% – 5.2%"},
    "Nevada": {"type": "none", "rates": "N/A"},
    "New Hampshire": {"type": "none", "rates": "N/A"},
    "New Jersey": {"type": "graduated", "rates": "1.4% – 10.75%"},
    "New Mexico": {"type": "graduated", "rates": "1.5% – 5.9%"},
    "New York": {"type": "graduated", "rates": "4% – 10.9%"},
    "North Carolina": {"type": "flat", "rates": "4.25%"},
    "North Dakota": {"type": "graduated", "rates": "0% – 2.5%"},
    "Ohio": {"type": "graduated", "rates": "0% – 3.5%"},
    "Oklahoma": {"type": "graduated", "rates": "0.25% – 4.75%"},
    "Oregon": {"type": "graduated", "rates": "4.75% – 9.9%"},
    "Pennsylvania": {"type": "flat", "rates": "3.07%"},
    "Rhode Island": {"type": "graduated", "rates": "3.75% – 5.99%"},
    "South Carolina": {"type": "graduated", "rates": "0% – 6.2%"},
    "South Dakota": {"type": "none", "rates": "N/A"},
    "Tennessee": {"type": "none", "rates": "N/A"},
    "Texas": {"type": "none", "rates": "N/A"},
    "Utah": {"type": "flat", "rates": "4.55%"},
    "Vermont": {"type": "graduated", "rates": "3.35% – 8.75%"},
    "Virginia": {"type": "graduated", "rates": "2% – 5.75%"},
    "Washington": {"type": "none", "rates": "N/A"},
    "West Virginia": {"type": "graduated", "rates": "2.22% – 4.82%"},
    "Wisconsin": {"type": "graduated", "rates": "3.54% – 7.65%"},
    "Wyoming": {"type": "none", "rates": "N/A"}
}

## User data dictionary
user_data = {}


user_data["Name"] = input("Whats your name?").title()
user_data["State"] = input("Whats state to you live in?").title

income_type = input("Would you like to use hourly income to budget, or anual?").lower

if income_type == "hourly":
    user_data["Hourly income"] = input("How much do you make per hour?")


Xaviercelz/Financial-Advisor 