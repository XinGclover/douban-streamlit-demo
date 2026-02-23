from pathlib import Path
import duckdb
import pandas as pd

# Define the path to the DuckDB database file
DB_PATH = Path(__file__).resolve().parents[1] / "demo.duckdb"

def demo_select_df(sql: str, params=None) -> pd.DataFrame:
    con = duckdb.connect(str(DB_PATH), read_only=True)
    try:
        if params:
            return con.execute(sql, params).df()
        return con.execute(sql).df()
    finally:
        con.close()