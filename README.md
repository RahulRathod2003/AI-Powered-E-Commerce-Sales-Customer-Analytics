# 🛒 AI-Powered E-Commerce Sales & Customer Analytics

> An interactive business intelligence dashboard built with Python and Streamlit that combines real-time sales analytics with Groq-powered AI business insights.

---

## 📋 Project Description

This project is a fully interactive e-commerce analytics dashboard that enables business users and data analysts to explore sales performance, customer behaviour, regional trends, and payment patterns — all filtered in real time. The dashboard is augmented with an AI question-and-answer engine powered by the Groq API (GPT-OSS 120B), allowing users to ask plain-English business questions and receive data-driven insights instantly.

---

## 🔍 Problem Statement

E-commerce businesses generate large volumes of transactional data that are difficult to interpret without specialised tools. Decision-makers need a fast, intuitive way to:

- Monitor revenue, orders, and profitability across product categories and regions
- Understand customer demographics and purchasing behaviour
- Track return rates and delivery performance
- Ask ad-hoc business questions without writing code or SQL

---

## 🎯 Objectives

1. Build an interactive, filter-driven sales analytics dashboard
2. Calculate and display accurate business KPIs in real time
3. Visualise sales, regional, customer, and payment trends with interactive charts
4. Integrate an AI engine to answer natural-language business questions about the data
5. Ensure the application is secure, reproducible, and professionally packaged

---

## ✨ Key Features

| Feature | Description |
|---|---|
| **8 KPI Cards** | Total Revenue, Total Orders, AOV, Quantity Sold, Avg Delivery Time, Avg Profit Margin, Return Rate, Total Profit |
| **4 Sidebar Filters** | Filter by Category, Region, Customer Gender, Payment Method |
| **Monthly Sales Trend** | Interactive line chart of revenue over time |
| **Sales by Category** | Bar chart of revenue per product category |
| **Sales by Region** | Bar chart of revenue per geographic region |
| **Payment Method Analysis** | Donut pie chart of order distribution by payment type |
| **Customer Gender Analysis** | Bar chart of orders by gender |
| **Return Analysis** | Pie chart of returned vs non-returned orders with return rate |
| **AI Business Insights** | Ask any business question; get AI-generated analysis using Groq GPT-OSS 120B |
| **Real-time Filtering** | All KPIs and charts update instantly when sidebar filters change |

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|---|---|---|
| Python | 3.13 | Runtime |
| Streamlit | ≥ 1.32.0 | Web dashboard framework |
| Pandas | ≥ 2.0.0 | Data loading, filtering, aggregation |
| Plotly Express | ≥ 5.18.0 | Interactive charts |
| Groq SDK | ≥ 0.9.0 | GPT-OSS 120B AI API client (via Groq) |
| python-dotenv | ≥ 1.0.0 | Secure API key loading from `.env` |

---

## 📊 Dataset Description

**Filename:** `data/ecommerce_sales.csv` (raw) → `data/clean_ecommerce_sales.csv` (processed)

**Rows:** ~34,500 orders  
**Columns:** 17

| Column | Type | Description |
|---|---|---|
| `order_id` | string | Unique order identifier |
| `customer_id` | string | Unique customer identifier |
| `product_id` | string | Unique product identifier |
| `category` | categorical | Product category (Electronics, Home, Sports, Fashion, Beauty, Toys, Grocery) |
| `price` | float | Base unit price |
| `discount` | float | Discount fraction (0.0 – 1.0) |
| `quantity` | integer | Units ordered |
| `payment_method` | categorical | Payment type (Credit Card, UPI, etc.) |
| `order_date` | date | Date the order was placed |
| `delivery_time_days` | integer | Days taken to deliver |
| `region` | categorical | Geographic region (South, North, West, East, Central) |
| `returned` | string | Whether order was returned ("Yes" / "No") |
| `total_amount` | float | Revenue after discount |
| `shipping_cost` | float | Shipping cost for the order |
| `profit_margin` | float | Profit margin percentage |
| `customer_age` | integer | Age of the customer |
| `customer_gender` | categorical | Customer gender (Male / Female) |

**Dataset link:** To be provided / original dataset source.

---

## 📁 Project Structure

```
AI-Powered E-Commerce Sales & Customer Analytics/
│
├── app.py                                              ← Main Streamlit dashboard (run this)
├── analysis.py                                         ← Data exploration & preprocessing script
├── ai_engine.py                                        ← Groq LLM integration module
├── charts.py                                           ← Standalone Plotly chart prototyping
├── test_ai.py                                          ← Manual AI engine smoke test
│
├── RahulRathod_AI_Ecommerce_Sales_Customer_Analytics.py ← Submission copy of app.py
├── RahulRathod_ProjectReport.docx                      ← Full project report
│
├── requirements.txt                                    ← Python dependencies
├── .env                                                ← Secret API key (NOT committed to git)
├── .env.example                                        ← Template for environment variables
├── .gitignore                                          ← Git ignore rules
├── README.md                                           ← This file
│
└── data/
    ├── ecommerce_sales.csv                             ← Raw dataset
    └── clean_ecommerce_sales.csv                       ← Cleaned/enriched dataset
```

---

## ⚙️ Installation Instructions

### Prerequisites
- Python 3.10 or higher
- A free [Groq API key](https://console.groq.com)

### 1 — Clone / download the project

```bash
git clone <repository-url>
cd "AI-Powered E-Commerce Sales & Customer Analytics"
```

### 2 — Create a virtual environment

```bash
python -m venv venv
```

### 3 — Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4 — Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root (copy from `.env.example`):

```bash
copy .env.example .env        # Windows
cp .env.example .env          # macOS/Linux
```

Open `.env` and add your Groq API key:

```
GROQ_API_KEY=your_actual_groq_api_key_here
```

> ⚠️ **Never share or commit your `.env` file.** It is already listed in `.gitignore`.  
> Get a free key at: https://console.groq.com

---

## ▶️ How to Run the Application

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser at:  
`http://localhost:8501`

---

## 🖥️ How to Use the Dashboard

1. **Open the app** — the dashboard loads with all data visible by default
2. **Apply filters** — use the left sidebar to filter by Category, Region, Gender, or Payment Method
3. **Read the KPIs** — the 8 KPI cards at the top update immediately with filtered data
4. **Explore charts** — scroll down to view Monthly Trend, Category, Region, Payment, Gender, and Return charts
5. **Ask the AI** — scroll to the "Ask AI" section at the bottom, type a business question, and click **✨ Analyze with AI**

---

## 💬 Example AI Questions

- "Which category generates the highest revenue?"
- "What is the highest gender purchasing from this store?"
- "Which region has the best sales performance?"
- "What is the return rate and how can we reduce it?"
- "Which payment method is most popular?"
- "What recommendations do you have to increase profitability?"
- "How does delivery time affect customer returns?"

---

## 🔒 Important Security Notes

- Your real `GROQ_API_KEY` must only ever exist in the `.env` file
- `.env` is listed in `.gitignore` and will **not** be committed to version control
- `.env.example` contains only a placeholder value — **no real keys**
- No API keys are hardcoded anywhere in the Python source files
- Do not share your `.env` file publicly or include it in any submission ZIP

---

## 📈 Expected Output

When you run `streamlit run app.py` you should see:

- **Header:** "🛒 AI-Powered E-Commerce Sales & Customer Analytics"
- **Dataset caption:** showing record count (e.g., "Showing 34,500 of 34,500 records")
- **Row 1 KPIs:** Total Revenue ₹X | Total Orders X | Avg Order Value ₹X | Quantity Sold X
- **Row 2 KPIs:** Avg Delivery Time X days | Avg Profit Margin X% | Return Rate X% | Total Profit ₹X
- **Charts:** Monthly trend line → Category bar → Region bar → Payment donut + Gender bar → Return pie
- **AI Section:** Text input + "✨ Analyze with AI" button

---

## 👤 Author

**Rahul Rathod**  
AI-Powered E-Commerce Sales & Customer Analytics  
Python | Streamlit | Pandas | Plotly | Groq AI

---

*Built with Python, Streamlit, and Groq LLaMA 3 AI*
