#  ✅ 2_Current_Account.py

import streamlit as st
from datetime import date

st.set_page_config(page_title="Current Account", page_icon="🏦")

st.markdown("<h1 style='text-align: center; color: maroon;'>🏦 Current Account (No Profit)</h1>", unsafe_allow_html=True)

st.markdown("### 📝 Description:")
st.markdown("""
The current account is meant for **general users and businessmen** to deposit and withdraw amounts frequently without earning profit.
""")

st.markdown("#### 📌 Important Rules:")
st.markdown("""
1. No profit is offered.
2. Unlimited transactions allowed.
3. Meant for business use and flexibility.
""")

st.markdown("---")
st.markdown("### 📥 Account Details:")

account_number = st.text_input("Account Number", value="1234567890")
account_date = st.date_input("Account Generated Date", value=date.today())
investment_amount = st.number_input("Invested Amount", min_value=0)
balance = investment_amount

if st.button("💡 Calculate"):
    st.markdown("---")
    st.markdown("### 📊 **_Account Summary:_**")
    st.markdown(f"""
    <div style='color: darkcyan; font-style: italic; font-weight: bold;'>
    ✅ Account Number: {account_number} <br>
    ✅ Account Generated Date: {account_date} <br>
    ✅ Invested Amount: {investment_amount} <br>
    ✅ Current Balance: {balance} <br>
    ✅ Deposit Terms: Flexible <br>
    ✅ Withdrawal Terms: Flexible <br>
    ✅ Transaction Limit: Flexible
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<span style='color: crimson; font-style: italic; font-weight: bold;'>📌 Note: Depositors can deposit unlimited amounts with proof and withdraw multiple times without conditions to ensure fast transactions.</span>", unsafe_allow_html=True)


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
