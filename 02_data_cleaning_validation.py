# Project 2: Data Cleaning and Validation Script
# Client: Global Retail Solutions (USA)

sales_data = [
    {"id": 101, "product": "Laptop", "amount": 1200},
    {"id": 102, "product": "Mouse", "amount": -50},      # ERROR: Negative amount
    {"id": 103, "product": "", "amount": 300},           # ERROR: Missing product name
    {"id": 104, "product": "Keyboard", "amount": 80},
    {"id": 105, "product": "Monitor", "amount": 450}
]

valid_sales = []
corrupted_entries = 0

print("==========================================")
print("     AUTOMATED DATA CLEANING PROCESS      ")
print("==========================================\n")

for item in sales_data:
    # RULE 1: Amount must be greater than 0
    # RULE 2: Product name cannot be empty
    if item["amount"] > 0 and item["product"] != "":
        valid_sales.append(item)
        print(f"✅ Sale ID {item['id']} [{item['product']}]: ${item['amount']} USD -> VALID")
    else:
        corrupted_entries += 1
        print(f"❌ ERROR in Sale ID {item['id']}: Corrupted or missing data detected.")

print("\n------------------------------------------")
print("CLEANING PROCESS SUMMARY:")
print(f"• Successfully processed records: {len(valid_sales)}")
print(f"• Corrupted entries removed: {corrupted_entries}")
print("==========================================")
