#!/usr/bin/env python3
from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    import ipdb; ipdb.set_trace()

ompany = session.query(Company).first()
print(company.freebies)

dev = session.query(Dev).first()
print(dev.companies)

freebie = session.query(Freebie).first()
print(freebie.print_details())
