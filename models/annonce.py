from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .annonce_equipement import AnnonceEquipement
from .base import Base

class Annonce(Base):
    __tablename__ = "annonce"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(String, nullable=True)  # Supports values like "PRIX NON SPÉCIFIÉ"
    datetime = Column(DateTime, nullable=False)
    nb_rooms = Column(Integer, nullable=True)
    nb_baths = Column(Integer, nullable=True)
    surface_area = Column(Float, nullable=True)
    link = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey("ville.id"), nullable=False)
    
    # Relationships
    ville = relationship("Ville", back_populates="annonces")
    equipements = relationship("Equipement", secondary=AnnonceEquipement, back_populates="annonces")
