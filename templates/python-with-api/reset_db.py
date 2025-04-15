from app.db.database import Base, engine

# Drop all tables in the database
# Use it carefully, as this will delete all data!
Base.metadata.drop_all(bind=engine)
print("All tables dropped.")
