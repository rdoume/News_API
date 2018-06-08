import os

db_ip = "172.16.100.68"
db_port = 5432
db_user = os.environ.get("NEWS_PG_USER")
db_passw = os.environ.get("NEWS_PG_PWD")
db_logs_path = "./logs/"
