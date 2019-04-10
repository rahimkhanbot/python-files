
import random

first_names = ['Suresh', 'Jane', 'Corey', 'Manoj', 'Finan', 'Kurt', 'Mcrenold', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Kumar', 'Doe', 'Jenkins', 'Kumar', 'Davis', 'Chand', 'Jefferson', 'Jacobs', 'Khan', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Chennai', "Pondy", 'Kanchipuram', 'Mumbai', 'South Park', 'Atlantis', 'Kozhikodu', 'Moscow', 'Kochi', 'Tirunelveli', 'Gotham', 'Springfield', 'Trichy', 'Smalltown', 'Madurai', 'Ahmedabad', 'Faketown', 'Kovai', 'Delhi', 'Vice City', 'New York', 'Neyveli', 'Theni', 'Winterfell', 'Salem', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000, 9999)}'

    st_num = random.randint(1, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 999999)

    address = f'No: {st_num} {street} st. {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@company.com'

    base = f'{first} {last} \n{phone} \n{address}\n{email} \n'
    print(base)