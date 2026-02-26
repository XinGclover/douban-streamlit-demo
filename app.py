import streamlit as st
from pathlib import Path


st.set_page_config(page_title="Fandom Behavior Analytics Demo", layout="wide")
st.title("🎭 Fandom Behavior Analytics Demo")

svg_path = Path("assets/architecture.svg")
svg_content = svg_path.read_text()

st.image("assets/architecture.svg")

st.markdown(
    """
    ## What this demo shows

    This Streamlit demo visualizes precomputed analytics tables derived from a larger data pipeline.

    ## Pipeline (full project)

    Scraping → PostgreSQL (raw) → LLM labeling → SQL views (analytics layer) → **Materialized demo tables** → Streamlit  
    The online demo presents only the materialized analytics layer.

    ## Why materialize into demo tables?

    - Keeps the demo lightweight and reproducible
    - Decouples the presentation layer from scraping/LLM runtime dependencies
    - Avoids exposing cookies, scrapers, or private raw data

    ## Tables in this demo

    - `demo_reply_users_distribution`: reply activity ranking + group memberships
    - `demo_lowrating_users_distribution`: users associated with low-rating patterns (precomputed)
    - `demo_high_rating_dramas_source_zhaoxuelu`: curated high-rating drama dataset (precomputed)
    """,
    unsafe_allow_html=True,
)
