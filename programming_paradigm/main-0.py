import sys
from bank_account import BankAccount

# Create an account with a default balance
account = BankAccount(100)

# Command line handling
if len(sys.argv) == 1:
    print("Usage: python main-0.py [deposit:<amount> | withdraw:<amount> | display]")
else:
    command = sys.argv[1]

    if command.startswith("deposit:"):
        amount = float(command.split(":")[1])
        account.deposit(amount)
    elif command.startswith("withdraw:"):
        amount = float(command.split(":")[1])
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command")
