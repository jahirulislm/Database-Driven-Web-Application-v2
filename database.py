from sqlalchemy import create_engine, text
import os

db_connect_string = os.environ("DB_CONNECTION_STRING")

# connection to the database
engine = create_engine(
  db_connect_string,
  connect_args={"ssl": {
    "ca": "//C:/Users/jahirul_islam/Downloads"
  }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())

# from sqlalchemy import create_engine, text
# # import os

# # db_connection_string = os.environ['DB_CONNECTION_STRING']

# engine = create_engine(
#   db_connect_string,
#   connect_args={
#     "ssl": {
#       "ssl_ca": ""
#     }
#   })

# def load_jobs_from_db():
#   with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     print(result.all())
