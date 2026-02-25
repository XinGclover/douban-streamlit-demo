import streamlit as st
import pandas as pd
from core.demo_db import demo_select_df

st.set_page_config(page_title="Query", layout="wide")
st.title("🔎 Query")


tab1, tab2 = st.tabs(["Reply users", "Low-rating users"])

with tab1:
    st.subheader("Lookup in Reply User Membership")
    user_id = st.text_input("user_id", placeholder="e.g. 239300232", key="reply_uid")

    if user_id:
        df = demo_select_df(
            """
            SELECT *
            FROM demo_reply_users_distribution
            WHERE user_id = ?
            """,
            params=[user_id],
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.caption("Enter a user_id to query.")

#with tab2:
  