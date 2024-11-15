from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .annonce_equipement import AnnonceEquipement
from .base import Base

class Ville(Base):
    __tablename__ = 'ville'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    
    annonces = relationship("Annonce", back_populates="ville")