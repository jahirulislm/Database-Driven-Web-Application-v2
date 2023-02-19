from sqlalchemy import create_engine



# connection to the database
engine = create_engine("mysql+pymysql://dvkmh0ivca6aejtwkopd:pscale_pw_y1FzH5npfX0npyjvUsFHVjhmDqa2Seo89gLBIVifk63@ap-southeast.connect.psdb.cloud/webapplication?charset=utf8mb4")


with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())