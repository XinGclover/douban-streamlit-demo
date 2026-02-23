import streamlit as st

st.set_page_config(page_title="Methodology", layout="wide")
st.title("🧭 Methodology")

st.markdown(
"""
## What this demo shows

This Streamlit demo visualizes precomputed analytics tables derived from a larger data pipeline.

## Pipeline (full project)

Scraping → PostgreSQL (raw) → LLM labeling → SQL views (analytics layer) → **Materialized demo tables** → Streamlit

## Why materialize into demo tables?

- Keeps the demo lightweight and reproducible
- Decouples the presentation layer from scraping/LLM runtime dependencies
- Avoids exposing cookies, scrapers, or private raw data

## Tables in this demo

- `demo_reply_users_distribution`: reply activity ranking + group memberships
- `demo_lowrating_users_distribution`: users associated with low-rating patterns (precomputed)
- `demo_high_rating_dramas_source_zhaoxuelu`: curated high-rating drama dataset (precomputed)

"""
)
