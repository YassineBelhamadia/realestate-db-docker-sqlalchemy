from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

# Load environment variables from the .env file
load_dotenv()

def init_engine(user_data):
    """
    Creates a new SQLAlchemy engine and tests the connection.
    """
    try:
        engine = create_engine(
            f'postgresql://{user_data["user"]}:{user_data["password"]}@{user_data["host"]}:{user_data["port"]}/{user_data["db"]}'
        )

        # Test the connection
        with engine.connect() as connection:
            print('Connection established successfully.')
        return engine
    except SQLAlchemyError as e:
        print(f"SQLAlchemy error: {e}")
        return None
    except Exception as e:
        print(f"General error: {e}")
        return None

def init_session(engine):
    """
    Initializes a new session connected to the PostgreSQL server.
    """
    if engine is None:
        print("Engine not initialized; cannot create session.")
        return None
    
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as e:
        print(f"Error creating session: {e}")
        return None

def close_session(session):
    """
    Closes the session safely.
    """
    try:
        session.close()
        print("Session closed successfully.")
    except Exception as e:
        print(f"Error closing session: {e}")
