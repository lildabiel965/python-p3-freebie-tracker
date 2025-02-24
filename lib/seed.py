#!/usr/bin/env python3
from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create sample companies
company1 = Company(name="Tech Corp", founding_year=2000)
company2 = Company(name="Code Masters", founding_year=1995)

# Create sample devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Create sample freebies
freebie1 = Freebie(item_name="T-shirt", value=20, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Sticker", value=5, dev=dev2, company=company2)

# Add and commit to the database
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()
