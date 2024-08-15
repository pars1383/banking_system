from bank.models import BankAccount, Person
from django.db import models  # Ensure this is imported
from django.db.models import Sum, Q, F
from django.db.models.functions import Cast
from django.db import transaction

def list_accounts_and_balances():
    # List the name of each account holder and their account balance
    accounts = BankAccount.objects.all().select_related('owner')
    for account in accounts:
        print(account.owner.first_name, account.owner.last_name, account.balance)

def find_richest_account():
    print("Finding the account with the highest balance...")
    richest_account = BankAccount.objects.order_by('-balance').first()
    if richest_account:
        print(f"Richest account: {richest_account.owner.first_name} {richest_account.owner.last_name} - {richest_account.balance}")
    else:
        print("No accounts found.")

def find_poorest_accounts():
    print("Finding the 5 accounts with the lowest balance...")
    poorest_accounts = BankAccount.objects.order_by('balance')[:5]
    if poorest_accounts:
        for account in poorest_accounts:
            print(f"Account with low balance: {account.owner.first_name} {account.owner.last_name} - {account.balance}")
    else:
        print("No accounts found.")


def transfer_money(from_account_id, to_account_id, amount):
    # Transfer function
    with transaction.atomic():
        from_account = BankAccount.objects.select_for_update().get(account_id=from_account_id)
        to_account = BankAccount.objects.select_for_update().get(account_id=to_account_id)

        if from_account.balance < amount:
            raise ValueError("Insufficient funds in the source account")

        from_account.balance -= amount
        to_account.balance += amount

        from_account.save()
        to_account.save()

def list_accounts_with_id_greater_than_balance():
    # List accounts where the account ID is greater than the balance
    accounts_with_id_greater_than_balance = BankAccount.objects.annotate(
        account_id_int=Cast('account_id', models.IntegerField())
    ).filter(account_id_int__gt=F('balance'))
    for account in accounts_with_id_greater_than_balance:
        print(account.account_id, account.balance)

def list_accounts_with_national_id_greater_than_balance():
    # List accounts where the national ID of the owner is greater than the balance
    accounts_with_national_id_greater_than_balance = BankAccount.objects.filter(
        owner__national_id__gt=F('balance')
    )
    for account in accounts_with_national_id_greater_than_balance:
        print(account.owner.national_id, account.balance)

def list_accounts_with_specific_balance():
    # List accounts with balance > 2 million or < 1 million
    accounts = BankAccount.objects.filter(Q(balance__gt=2000000) | Q(balance__lt=1000000))
    for account in accounts:
        print(account.owner.first_name, account.owner.last_name, account.balance)

def calculate_total_balance_per_person():
    # Calculate total balance per person
    balances = Person.objects.annotate(total_balance=Sum('accounts__balance'))
    for person in balances:
        print(person.first_name, person.last_name, person.total_balance)
