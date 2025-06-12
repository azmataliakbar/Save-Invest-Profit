# ← Main app file (with sidebar and navigation)

# calculate_profit/
# │
# ├── app.py                        ← Main app file (with sidebar and navigation)
# ├── assets/                       ← Folder for icons/images
# ├── styles/                       ← (Optional) for custom CSS if needed
# └── pages/                        ← Contains all your functional pages
#     ├── 1_Committee_BC.py
#     ├── 2_Current_Account.py
#     ├── 3_Saving_Account.py
#     ├── 4_3_Month_Certificate.py
#     ├── 5_6_Month_Certificate.py
#     ├── 6_1_Year_Certificate.py
#     ├── 7_3_Year_Certificate.py
#     └── 8_5_Year_Certificate.py

# app.py

import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Calculate Profit", page_icon="💰", layout="wide")

# Main heading
st.markdown("""
    <h1 style='text-align: center; color: green; font-size: 48px;'>
        💰 Calculate Profit 💰
    </h1>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 📊 Select a Profit Calculation Page")
st.sidebar.page_link("pages/1_Committee_BC.py", label="1. Committee / BC", icon="🧾")
st.sidebar.page_link("pages/2_Current_Account.py", label="2. Current Account (No Profit)", icon="🏦")
st.sidebar.page_link("pages/3_Saving_Account.py", label="3. Saving Account (With Profit)", icon="💹")
st.sidebar.page_link("pages/4_3_Month_Certificate.py", label="4. 3 Months Certificate Scheme", icon="📅")
st.sidebar.page_link("pages/5_6_Month_Certificate.py", label="5. 6 Months Certificate Scheme", icon="📅")
st.sidebar.page_link("pages/6_1_Year_Certificate.py", label="6. 1 Year Certificate Scheme", icon="🕐")
st.sidebar.page_link("pages/7_3_Year_Certificate.py", label="7. 3 Year Certificate Scheme", icon="📈")
st.sidebar.page_link("pages/8_5_Year_Certificate.py", label="8. 5 Year Certificate Scheme", icon="📈")

# Default message
st.markdown("### 👈 Select a page from the sidebar to begin your profit calculation.")
st.markdown("""
### 💰 This App gives an idea of 💰 :
- **Saving**
- **Investment**
- **Profit** 
""")

# Descriptions
st.markdown("""
---

### 🕌 **1. Islamic Shariah Investment:**
- The **percentage of profit** varies on a **monthly basis**.
- Banks disclose the **actual profit rate** and amount each month.
- Based on **Mudarabah** or **other Islamic finance principles**, avoiding interest (Riba).

---

### 🏦 **2. Conventional Investment:**
- Offers a **fixed profit rate** decided by the bank.
- Rate is usually **locked** based on the **prevailing economic conditions** at the time of investment.
- Suitable for individuals preferring **predictable returns** over variable ones.

---
""", unsafe_allow_html=True)

# Author signature
st.markdown("<p style='text-align: center; color: blue; font-style: italic;'>Author: Azmat Ali Akbar</p>", unsafe_allow_html=True)