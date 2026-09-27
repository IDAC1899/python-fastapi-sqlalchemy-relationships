# seed.py

from sqlalchemy.orm import sessionmaker, Session
from data.tea_data import teas_list
from config.environment import db_URI
from sqlalchemy import create_engine
from models.tea import Base, TeaModel

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("seeding the database...")
    db = SessionLocal()
    db.add_all(teas_list)
    db.commit()
    db.close()

    print("Database seeding complete! 👋")
except Exception as e:
    print("An error occurred:", e)