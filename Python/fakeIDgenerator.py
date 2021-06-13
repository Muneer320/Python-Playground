from faker import Faker
from time import sleep

fake = Faker()

print('*' * 25, f"\nName:\n{fake.name()}\n", '=' * 15, f"\nAddress:\n{fake.address()}\n{fake.city()}\n{fake.country()}\n", '-' * 15, f"\nJob:\n{fake.job()}\n", '-' * 15, f"\nDate Of Birth:\n {fake.date_of_birth()}\n", '-' * 15, f"\nFavourite Colour:\n {fake.color_name()}\n", '*' * 25)
sleep(5)