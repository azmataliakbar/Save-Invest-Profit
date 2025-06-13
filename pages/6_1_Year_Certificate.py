import streamlit as st
from datetime import date

st.set_page_config(page_title="1-Year Certificate", page_icon="📅")

st.markdown("""
<h1 style='text-align: center; color: teal;'>
📅 1-Year Certificate Scheme<br>(With Profit)
</h1>
""", unsafe_allow_html=True)


st.markdown("### 📝 Description:")
st.markdown("""
The **1-Year Certificate** offers an annual return with a higher profit rate compared to shorter certificates. Ideal for individuals who can invest for 12 months.
""")

st.markdown("#### 📌 Key Features:")
st.markdown("""
- Fixed 1-year term.
- Profit paid at maturity.
- Tax deducted based on filer/non-filer status.
- Suitable for mid-to-long term savings.
""")

st.markdown("---")
st.markdown("### 📥 Enter Certificate Details:")

account_number = st.text_input("Account Number", value="CERT-1Y-0003")
account_date = st.date_input("Account Start Date", value=date.today())
investment_amount = st.number_input("Invested Amount (Rs.)", min_value=0)
profit_percent = st.number_input("Annual Profit %", min_value=0.0, step=0.1)

if st.button("💡 Calculate"):
    # Profit Calculation
    profit_amount = (investment_amount * profit_percent) / 100

    # Taxes
    tax_filer = (profit_amount * 17) / 100
    tax_non_filer = (profit_amount * 37) / 100

    # Net Profit
    net_filer = profit_amount - tax_filer
    net_non_filer = profit_amount - tax_non_filer

    # Calculate maturity date (3 years later)
    maturity_date = date(account_date.year + 1, account_date.month, account_date.day)

    st.markdown("---")
    st.markdown("### 📊 **_Certificate Summary:_**")
    st.markdown(f"""
    <div style='color: teal; font-style: italic; font-weight: bold;'>
    ✅ Account No: {account_number} <br>
    ✅ Purchase Date: {account_date} <br>
    ✅ Maturity Date: {maturity_date} <br>
    ✅ Invested: Rs. {investment_amount:,} <br>
    ✅ Profit Rate (1-Year): {profit_percent}% <br><br>

    💵 Profit Earned: Rs. {profit_amount:,.2f} <br>
    🔖 Tax (17%) for Filer: Rs. {tax_filer:,.2f} <br>
    🔖 Tax (37%) for Non-Filer: Rs. {tax_non_filer:,.2f} <br><br>

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