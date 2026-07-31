# Project 3: Automated Business Performance & KPIs Reporter
# Client: TechCorp Services (USA)

sales_team_data = [
    {"agent": "Michael Scott", "sales": 15, "revenue": 14500},
    {"agent": "Jim Halpert", "sales": 22, "revenue": 21000},
    {"agent": "Pam Beesly", "sales": 8, "revenue": 7200},
    {"agent": "Dwight Schrute", "sales": 30, "revenue": 31000},
    {"agent": "Ryan Howard", "sales": 4, "revenue": 3500}
]

total_company_revenue = 0
top_performer = ""
highest_revenue = 0

print("==================================================")
print("     MONTHLY SALES PERFORMANCE REPORT             ")
print("==================================================")

for agent in sales_team_data:
    revenue = agent["revenue"]
    sales_count = agent["sales"]
    avg_sale = revenue / sales_count if sales_count > 0 else 0
    
    total_company_revenue += revenue
    
    if revenue > highest_revenue:
        highest_revenue = revenue
        top_performer = agent["agent"]
        
    if revenue >= 15000:
        status = "HIGH PERFORMER"
    elif revenue >= 8000:
        status = "MET TARGET"
    else:
        status = "NEEDS IMPROVEMENT"
        
    print("Agent:", agent["agent"])
    print("Sales:", sales_count, "| Revenue: $", revenue)
    print("Status:", status)
    print("--------------------------------------------------")

print("EXECUTIVE SUMMARY:")
print("Total Revenue Generated: $", total_company_revenue, "USD")
print("Top Performing Agent:", top_performer, "($", highest_revenue, "USD)")
print("==================================================")
