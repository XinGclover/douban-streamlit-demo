from __future__ import annotations

import os
from pathlib import Path
import pandas as pd
import duckdb
from core.db import get_conn

TABLES = [
    "demo_reply_users_distribution",
    "demo_lowrating_users_distribution",
    "demo_high_rating_dramas_source_zhaoxuelu",
]

OUT_PATH = Path(__file__).resolve().parent / "demo.duckdb"


def load_table(pg_conn, table_name: str) -> pd.DataFrame:
    return pd.read_sql(f'SELECT * FROM public."{table_name}"', pg_conn)


def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    pg = get_conn()

    print(f"[2/3] Create DuckDB: {OUT_PATH}")
    con = duckdb.connect(str(OUT_PATH))
    con.execute("PRAGMA threads=4;")

    for t in TABLES:
        print(f"  - Export table: {t}")
        df = load_table(pg, t)

        # Overwrite if exists
        con.execute(f'DROP TABLE IF EXISTS "{t}"')
        con.register("df_tmp", df)
        con.execute(f'CREATE TABLE "{t}" AS SELECT * FROM df_tmp')
        con.unregister("df_tmp")

        # Optional: Simple sanity check
        cnt = con.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0]
        print(f"    rows: {cnt}")

    con.close()
    pg.close()
    print(f"[3/3] Done. File generated: {OUT_PATH}")


if __name__ == "__main__":
    main()