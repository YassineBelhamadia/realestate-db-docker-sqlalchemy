from models import Annonce, Ville, Equipement, AnnonceEquipement, Base
from session import init_engine, init_session, close_session
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()  # This will automatically load the .env file if it exists

user = {
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host', 'localhost'),  # Default to 'localhost' if not set
    'port': os.getenv('port', '5432'),  # same for the port
    'db': os.getenv('db')
}

# Initializing the engine and session
engine = init_engine(user)
session = init_session(engine)

# creating the tables
Base.metadata.create_all(engine)
# Check if the session is created successfully
if session:
    # Load the CSV file from the `data` folder
    try:
        df = pd.read_csv('./data/input.csv')
        print("CSV file loaded successfully.")
    except FileNotFoundError:
        print("File 'input.csv' not found in the 'data' folder.")
        exit(1)

    # Process and insert data into the database
    for _, row in df.iterrows():
        # Check if the city already exists
        city = session.query(Ville).filter_by(name=row["city_name"]).first()
        if not city:
            city = Ville(name=row["city_name"])
            session.add(city)
            session.commit()

        # Create the Annonce object
        annonce = Annonce(
            title=row["title"],
            price=row["price"],
            datetime=row["datetime"],
            nb_rooms=int(row["nb_rooms"]),
            nb_baths=int(row["nb_baths"]),
            surface_area=float(row["surface_area"]),
            link=row["link"],
            city_id=city.id
        )
        session.add(annonce)
        session.commit()

        # Process and link equipment
        equipement_names = row["equipement_names"].split("|")
        for equipement_name in equipement_names:
            equipement = session.query(Equipement).filter_by(name=equipement_name).first()
            if not equipement:
                equipement = Equipement(name=equipement_name)
                session.add(equipement)
                session.commit()

            # Associate equipment with the announcement
            annonce.equipements.append(equipement)

        # Commit each annonce and its relationships
        session.commit()

    print("Data imported successfully.")
    
    # Close the session
    close_session(session)

else:
    print("Session creation failed. Exiting.")
    exit(1)

    
