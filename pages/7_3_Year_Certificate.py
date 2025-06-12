import streamlit as st
from datetime import date

st.set_page_config(page_title="3-Year Certificate", page_icon="📆")

st.markdown("""
<h1 style='text-align: center; color: darkgreen;'>
📆 3-Year Certificate Scheme<br>(With Profit)
</h1>
""", unsafe_allow_html=True)

st.markdown("### 📝 Description:")
st.markdown("""
The **3-Year Certificate** offers a higher cumulative return with profits paid annually or at maturity. It's ideal for medium to long-term investment plans.
""")

st.markdown("#### 📌 Key Features:")
st.markdown("""
- Fixed term of 3 years.
- Annual profit or maturity-based return.
- Higher total return than short-term certificates.
- Tax based on filer status.
""")

st.markdown("---")
st.markdown("### 📥 Enter Certificate Details:")

account_number = st.text_input("Account Number", value="CERT-3Y-0004")
account_date = st.date_input("Account Start Date", value=date.today())
investment_amount = st.number_input("Invested Amount (Rs.)", min_value=0)
annual_profit_percent = st.number_input("Annual Profit %", min_value=0.0, step=0.1)

if st.button("📈 Calculate"):
    # Annual profit calculation
    total_profit = (investment_amount * annual_profit_percent * 3) / 100

    # Taxes
    tax_filer = (total_profit * 15) / 100
    tax_non_filer = (total_profit * 35) / 100

    # Net Profit
    net_filer = total_profit - tax_filer
    net_non_filer = total_profit - tax_non_filer

    # Calculate maturity date (3 years later)
    maturity_date = date(account_date.year + 3, account_date.month, account_date.day)

    st.markdown("---")
    st.markdown("### 📊 **_Certificate Summary:_**")
    st.markdown(f"""
    <div style='color: green; font-style: italic; font-weight: bold;'>
    ✅ Account No: {account_number} <br>
    ✅ Purchase Date: {account_date} <br>
    ✅ Maturity Date: {maturity_date} <br>
    ✅ Invested: Rs. {investment_amount:,} <br>
    ✅ Profit Rate (Annual): {annual_profit_percent}% <br><br>

    💵 Total Profit (3 Years): Rs. {total_profit:,.2f} <br>
    🔖 Tax (15%) for Filer: Rs. {tax_filer:,.2f} <br>
    🔖 Tax (35%) for Non-Filer: Rs. {tax_non_filer:,.2f} <br><br>

    ✅ Net Profit (Filer): Rs. {net_filer:,.2f} <br>
    ✅ Net Profit (Non-Filer): Rs. {net_non_filer:,.2f}
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

