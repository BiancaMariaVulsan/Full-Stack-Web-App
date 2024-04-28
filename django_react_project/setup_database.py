import psycopg2
from psycopg2 import sql

# Connect to the PostgreSQL server
conn = psycopg2.connect(dbname='postgres', user='postgres', password='yourpassword')
conn.autocommit = True
cur = conn.cursor()

# SQL commands
commands = [
    "CREATE DATABASE mydatabase;",
    """
    CREATE USER myuser WITH PASSWORD 'mypassword';
    ALTER ROLE myuser SET client_encoding TO 'utf8';
    ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myuser SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
    """
]

# Execute SQL commands
for command in commands:
    cur.execute(command)

# Close the connection
cur.close()
conn.close()
