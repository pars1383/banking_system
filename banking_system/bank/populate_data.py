import random
from decimal import Decimal
from django.utils.crypto import get_random_string
from bank.models import Person, BankAccount

def populate_data():
    # Create some Person objects
    persons = []
    for _ in range(1000):
        person = Person(
            first_name=get_random_string(10),
            last_name=get_random_string(10),
            national_id=get_random_string(10)
        )
        persons.append(person)
    Person.objects.bulk_create(persons)

    # Fetch all Person objects
    persons = list(Person.objects.all())

    # Create 20,000 BankAccount objects
    accounts = []
    for _ in range(20000):
        person = random.choice(persons)
        account = BankAccount(
            owner=person,
            account_id=get_random_string(20),
            balance=Decimal(random.uniform(0, 1000000)).quantize(Decimal('0.01'))
        )
        accounts.append(account)
    BankAccount.objects.bulk_create(accounts)

if __name__ == "__main__":
    populate_data()
