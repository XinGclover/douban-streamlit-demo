import streamlit as st
import pandas as pd
from core.demo_db import demo_select_df
import plotly.express as px



st.title("📊 Statistic of Douban User")

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Reply User Distribution")

kpi_df = demo_select_df(
    """
    SELECT
        COUNT(DISTINCT user_id) AS total_users,
        COALESCE(SUM(reply_count), 0) AS total_replies,
        COALESCE(MAX(reply_count), 0) AS max_reply
    FROM demo_reply_users_distribution
    """
)
#st.dataframe(kpi_df)     #table

total_users = int(kpi_df["total_users"][0])
total_replies = int(kpi_df["total_replies"][0])
max_reply = int(kpi_df["max_reply"][0])


col1, col2, col3 = st.columns(3)

col1.metric("Total Group Members", total_users)
col2.metric("Total Replies", total_replies)
col3.metric("Top Members Replies", max_reply)

st.divider()
#st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Low Rating User Distribution")

df1 = demo_select_df(
    """
    SELECT *
    FROM demo_lowrating_users_distribution
    ORDER BY user_cnt DESC
    LIMIT 20
    """ 
)
fig = px.bar(
    df1,
    x="user_cnt",
    y="group_name",  
    hover_data=["group_who"],
)
st.plotly_chart(fig, use_container_width=True)
st.divider()
#st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Low Rating User Distribution by High Rating Drama")

df2 = demo_select_df(
    """
    SELECT 
    high_rating_user_count AS user_cnt,
    drama_name
    FROM demo_high_rating_dramas_source_zhaoxuelu
    ORDER BY high_rating_user_count DESC
    LIMIT 20
    """ 
)
fig = px.bar(
    df2,
    x="user_cnt",
    y="drama_name",  
)
st.plotly_chart(fig, use_container_width=True)




