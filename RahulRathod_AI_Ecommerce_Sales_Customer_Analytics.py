import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ============================================================
# AI ENGINE
# ============================================================

try:
    from ai_engine import generate_business_insight
    AI_AVAILABLE = True
except Exception:
    AI_AVAILABLE = False


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI-Powered E-Commerce Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #ffffff;
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #202124;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #666666;
        margin-bottom: 30px;
    }

    /* KPI Cards */
    .kpi-card {
        padding: 22px;
        border-radius: 15px;
        min-height: 145px;
        box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
        border: 1px solid rgba(0,0,0,0.05);
    }

    .kpi-title {
        font-size: 15px;
        font-weight: 600;
        color: #555555;
        margin-bottom: 10px;
    }

    .kpi-value {
        font-size: 28px;
        font-weight: 800;
        color: #202124;
    }

    .kpi-icon {
        font-size: 25px;
        margin-bottom: 5px;
    }

    /* AI box */
    .ai-header {
        font-size: 30px;
        font-weight: 750;
        color: #202124;
    }

    /* Section headings */
    .section-title {
        font-size: 28px;
        font-weight: 750;
        color: #202124;
        margin-top: 25px;
        margin-bottom: 5px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f3f5f9;
    }

    /* Buttons */
    .stButton button {
        border-radius: 10px;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FIND DATASET
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def find_cleaned_csv():

    # Preferred cleaned dataset names
    preferred_names = [
        "clean_ecommerce_sales.csv",
        "clean_ecommerce.csv",
        "clean_ecommerce_data.csv",
        "cleaned_ecommerce.csv",
        "cleaned_ecommerce_data.csv",
        "cleaned_dataset.csv",
        "ecommerce_cleaned.csv"
    ]

    # First check exact preferred names
    for name in preferred_names:

        file_path = DATA_DIR / name

        if file_path.exists():
            return file_path

    # Then search for any CSV containing "clean"
    clean_files = list(DATA_DIR.glob("*clean*.csv"))

    if clean_files:
        return clean_files[0]

    # Finally search all CSV files
    csv_files = list(DATA_DIR.glob("*.csv"))

    if csv_files:
        # Avoid using original dataset if a clean file exists
        return csv_files[0]

    return None


CSV_FILE = find_cleaned_csv()


# ============================================================
# DATA LOAD
# ============================================================

if CSV_FILE is None:

    st.error(
        "No CSV dataset found. "
        "Please place your CSV file inside the 'data' folder."
    )

    st.info(
        "Expected location: "
        f"{DATA_DIR}"
    )

    st.stop()


@st.cache_data
def load_data(path):
    return pd.read_csv(path)


try:

    df = load_data(CSV_FILE)

except Exception as e:

    st.error(f"Unable to read CSV file: {e}")
    st.stop()


# ============================================================
# DATA PREPARATION
# ============================================================

# Convert date
if "order_date" in df.columns:

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )


# Numeric columns
numeric_columns = [
    "price",
    "discount",
    "quantity",
    "delivery_time_days",
    "total_amount",
    "shipping_cost",
    "profit_margin",
    "customer_age"
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown(
    "## 🔎 Filters"
)


# Category filter
if "category" in df.columns:

    categories = sorted(
        df["category"].dropna().unique().tolist()
    )

    selected_categories = st.sidebar.multiselect(
        "Select Category",
        categories,
        default=categories
    )

else:

    selected_categories = []


# Region filter
if "region" in df.columns:

    regions = sorted(
        df["region"].dropna().unique().tolist()
    )

    selected_regions = st.sidebar.multiselect(
        "Select Region",
        regions,
        default=regions
    )

else:

    selected_regions = []


# Gender filter
if "customer_gender" in df.columns:

    genders = sorted(
        df["customer_gender"].dropna().unique().tolist()
    )

    selected_genders = st.sidebar.multiselect(
        "Select Customer Gender",
        genders,
        default=genders
    )

else:

    selected_genders = []


# Payment method filter
if "payment_method" in df.columns:

    payment_methods = sorted(
        df["payment_method"].dropna().unique().tolist()
    )

    selected_payments = st.sidebar.multiselect(
        "Select Payment Method",
        payment_methods,
        default=payment_methods
    )

else:

    selected_payments = []


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_categories and "category" in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df["category"].isin(selected_categories)
    ]


if selected_regions and "region" in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df["region"].isin(selected_regions)
    ]


if selected_genders and "customer_gender" in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df["customer_gender"].isin(selected_genders)
    ]


if selected_payments and "payment_method" in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df["payment_method"].isin(selected_payments)
    ]


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="main-title">
        🛒 AI-Powered E-Commerce Sales & Customer Analytics
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Analyze sales performance, customers, products, regions,
        payments and generate AI-powered business insights.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATASET STATUS
# ============================================================

st.caption(
    f"📁 Dataset: {CSV_FILE.name} | "
    f"Showing {len(filtered_df):,} of {len(df):,} records"
)


# ============================================================
# EMPTY DATA CHECK
# ============================================================

if filtered_df.empty:

    st.warning(
        "No records match the selected filters. "
        "Please change your filters."
    )

    st.stop()


# ============================================================
# BUSINESS KPI CALCULATIONS
# ============================================================

total_revenue = filtered_df["total_amount"].sum()

total_orders = len(filtered_df)

average_order_value = (
    filtered_df["total_amount"].mean()
)

quantity_sold = (
    filtered_df["quantity"].sum()
)

average_delivery = (
    filtered_df["delivery_time_days"].mean()
)

average_profit_margin = (
    filtered_df["profit_margin"].mean()
)

total_profit = (
    filtered_df["total_amount"]
    * filtered_df["profit_margin"]
    / 100
).sum()


# Return rate
if "returned" in filtered_df.columns:

    return_count = (
        filtered_df["returned"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .sum()
    )

    return_rate = (
        return_count / total_orders * 100
        if total_orders > 0
        else 0
    )

else:

    return_count = 0
    return_rate = 0


# ============================================================
# BUSINESS KPIs
# ============================================================

st.markdown(
    '<div class="section-title">📊 Business KPIs</div>',
    unsafe_allow_html=True
)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)


with kpi1:

    st.markdown(
        f"""
        <div class="kpi-card" style="background:#E8F4FF;">
            <div class="kpi-icon">💰</div>
            <div class="kpi-title">Total Revenue</div>
            <div class="kpi-value">₹{total_revenue:,.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi2:

    st.markdown(
        f"""
        <div class="kpi-card" style="background:#EEF9EE;">
            <div class="kpi-icon">🛍️</div>
            <div class="kpi-title">Total Orders</div>
            <div class="kpi-value">{total_orders:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi3:

    st.markdown(
        f"""
        <div class="kpi-card" style="background:#FFF5E6;">
            <div class="kpi-icon">🧾</div>
            <div class="kpi-title">Average Order Value</div>
            <div class="kpi-value">₹{average_order_value:,.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi4:

    st.markdown(
        f"""
        <div class="kpi-card" style="background:#F3EDFF;">
            <div class="kpi-icon">📦</div>
            <div class="kpi-title">Quantity Sold</div>
            <div class="kpi-value">{quantity_sold:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


kpi5, kpi6, kpi7, kpi8 = st.columns(4)


with kpi5:

    st.markdown(
        f"""
        <div class="kpi-card" style="background:#EAF7F7;">
            <div class="kpi-icon">🚚</div>
            <div class="kpi-title">Avg Delivery Time</div>
            <div class="kpi-value">{average_delivery:.2f} days</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi6:

    st.markdown(
        f"""
        <div class="kpi-card" style="background:#FFF0F0;">
            <div class="kpi-icon">📈</div>
            <div class="kpi-title">Avg Profit Margin</div>
            <div class="kpi-value">{average_profit_margin:.2f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi7:

    st.markdown(
        f"""
        <div class="kpi-card" style="background:#F0F7FF;">
            <div class="kpi-icon">🔄</div>
            <div class="kpi-title">Return Rate</div>
            <div class="kpi-value">{return_rate:.2f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi8:

    st.markdown(
        f"""
        <div class="kpi-card" style="background:#F5F5F5;">
            <div class="kpi-icon">💵</div>
            <div class="kpi-title">Total Profit</div>
            <div class="kpi-value">₹{total_profit:,.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# MONTHLY SALES TREND
# ============================================================

st.markdown(
    '<div class="section-title">📈 Monthly Sales Trend</div>',
    unsafe_allow_html=True
)

if "order_date" in filtered_df.columns:

    monthly_sales = (
        filtered_df
        .dropna(subset=["order_date"])
        .groupby(
            filtered_df["order_date"].dt.to_period("M")
        )["total_amount"]
        .sum()
        .reset_index()
    )

    monthly_sales["order_date"] = (
        monthly_sales["order_date"]
        .astype(str)
    )

    monthly_sales.columns = [
        "Month",
        "Revenue"
    ]

    fig_monthly = px.line(
        monthly_sales,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue Trend"
    )

    fig_monthly.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue (₹)",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig_monthly,
        use_container_width=True
    )


# ============================================================
# SALES BY CATEGORY
# ============================================================

st.markdown(
    '<div class="section-title">📦 Sales by Category</div>',
    unsafe_allow_html=True
)

if "category" in filtered_df.columns:

    category_sales = (
        filtered_df
        .groupby("category")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    category_sales.columns = [
        "Category",
        "Revenue"
    ]

    fig_category = px.bar(
        category_sales,
        x="Category",
        y="Revenue",
        text_auto=".2s",
        title="Revenue by Category"
    )

    fig_category.update_layout(
        xaxis_title="Category",
        yaxis_title="Revenue (₹)"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )


# ============================================================
# SALES BY REGION
# ============================================================

st.markdown(
    '<div class="section-title">🌍 Sales by Region</div>',
    unsafe_allow_html=True
)

if "region" in filtered_df.columns:

    region_sales = (
        filtered_df
        .groupby("region")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    region_sales.columns = [
        "Region",
        "Revenue"
    ]

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="Revenue",
        text_auto=".2s",
        title="Revenue by Region"
    )

    fig_region.update_layout(
        xaxis_title="Region",
        yaxis_title="Revenue (₹)"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )


# ============================================================
# TWO COLUMN ANALYSIS
# ============================================================

left_col, right_col = st.columns(2)


# ============================================================
# PAYMENT METHODS
# ============================================================

with left_col:

    st.markdown(
        '<div class="section-title">💳 Payment Methods</div>',
        unsafe_allow_html=True
    )

    if "payment_method" in filtered_df.columns:

        payment_data = (
            filtered_df["payment_method"]
            .value_counts()
            .reset_index()
        )

        payment_data.columns = [
            "Payment Method",
            "Orders"
        ]

        fig_payment = px.pie(
            payment_data,
            names="Payment Method",
            values="Orders",
            hole=0.35,
            title="Orders by Payment Method"
        )

        st.plotly_chart(
            fig_payment,
            use_container_width=True
        )


# ============================================================
# CUSTOMER GENDER
# ============================================================

with right_col:

    st.markdown(
        '<div class="section-title">👥 Customer Gender</div>',
        unsafe_allow_html=True
    )

    if "customer_gender" in filtered_df.columns:

        gender_data = (
            filtered_df["customer_gender"]
            .value_counts()
            .reset_index()
        )

        gender_data.columns = [
            "Gender",
            "Orders"
        ]

        fig_gender = px.bar(
            gender_data,
            x="Gender",
            y="Orders",
            text_auto=True,
            title="Orders by Customer Gender"
        )

        fig_gender.update_layout(
            xaxis_title="Gender",
            yaxis_title="Orders"
        )

        st.plotly_chart(
            fig_gender,
            use_container_width=True
        )


# ============================================================
# RETURN ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">🔄 Return Analysis</div>',
    unsafe_allow_html=True
)

if "returned" in filtered_df.columns:

    return_data = (
        filtered_df["returned"]
        .astype(str)
        .str.strip()
        .str.title()
        .value_counts()
        .reset_index()
    )

    return_data.columns = [
        "Returned",
        "Orders"
    ]

    fig_return = px.pie(
        return_data,
        names="Returned",
        values="Orders",
        hole=0,
        title="Returned vs Non-Returned Orders"
    )

    st.plotly_chart(
        fig_return,
        use_container_width=True
    )

    st.info(
        f"Return rate for the selected data: {return_rate:.2f}%"
    )


# ============================================================
# AI BUSINESS INSIGHT
# ============================================================

st.markdown(
    '<div class="section-title">🤖 Ask AI</div>',
    unsafe_allow_html=True
)

st.write(
    "Ask a business question about the selected e-commerce data."
)


question = st.text_input(
    "Enter your business question",
    placeholder="Example: Which category generates the highest revenue?"
)


# ============================================================
# CREATE DATA SUMMARY FOR AI
# ============================================================

def create_ai_summary(data):

    summary = {}

    summary["total_orders"] = len(data)

    summary["total_revenue"] = round(
        data["total_amount"].sum(),
        2
    )

    summary["average_order_value"] = round(
        data["total_amount"].mean(),
        2
    )

    summary["quantity_sold"] = int(
        data["quantity"].sum()
    )

    summary["average_delivery_time"] = round(
        data["delivery_time_days"].mean(),
        2
    )

    summary["average_profit_margin"] = round(
        data["profit_margin"].mean(),
        2
    )

    summary["total_profit"] = round(
        (data["total_amount"] * data["profit_margin"] / 100).sum(),
        2
    )

    # Category
    if "category" in data.columns:

        summary["sales_by_category"] = (
            data.groupby("category")["total_amount"]
            .sum()
            .round(2)
            .sort_values(ascending=False)
            .to_dict()
        )

    # Region
    if "region" in data.columns:

        summary["sales_by_region"] = (
            data.groupby("region")["total_amount"]
            .sum()
            .round(2)
            .sort_values(ascending=False)
            .to_dict()
        )

    # Payment
    if "payment_method" in data.columns:

        summary["payment_methods"] = (
            data["payment_method"]
            .value_counts()
            .to_dict()
        )

    # Gender
    if "customer_gender" in data.columns:

        summary["customer_gender"] = (
            data["customer_gender"]
            .value_counts()
            .to_dict()
        )

    # Returns
    if "returned" in data.columns:

        summary["returns"] = (
            data["returned"]
            .astype(str)
            .str.strip()
            .str.title()
            .value_counts()
            .to_dict()
        )

    # Build a human-readable string for the LLM
    lines = []
    lines.append(f"Total Orders: {summary['total_orders']}")
    lines.append(f"Total Revenue: ₹{summary['total_revenue']:,}")
    lines.append(f"Average Order Value: ₹{summary['average_order_value']:,}")
    lines.append(f"Quantity Sold: {summary['quantity_sold']:,}")
    lines.append(
        f"Average Delivery Time: {summary['average_delivery_time']} days"
    )
    lines.append(
        f"Average Profit Margin: {summary['average_profit_margin']}%"
    )
    lines.append(f"Total Estimated Profit: ₹{summary['total_profit']:,}")

    if "sales_by_category" in summary:
        lines.append("\nSales by Category:")
        for cat, val in summary["sales_by_category"].items():
            lines.append(f"  {cat}: ₹{val:,}")

    if "sales_by_region" in summary:
        lines.append("\nSales by Region:")
        for region, val in summary["sales_by_region"].items():
            lines.append(f"  {region}: ₹{val:,}")

    if "payment_methods" in summary:
        lines.append("\nPayment Methods (orders):")
        for method, count in summary["payment_methods"].items():
            lines.append(f"  {method}: {count:,}")

    if "customer_gender" in summary:
        lines.append("\nCustomer Gender (orders):")
        for gender, count in summary["customer_gender"].items():
            lines.append(f"  {gender}: {count:,}")

    if "returns" in summary:
        lines.append("\nOrder Returns:")
        for status, count in summary["returns"].items():
            lines.append(f"  {status}: {count:,}")

    return "\n".join(lines)


# ============================================================
# AI BUTTON
# ============================================================

if st.button(
    "✨ Analyze with AI",
    type="primary"
):

    if not question.strip():

        st.warning(
            "Please enter a business question first."
        )

    elif not AI_AVAILABLE:

        st.error(
            "AI engine is unavailable. "
            "Please ensure GROQ_API_KEY is set in your .env file "
            "and that ai_engine.py is present."
        )

    else:

        with st.spinner(
            "AI is analyzing the selected data..."
        ):

            try:

                data_summary = create_ai_summary(
                    filtered_df
                )

                answer = generate_business_insight(
                    data_summary,
                    question
                )

                st.success(
                    "AI Analysis Complete"
                )

                st.markdown(
                    "## 💡 AI Business Insight"
                )

                st.markdown(answer)

            except Exception as e:

                st.error(
                    f"AI analysis failed: {e}"
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "AI-Powered E-Commerce Sales & Customer Analytics | "
    "Python • Pandas • Plotly • Streamlit • Groq"
)