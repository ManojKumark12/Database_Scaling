import psycopg2
from psycopg2.extras import execute_batch
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file
def connect_to_db():
    conn = psycopg2.connect(
    database=os.getenv("DATABASE"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT")
            )
    return conn
def execute_query(query, params=None, rows='multiple'):
    try:
        with connect_to_db() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)

                if query.strip().lower().startswith("select"):
                    return cur.fetchone() if rows == 'single' else cur.fetchall()
                else:
                    conn.commit()
                    return cur.rowcount

    except Exception as e:
        print("Error:", e)
        return None
def execute_batch_query(query,params):
    try:
        with connect_to_db() as conn:
            with conn.cursor() as cur:
                execute_batch(cur, query, params)
                conn.commit()
                return cur.rowcount

    except Exception as e:
        print("Error:", e)
        return None

def bulk_insert():
    data = [
        (f"Product{i}",  json.dumps({
            "color": "blue",
            "size": "L",
            "price": i
        }))
        for i in range(1_00_000)
    ]
    res=execute_batch_query(
        '''
        INSERT INTO products (name, metadata) VALUES (%s, %s);
        ''',
        data
    )
    return res