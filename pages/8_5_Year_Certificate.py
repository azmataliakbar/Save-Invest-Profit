import streamlit as st
from datetime import date

st.set_page_config(page_title="5-Year Certificate", page_icon="📅")

st.markdown("""
<h1 style='text-align: center; color: darkblue;'>
📅 5-Year Certificate Scheme<br>(With Profit)
</h1>
""", unsafe_allow_html=True)


st.markdown("### 📝 Description:")
st.markdown("""
The **5-Year Certificate** provides maximum long-term profit with compound annual returns or maturity benefits. Ideal for long-term financial planning.
""")

st.markdown("#### 📌 Key Features:")
st.markdown("""
- Fixed term of 5 years.
- Profits usually paid annually or at maturity.
- Highest cumulative return among certificate options.
- Applicable tax for filers and non-filers.
""")

st.markdown("---")
st.markdown("### 📥 Enter Certificate Details:")

account_number = st.text_input("Account Number", value="CERT-5Y-0005")
account_date = st.date_input("Account Start Date", value=date.today())
investment_amount = st.number_input("Invested Amount (Rs.)", min_value=0)
annual_profit_percent = st.number_input("Annual Profit %", min_value=0.0, step=0.1)

if st.button("📊 Calculate"):
    # Total profit over 5 years
    total_profit = (investment_amount * annual_profit_percent * 5) / 100

    # Tax calculations
    tax_filer = (total_profit * 17) / 100
    tax_non_filer = (total_profit * 37) / 100

    # Net profits
    net_filer = total_profit - tax_filer
    net_non_filer = total_profit - tax_non_filer

    # Calculate maturity date (5 years later)
    maturity_date = date(account_date.year + 5, account_date.month, account_date.day)

    st.markdown("---")
    st.markdown("### 📈 **_Certificate Summary:_**")
    st.markdown(f"""
    <div style='color: blue; font-weight: bold; font-style: italic;'>
    ✅ Account No: {account_number} <br>
    ✅ Purchase Date: {account_date} <br>
    ✅ Maturity Date: {maturity_date} <br>
    ✅ Invested Amount: Rs. {investment_amount:,} <br>
    ✅ Annual Profit Rate: {annual_profit_percent}% <br><br>

    💰 Total Profit (5 Years): Rs. {total_profit:,.2f} <br>
    🔖 Tax (Filer - 17%): Rs. {tax_filer:,.2f} <br>
    🔖 Tax (Non-Filer - 37%): Rs. {tax_non_filer:,.2f} <br><br>

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
