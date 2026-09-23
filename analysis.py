import pandas as pd
from pathlib import Path

# ==========================================
# 1. LOAD DATA
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "data" / "ecommerce_sales.csv")

print("Original shape:", df.shape)


# ==========================================
# 2. CONVERT DATE COLUMN
# ==========================================

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")


# ==========================================
# 3. CHECK DATA QUALITY
# ==========================================

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


# ==========================================
# 4. CHECK NUMERIC VALUES
# ==========================================

print("\nNumeric column summary:")
print(df[
    [
        "price",
        "discount",
        "quantity",
        "delivery_time_days",
        "total_amount",
        "shipping_cost",
        "profit_margin",
        "customer_age"
    ]
].describe())


# ==========================================
# 5. CHECK CATEGORICAL VALUES
# ==========================================

print("\nCategories:")
print(df["category"].value_counts())

print("\nPayment methods:")
print(df["payment_method"].value_counts())

print("\nRegions:")
print(df["region"].value_counts())

print("\nCustomer gender:")
print(df["customer_gender"].value_counts())

print("\nReturned:")
print(df["returned"].value_counts())


# ==========================================
# 6. CREATE USEFUL FEATURES
# ==========================================

df["revenue"] = df["total_amount"]

df["total_cost"] = df["shipping_cost"]

df["profit"] = df["revenue"] * (df["profit_margin"] / 100)


# ==========================================
# 7. BASIC BUSINESS KPIs
# ==========================================

print("\n========== BUSINESS KPIs ==========")

print("Total Revenue:", round(df["revenue"].sum(), 2))

print("Average Order Value:", round(df["revenue"].mean(), 2))

print("Total Quantity Sold:", df["quantity"].sum())

print("Average Delivery Time:",
      round(df["delivery_time_days"].mean(), 2), "days")

print("Average Profit Margin:",
      round(df["profit_margin"].mean(), 2))

print("Total Estimated Profit:",
      round(df["profit"].sum(), 2))


# ==========================================
# 8. TOP CATEGORIES
# ==========================================

category_sales = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY CATEGORY ==========")
print(category_sales)


# ==========================================
# 9. SALES BY REGION
# ==========================================

region_sales = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY REGION ==========")
print(region_sales)


# ==========================================
# 10. SAVE CLEAN DATA
# ==========================================

df.to_csv(BASE_DIR / "data" / "clean_ecommerce_sales.csv", index=False)

print("\nClean dataset saved successfully.")
print("Final shape:", df.shape)