
import csv
from api import databases
from api import model

model.Base.metadata.create_all(databases.engine)

r=databases.SessionLocal()

with open(r"C:\Users\prana\OneDrive\Desktop\testupdate.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        if not row['group']:
            raise ValueError('group row is empty')
        if not row['subgroup_id']:
            raise ValueError('subgroup row is empty')
        if not row['tenant_id']:
            raise ValueError('tenant_id row is empty')
        if not row['email']:
            raise ValueError('email row is empty')
        if not row['role']:
            raise ValueError('role row is empty')
        if not row['firstname']:
            raise ValueError('firstname row is empty')
        if not row['lastname']:
            raise ValueError('lastname row is empty')
        if not row['cell_number']:
            raise ValueError('cell_number row is empty')
        if not row['level_twomanager']:
            raise ValueError('level_twomanager row is empty')
        if not row['company_name']:
            raise ValueError('company_name row is empty')
        if not row['account_name']:
            raise ValueError('account_name row is empty')
        if not row['title']:
            raise ValueError('title row is empty')
        if not row['country']:
            raise ValueError('country row is empty')
        if not row['line_manager']:
            raise ValueError('line_manager row is empty')
        if not row['address']:
            raise ValueError('address row is empty')
        if not row['department']:
            raise ValueError('department row is empty')
        if not row['job_title']:
            raise ValueError('job_title row is empty')
        if not row['date_of_birth']:
            raise ValueError('date_of_birth row is empty')
        if not row['start_date']:
            raise ValueError('start_date row is empty')
        if not row['start_date']:
            raise ValueError('start_date row is empty')
        if not row['town']:
            raise ValueError('town row is empty')
        if not row['postcode']:
            raise ValueError('postcode row is empty')    
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
