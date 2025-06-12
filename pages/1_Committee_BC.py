#  ✅ 1_Committee_BC.py

import streamlit as st
from datetime import date

st.set_page_config(page_title="Committee / BC", page_icon="🤝")

st.markdown("<h1 style='text-align: center; color: darkblue;'>🤝 Committee / BC (No Profit)</h1>", unsafe_allow_html=True)

st.markdown("### 📝 Description:")
st.markdown("""
This system is designed locally among the community to **help and support each other** and achieve saving goals on a monthly basis.
""")

st.markdown("---")
st.markdown("### 📥 Enter Committee Details:")

receive_turn = st.number_input("Turn to receive amount of commetti", min_value=1)
investment_amount = st.number_input("Investment Amount", min_value=0)
num_investors = st.number_input("Number Of Persons Investing", min_value=1)
start_date = st.date_input("Date of Starting Commetti", value=date.today())
end_date = st.date_input("Date of End", value=date.today().replace(year=date.today().year + 1))

if st.button("💡 Calculate"):
    total_received = investment_amount * num_investors

    st.markdown("---")
    st.markdown("### 📊 **_Committee Summary:_**")
    st.markdown(f"""
    <div style='color: green; font-style: italic; font-weight: bold;'>
    ✅ Turn to receive amount: {receive_turn} <br>
    ✅ Investment Amount: {investment_amount} <br>
    ✅ Number Of Persons Investing: {num_investors} <br>
    ✅ Start Date: {start_date} <br>
    ✅ End Date: {end_date} <br>
    ✅ Total Commetti Amount to Receive: {total_received}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<span style='color: crimson; font-style: italic; font-weight: bold;'>📌 Note: Complete the cycle of commetti, respect each other, and pay the amount on time.</span>", unsafe_allow_html=True)

    # Author signature
st.markdown("<p style='text-align: center; color: blue; font-style: italic;'>Author: Azmat Ali Akbar</p>", unsafe_allow_html=True)
