import streamlit as st
import pandas as pd
from core.demo_db import demo_select_df

st.set_page_config(page_title="Query", layout="wide")
st.title("🔎 Query")

DEFAULT_REPLY_UID = "289367372"   
DEFAULT_LOW_UID = "289367372"

tab1, tab2 = st.tabs(["Member Groups", "Low-rating users"])

with tab1:
    st.subheader("Lookup in Member Groups")
    user_id = st.text_input(
        "user_id", 
        placeholder=f"e.g. {DEFAULT_REPLY_UID}",
        key="reply_uid"
    )

    effective_id = (user_id or "").strip() or DEFAULT_REPLY_UID

    df = demo_select_df(
        """
        SELECT *
        FROM demo_member_groups
        WHERE member_id = ?
        """,
        params=[effective_id],
    )

    
    if (user_id or "").strip() == "":
        st.caption(f"Showing example result for user_id={DEFAULT_REPLY_UID}. Type another id to update.")
    else:
        st.caption(f"Showing result for user_id={effective_id}.")
    st.dataframe(df, use_container_width=True)

#with tab2:
  