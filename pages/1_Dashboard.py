import streamlit as st
import pandas as pd
from core.demo_db import demo_select_df
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots



st.title("📊 Statistic of Douban User")

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🧮 Reply User Distribution")

kpi_query = """
    SELECT
        COUNT(DISTINCT user_id) AS total_users,
        COALESCE(SUM(reply_count), 0) AS total_replies,
        COALESCE(MAX(reply_count), 0) AS max_reply
    FROM demo_reply_users_distribution
    """

df1_query = """
    SELECT *
    FROM demo_lowrating_users_distribution
    ORDER BY user_cnt DESC
    LIMIT 20
    """ 

df2_query = """
    SELECT 
    high_rating_user_count AS user_cnt,
    drama_name
    FROM demo_high_rating_dramas_source_zhaoxuelu
    ORDER BY high_rating_user_count DESC
    LIMIT 20
    """ 

df3_query = """
    SELECT user_id, ip_location, reply_count
    FROM demo_reply_users_distribution
    WHERE ip_location IS NOT NULL
    AND reply_count IS NOT NULL
    """

df4_query = """
    SELECT
        user_id,
        reply_count,
        trim(w) AS group_who
    FROM demo_reply_users_distribution,
    UNNEST(group_whos) AS t(w)
    WHERE group_whos IS NOT NULL
      AND w IS NOT NULL
      AND trim(w) <> ''
    """
df5_query = """
    SELECT
        user_location,
        rating,
        COUNT(*) AS cnt
    FROM demo_zhaoxuelu_comments
    WHERE user_location IS NOT NULL AND user_location <> ''
    GROUP BY user_location, rating
    """

df6_query = """
    SELECT
        user_location,
        COUNT(*) AS total,
        AVG(rating)::float AS avg_rating,
        SUM(CASE WHEN rating <= 2 THEN 1 ELSE 0 END)::float / COUNT(*) AS low_ratio,
        SUM(CASE WHEN rating >= 4 THEN 1 ELSE 0 END)::float / COUNT(*) AS high_ratio
    FROM demo_zhaoxuelu_comments
    WHERE user_location IS NOT NULL AND user_location <> ''
    GROUP BY user_location
    HAVING COUNT(*) >= 50
    ORDER BY total DESC
    """
#st.dataframe(kpi_df)     #table

kpi_df = demo_select_df(kpi_query)
total_users = int(kpi_df["total_users"][0])
total_replies = int(kpi_df["total_replies"][0])
max_reply = int(kpi_df["max_reply"][0])


col1, col2, col3 = st.columns(3)

col1.metric("Total Reply Users", total_users)
col2.metric("Total Replies", total_replies)
col3.metric("Top Members Replies", max_reply)

st.divider()
#st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("📊 Low Rating User Membership Distribution")

    df1 = demo_select_df(df1_query)
    fig = px.bar(
        df1,
        x="user_cnt",
        y="group_name",  
        hover_data=["group_who"],
    )
    st.plotly_chart(fig, use_container_width=True)
 
    #st.markdown("<br>", unsafe_allow_html=True)

with col2:
    st.subheader("📊 Low Rating User High Rating Drama Distribution")

    df2 = demo_select_df(df2_query)
    fig = px.bar(
        df2,
        x="user_cnt",
        y="drama_name",  
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("📈 Zhaoxuelu Comments Rating Location Distribution")
df5 = demo_select_df(df5_query)
df6 = demo_select_df(df6_query)


TOP_N = 20
top_locs = df6["user_location"].head(TOP_N).tolist()

df_dist = df5[df5["user_location"].isin(top_locs)]
df_metric = df6[df6["user_location"].isin(top_locs)]

# 4) Unified regional order 
order = top_locs

# 5) Draw a composite chart: Left axis = number of people (stacked bars), right axis = indicator (line).
fig = make_subplots(specs=[[{"secondary_y": True}]])

for r in [1, 2, 3, 4, 5]:
    sub = df_dist[df_dist["rating"] == r].set_index("user_location").reindex(order).fillna(0)
    fig.add_trace(
        go.Bar(x=order, y=sub["cnt"], name=f"{r}⭐"),
        secondary_y=False
    )

# Linear graph: Average score (1~5)
m = df_metric.set_index("user_location").reindex(order)
fig.add_trace(
    go.Scatter(x=order, y=m["avg_rating"], mode="lines+markers", name="Avg rating"),
    secondary_y=True
)

# Line graph: Low score ratio / High score ratio (0~1)
fig.add_trace(
    go.Scatter(x=order, y=m["low_ratio"], mode="lines+markers", name="Low ratio (<=2)"),
    secondary_y=True
)
fig.add_trace(
    go.Scatter(x=order, y=m["high_ratio"], mode="lines+markers", name="High ratio (>=4)"),
    secondary_y=True
)

fig.update_layout(
    title="Rating distribution by location + metrics",
    barmode="stack",
    xaxis_title="Location",
    yaxis_title="Count",
    legend_title="",
    xaxis_tickangle=-90,
)

fig.update_yaxes(title_text="Count", secondary_y=False)
fig.update_yaxes(title_text="Avg / Ratios", secondary_y=True, rangemode="tozero")

st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("📈 Reply Count Statistics by Region")
 

df3 = demo_select_df(df3_query)
top_regions = df3["ip_location"].value_counts().head(20).index
df_top = df3[df3["ip_location"].isin(top_regions)]

# log scale → clearer distribution structure
df_top["log_reply"] = np.log1p(df_top["reply_count"])

fig = px.box(
    df_top,
    x="ip_location",
    y="log_reply",
    points=False
)
fig.update_xaxes(tickangle=-45)
# fig.update_layout(
#     yaxis_range=[0.5, 2.5]  # focus on 1-10 replies (log scale)
# )

st.plotly_chart(fig, use_container_width=True)


region_summary = (
    df3.groupby("ip_location")["reply_count"]
    .describe()
    .sort_values("count", ascending=False)
)

with st.expander("📊 Statistical Summary (describe)"):
    st.dataframe(region_summary, use_container_width=True)

median_table = (
    df3.groupby("ip_location")["reply_count"]
    .median()
    .sort_values(ascending=False)
    .rename("median_reply_count")
    .reset_index()
)

with st.expander("📊 Median reply_count by region"):
    st.dataframe(median_table, use_container_width=True)
st.markdown("<br>", unsafe_allow_html=True)


st.divider()
st.subheader("📈 Reply Count Statistics by Star Group")

df4 = demo_select_df(df4_query)

# Clean data by dropping rows where group_who or reply_count is null
df4 = df4.dropna(subset=["group_who", "reply_count"])

top_n = 20
top_groups = (
    df4["group_who"]
    .value_counts()
    .head(top_n)
    .index
)
df_topg = df4[df4["group_who"].isin(top_groups)].copy()

df_topg["log_reply"] = np.log1p(df_topg["reply_count"])

fig = px.box(
    df_topg,
    x="group_who",
    y="log_reply",
    points=False
)
fig.update_layout(
    xaxis_tickangle=-90   
)

st.plotly_chart(fig, use_container_width=True)

