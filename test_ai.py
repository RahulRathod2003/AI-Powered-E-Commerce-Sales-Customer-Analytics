from ai_engine import generate_business_insight

data_summary = """
Total Revenue: ₹5,865,293.05
Total Orders: 34,500
Average Order Value: ₹170.01
Total Quantity Sold: 51,430

Sales by Category:
Electronics: ₹3,319,206.50
Home: ₹1,077,681.52
Sports: ₹629,825.54
Fashion: ₹471,545.80
Beauty: ₹153,019.38
Toys: ₹132,013.80
Grocery: ₹82,000.51

Sales by Region:
South: ₹1,298,096.07
North: ₹1,264,008.35
West: ₹1,186,350.50
East: ₹1,176,334.75
Central: ₹940,503.38
"""

question = "Which category generates the highest revenue?"

answer = generate_business_insight(data_summary, question)

print("\nAI INSIGHT:")
print(answer)