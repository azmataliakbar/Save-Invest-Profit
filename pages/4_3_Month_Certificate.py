import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="3-Months Certificate", page_icon="📄")

st.markdown("<h1 style='text-align: center; color: teal;'>📄 3-Month Certificate Scheme (With Profit)</h1>", unsafe_allow_html=True)

st.markdown("### 📝 Description:")
st.markdown("""
This **3-Months Certificate Scheme** provides short-term profit on a fixed investment. It's commonly used for quick returns under **bank rules or private finance organizations**.
""")

st.markdown("#### 📌 Key Features:")
st.markdown("""
1. Fixed 3-month duration.
2. Profit calculated once at end of term.
3. Tax deduction based on filer status.
4. Returns deposited back to account.
""")

st.markdown("---")
st.markdown("### 📥 Enter Certificate Details:")

account_number = st.text_input("Account Number", value="CERT-3M-0001")
account_date = st.date_input("Account Start Date", value=date.today())
investment_amount = st.number_input("Invested Amount (Rs.)", min_value=0)
profit_percent = st.number_input("Profit % for 3 Months", min_value=0.0, step=0.1)

if st.button("💡 Calculate"):
    # Profit
    profit_amount = (investment_amount * profit_percent) / 100

    # Tax
    tax_filer = (profit_amount * 15) / 100
    tax_non_filer = (profit_amount * 35) / 100

    # Net Profit
    net_filer = (profit_amount - tax_filer) / 3
    net_non_filer = (profit_amount - tax_non_filer) / 3

    # Calculate maturity date (6 Months later)
    maturity_date = account_date + relativedelta(months=3)

    st.markdown("---")
    st.markdown("### 📊 **_Certificate Summary:_**")
    st.markdown(f"""
    <div style='color: teal; font-style: italic; font-weight: bold;'>
    ✅ Account No: {account_number} <br>
    ✅ Purchase Date: {account_date} <br>
    ✅ Maturity Date: {maturity_date} <br>
    ✅ Invested: Rs. {investment_amount:,} <br>
    ✅ Profit Rate (1-Year): {profit_percent}% <br><br>

    💵 Profit Earned On 1 Year basis: Rs. {profit_amount:,.2f} <br>
    🔖 Tax (15%) for Filer: Rs. {tax_filer:,.2f} <br>
    🔖 Tax (35%) for Non-Filer: Rs. {tax_non_filer:,.2f} <br><br>

    ✅ Net Profit After 3 Months (Filer): Rs. {net_filer:,.2f} <br>
    ✅ Net Profit After 3 Months (Non-Filer): Rs. {net_non_filer:,.2f}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='color: crimson; font-style: italic; font-weight: bold;'>
    📌 Note: Recheck profit rates with your bank. Tax rules may change annually.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='color: crimson; font-style: italic; font-weight: bold;'>
    📌 Note: Please follow your institution's rules. Confirm latest tax policies with authorized personnel. <br>
    ✅ KYC (Know Your Customer) is required. <br>
    ✅ Income Certificate may be needed.
    </div>
    """, unsafe_allow_html=True)

    # Author signature
st.markdown("<p style='text-align: center; color: blue; font-style: italic;'>Author: Azmat Ali Akbar</p>", unsafe_allow_html=True)
