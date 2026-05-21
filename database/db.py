import psycopg2

def create_connection():

    conn = psycopg2.connect(
        host="ep-square-mud-apxzsymt.c-7.us-east-1.aws.neon.tech",
        database="neondb",
        user="neondb_owner",
        password="npg_EXjBu2gqih6R",
        sslmode="require"
    )

    return conn