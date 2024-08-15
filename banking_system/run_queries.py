import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_system.settings')
django.setup()

from bank.queries import (
    list_accounts_and_balances,
    find_richest_account,
    find_poorest_accounts,
    transfer_money,
    list_accounts_with_id_greater_than_balance,
    list_accounts_with_national_id_greater_than_balance,
    list_accounts_with_specific_balance,
    calculate_total_balance_per_person
)

print("Starting script...")

# Run all functions one by one
list_accounts_and_balances()
print("Finished listing accounts and balances.")

find_richest_account()
print("Finished finding the richest account.")

find_poorest_accounts()
print("Finished finding the poorest accounts.")

# Example transfer: Adjust IDs and amount as needed
# transfer_money('account_id_1', 'account_id_2', 500.00)
# print("Finished transferring money.")

list_accounts_with_id_greater_than_balance()
print("Finished listing accounts with ID greater than balance.")

list_accounts_with_national_id_greater_than_balance()
print("Finished listing accounts with national ID greater than balance.")

list_accounts_with_specific_balance()
print("Finished listing accounts with specific balance conditions.")

calculate_total_balance_per_person()
print("Finished calculating total balance per person.")
