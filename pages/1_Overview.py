import streamlit as st
import pandas as pd
from core.demo_db import demo_select_df

st.title("Reply User Distribution")



kpi_df = demo_select_df(
    """
    SELECT
        COUNT(*) AS total_users,
        COALESCE(SUM(reply_count), 0) AS total_replies,
        COALESCE(MAX(reply_count), 0) AS max_reply
    FROM demo_reply_users_distribution
    """
)
st.dataframe(kpi_df)



total_users = int(kpi_df["total_users"][0])
total_replies = int(kpi_df["total_replies"][0])
max_reply = int(kpi_df["max_reply"][0])


col1, col2, col3 = st.columns(3)

col1.metric("Total Users", total_users)
col2.metric("Total Replies", total_replies)
col3.metric("Top User Replies", max_reply)

min_replies = st.slider("Minimum reply count", 1, 200, 10)

chart_query = demo_select_df(f"""
SELECT user_name, reply_count
FROM demo_reply_users_distribution
WHERE reply_count >= {min_replies}
ORDER BY reply_count DESC
LIMIT 20
""")

st.bar_chart(chart_query.set_index("user_name"))







