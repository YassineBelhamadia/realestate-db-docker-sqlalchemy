from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

AnnonceEquipement = Table(
    "annonce_equipement",
    Base.metadata,
    Column("annonce_id", Integer, ForeignKey("annonce.id"), primary_key=True),
    Column("equipement_id", Integer, ForeignKey("equipement.id"), primary_key=True)
)
