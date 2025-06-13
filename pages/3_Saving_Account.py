import streamlit as st
from datetime import date

st.set_page_config(page_title="Saving Account", page_icon="💰")

st.markdown("""
<h1 style='text-align: center; color: darkgreen;'>
💰 Saving Account (Profit-Based)
</h1>
""", unsafe_allow_html=True)

st.markdown("### 📝 Description:")
st.markdown("""
A **Saving Account** allows the account holder to deposit and withdraw money while **earning profit** monthly or quarterly, depending on the bank’s policies.
""")

st.markdown("#### 📌 Key Features:")
st.markdown("""
- Offers monthly/quarterly profit.
- Ideal for individuals saving for future goals.
- Limited transactions compared to Current Account.
""")

st.markdown("---")
st.markdown("### 📥 Enter Account Details:")

account_number = st.text_input("Account Number", value="SAV123456")
account_date = st.date_input("Account Opened Date", value=date.today())
investment_amount = st.number_input("Initial Deposit (Rs.)", min_value=0)
expected_rate = st.number_input("Expected Annual Profit Rate (%)", min_value=0.0, step=0.1)
months = st.number_input("Fixed Profit Term (Months)", min_value=1)


filer_status = st.radio("Are you a Filer?", ["Yes (17% Tax)", "No (37% Tax)"])

if st.button("💡 Calculate"):
    # Profit calculation
    total_profit = investment_amount * (expected_rate / 100) * (months / 12)

    # Tax logic
    tax_rate = 0.17 if filer_status == "Yes (17% Tax)" else 0.37
    tax_deducted = total_profit * tax_rate
    profit_after_tax = total_profit - tax_deducted
    total_balance_after_tax = investment_amount + profit_after_tax

    st.markdown("---")
    st.markdown("### 📊 **_Savings Summary:_**")
    st.markdown(f"""
    <div style='color: blue; font-style: italic; font-weight: bold;'>
    ✅ Account Number: {account_number} <br>
    ✅ Account Opened On: {account_date} <br>
    ✅ Invested Amount: Rs. {investment_amount:,.2f} <br>
    ✅ Profit Rate: {expected_rate}% <br>
    ✅ Duration: {months} Month(s) <br><br>

    💰 Gross Profit: Rs. {total_profit:,.2f} <br>
    🧾 Tax Deducted ({int(tax_rate*100)}%): Rs. {tax_deducted:,.2f} <br>
    💸 Net Profit After Tax: Rs. {profit_after_tax:,.2f} <br><br>

    🟢 Total Balance After Tax: Rs. {total_balance_after_tax:,.2f}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<span style='color: crimson; font-style: italic; font-weight: bold;'>📌 Note: Withdrawals may impact your profit. Keep funds for the selected duration to earn full returns.</span>", unsafe_allow_html=True)

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
