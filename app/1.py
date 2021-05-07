
import csv
from api import databases
from api import model

model.Base.metadata.create_all(databases.engine)

r=databases.SessionLocal()

with open(r"C:\Users\prana\OneDrive\Desktop\testupdate.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        db_record = model.Data(
            group=row['group'],
            subgroup_id=row['subgroup_id'],
            tenant_id=row['tenant_id'],
            email=row['email'],
            role=row['role'],
            firstname=row['firstname'],
            lastname=row['lastname'],
            password=row['password'],
            cell_number=row['cell_number'],
            level_twomanager=row['level_twomanager'],
            company_name=row['company_name'],
            account_name=row['account_name'],
            title=row['title'],
            country=row['country'],
            line_manager=row['line_manager'],
            address=row['address'],
            department=row['department'],
            job_title=row['job_title'],
            date_of_birth=row['date_of_birth'],
            start_date=row['start_date'],
            town=row['town'],
            postcode=row['postcode']
            )
        r.add(db_record)
    r.commit()
r.close()
print('data stored successfully')