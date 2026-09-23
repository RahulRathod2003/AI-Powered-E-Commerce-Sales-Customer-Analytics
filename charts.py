import pandas as pd
import plotly.express as px
from pathlib import Path

# Load cleaned data
BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "data" / "clean_ecommerce_sales.csv")

# Convert date
df["order_date"] = pd.to_datetime(df["order_date"])


# ==========================================
# 1. SALES BY CATEGORY
# ==========================================

category_sales = (
    df.groupby("category", as_index=False)["total_amount"]
    .sum()
    .sort_values("total_amount", ascending=False)
)

fig1 = px.bar(
    category_sales,
    x="category",
    y="total_amount",
    title="Sales by Product Category",
    text_auto=".2s"
)

fig1.show()


# ==========================================
# 2. SALES BY REGION
# ==========================================

region_sales = (
    df.groupby("region", as_index=False)["total_amount"]
    .sum()
    .sort_values("total_amount", ascending=False)
)

fig2 = px.bar(
    region_sales,
    x="region",
    y="total_amount",
    title="Sales by Region",
    text_auto=".2s"
)

fig2.show()


# ==========================================
# 3. PAYMENT METHOD
# ==========================================

payment_sales = (
    df.groupby("payment_method", as_index=False)
    .size()
    .rename(columns={"size": "transactions"})
)

fig3 = px.pie(
    payment_sales,
    names="payment_method",
    values="transactions",
    title="Payment Method Distribution"
)

fig3.show()


# ==========================================
# 4. CUSTOMER GENDER
# ==========================================

gender_data = (
    df.groupby("customer_gender", as_index=False)
    .size()
    .rename(columns={"size": "customers"})
)

fig4 = px.pie(
    gender_data,
    names="customer_gender",
    values="customers",
    title="Customer Gender Distribution"
)

fig4.show()


# ==========================================
# 5. MONTHLY SALES
# ==========================================

df["month"] = df["order_date"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("month", as_index=False)["total_amount"]
    .sum()
)

fig5 = px.line(
    monthly_sales,
    x="month",
    y="total_amount",
    markers=True,
    title="Monthly Sales Trend"
)

fig5.show()


# ==========================================
# 6. RETURN ANALYSIS
# ==========================================

return_data = (
    df.groupby("returned", as_index=False)
    .size()
    .rename(columns={"size": "orders"})
)

fig6 = px.bar(
    return_data,
    x="returned",
    y="orders",
    title="Returned vs Non-Returned Orders",
    text_auto=True
)

fig6.show()