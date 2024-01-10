import sys
import os
import redis

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import dotenv

# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from sqlalchemy import DDL

# from models import PDUData
dotenv.load_dotenv("./.env")

PWD = os.getenv("DB_PWD")
USER = os.getenv("DB_USER")

conn_str = f"clickhouse://{USER}:{PWD}@localhost:8123/test"  # create a .env file and put your clickhouse password and username there with
# name DB_PWD and DB_USER respectively


engine = create_engine(conn_str)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = "test"
with engine.connect() as connection:
    # Use the connection to execute the DDL statement
    connection.execute(DDL(f"CREATE DATABASE IF NOT EXISTS {database}"))
# PDUData.__table__.create(engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def redis_connect() -> redis.client.Redis:
    try:
        r = redis.ConnectionPool(
            host="localhost",
            port=6379,
            password="redispw",
            username="default",
            db=0,
        )
        client = redis.Redis(connection_pool=r)
        return client
    except redis.ConnectionError:
        print("Connection Error!")
        sys.exit(1)


client = redis_connect()
