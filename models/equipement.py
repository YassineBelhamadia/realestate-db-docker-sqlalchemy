from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .annonce_equipement import AnnonceEquipement
from .base import Base


class Equipement(Base):
    __tablename__ = "equipement"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationships
    annonces = relationship("Annonce", secondary=AnnonceEquipement, back_populates="equipements")
