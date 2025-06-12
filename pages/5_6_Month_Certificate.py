import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="6-Months Certificate", page_icon="🗓️")

st.markdown("<h1 style='text-align: center; color: darkgreen;'>🗓️ 6-Month Certificate Scheme (With Profit)</h1>", unsafe_allow_html=True)

st.markdown("### 📝 Description:")
st.markdown("""
This **6-Month Certificate** offers a secure return on a mid-term investment. Profits are usually paid at maturity with tax applied based on filer status.
""")

st.markdown("#### 📌 Key Features:")
st.markdown("""
- Fixed duration: 6 months.
- Profit calculated at the end.
- Tax differences for filers and non-filers.
- Good for individuals who don't want to lock funds for too long.
""")

st.markdown("---")
st.markdown("### 📥 Enter Certificate Details:")

account_number = st.text_input("Account Number", value="CERT-6M-0002")
account_date = st.date_input("Account Start Date", value=date.today())
investment_amount = st.number_input("Invested Amount (Rs.)", min_value=0)
profit_percent = st.number_input("Profit % for 1 Year", min_value=0.0, step=0.1)

if st.button("💡 Calculate"):
    # Profit Calculation
    profit_amount = (investment_amount * profit_percent) / 100

    # Taxes
    tax_filer = (profit_amount * 15) / 100
    tax_non_filer = (profit_amount * 35) / 100

    # Net Profit
    net_filer = (profit_amount - tax_filer) / 2
    net_non_filer = (profit_amount - tax_non_filer) / 2

    # Calculate maturity date (6 Months later)
    maturity_date = account_date + relativedelta(months=6)

    st.markdown("---")
    st.markdown("### 📊 **_Certificate Summary:_**")
    st.markdown(f"""
    <div style='color: green; font-style: italic; font-weight: bold;'>
    ✅ Account No: {account_number} <br>
    ✅ Purchase Date: {account_date} <br>
    ✅ Maturity Date: {maturity_date} <br>
    ✅ Invested: Rs. {investment_amount:,} <br>
    ✅ Profit Rate (6-Month): {profit_percent}% <br><br>

    💵 Profit Earned On 1 Year Basis: Rs. {profit_amount:,.2f} <br>
    🔖 Tax (15%) for Filer: Rs. {tax_filer:,.2f} <br>
    🔖 Tax (35%) for Non-Filer: Rs. {tax_non_filer:,.2f} <br><br>

    ✅ Net Profit After 6 Months (Filer): Rs. {net_filer:,.2f} <br>
    ✅ Net Profit After 6 Months (Non-Filer): Rs. {net_non_filer:,.2f}
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
