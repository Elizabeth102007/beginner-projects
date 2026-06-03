from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def get_receipt(self) -> str:
        pass


class CreditCardPayment(Payment):
    def __init__(self, cardholder: str, amount: float, card_number: str):
        self.cardholder = cardholder
        self.amount = amount
        self.card_number = card_number[-4:]  

    def process_payment(self):
        print(f"  [CreditCard] Charging ${self.amount:.2f} to card ending in {self.card_number}...")

    def get_receipt(self) -> str:
        return (
            f"--- Credit Card Receipt ---\n"
            f"  Cardholder : {self.cardholder}\n"
            f"  Card       : **** **** **** {self.card_number}\n"
            f"  Amount     : ${self.amount:.2f}\n"
            f"  Status     : Approved\n"
        )

    def __str__(self):
        return f"CreditCardPayment({self.cardholder}, ${self.amount:.2f}, *{self.card_number})"


class PayPalPayment(Payment):
    def __init__(self, email: str, amount: float):
        self.email = email
        self.amount = amount

    def process_payment(self):
        print(f"  [PayPal] Sending ${self.amount:.2f} request to {self.email}...")

    def get_receipt(self) -> str:
        return (
            f"--- PayPal Receipt ---\n"
            f"  Email  : {self.email}\n"
            f"  Amount : ${self.amount:.2f}\n"
            f"  Status : Completed\n"
        )

    def __str__(self):
        return f"PayPalPayment({self.email}, ${self.amount:.2f})"


class CryptoPayment(Payment):
    def __init__(self, wallet_address: str, amount: float, currency: str):
        self.wallet_address = wallet_address
        self.amount = amount
        self.currency = currency.upper()

    def process_payment(self):
        print(f"  [Crypto] Broadcasting {self.amount} {self.currency} to {self.wallet_address[:10]}...")

    def get_receipt(self) -> str:
        return (
            f"--- Crypto Receipt ---\n"
            f"  Wallet   : {self.wallet_address}\n"
            f"  Amount   : {self.amount} {self.currency}\n"
            f"  Status   : Confirmed\n"
        )

    def __str__(self):
        return f"CryptoPayment({self.wallet_address[:10]}..., {self.amount} {self.currency})"



class BankTransfer:
    
    def __init__(self, account_name: str, account_number: str, amount: float):
        self.account_name = account_name
        self.account_number = account_number[-4:]  # last 4 digits only
        self.amount = amount

    def process_payment(self):
        print(f"  [BankTransfer] Authorizing ${self.amount:.2f} from account ending in {self.account_number}...")

    def get_receipt(self) -> str:
        return (
            f"--- Bank Transfer Receipt ---\n"
            f"  Account Holder : {self.account_name}\n"
            f"  Account        : **** {self.account_number}\n"
            f"  Amount         : ${self.amount:.2f}\n"
            f"  Status         : Transferred\n"
        )

    def __str__(self):
        return f"BankTransfer({self.account_name}, ${self.amount:.2f}, *{self.account_number})"


class Transaction:
    def __init__(self, payments: list = None):
        self.payments = payments if payments is not None else []

    def __add__(self, other: "Transaction") -> "Transaction":
        """t1 + t2 returns a NEW Transaction with combined payments."""
        return Transaction(self.payments + other.payments)

    def __len__(self) -> int:
        """len(transaction) returns number of payments."""
        return len(self.payments)

    def total_amount(self) -> float:
        """Sum of all payment amounts in this transaction."""
        return sum(p.amount for p in self.payments)

    def __str__(self):
        lines = [f"Transaction ({len(self)} payments, total=${self.total_amount():.2f}):"]
        for i, p in enumerate(self.payments, 1):
            lines.append(f"  {i}. {p}")
        return "\n".join(lines)


def process_all(payments: list):
    
    print("\n========== Processing All Payments ==========")
    for payment in payments:
        payment.process_payment()
        print(payment.get_receipt())
    print("=============================================\n")


def add_payment_cli() -> object:
    print("\nPayment types:")
    print("  1. Credit Card")
    print("  2. PayPal")
    print("  3. Crypto")
    print("  4. Bank Transfer")
    choice = input("Select type (1-4): ").strip()

    if choice == "1":
        cardholder = input("Cardholder name: ").strip()
        card_number = input("Card number (will store last 4 only): ").strip()
        amount = float(input("Amount: $"))
        return CreditCardPayment(cardholder, amount, card_number)

    elif choice == "2":
        email = input("PayPal email: ").strip()
        amount = float(input("Amount: $"))
        return PayPalPayment(email, amount)

    elif choice == "3":
        wallet = input("Wallet address: ").strip()
        currency = input("Currency (BTC/ETH/etc): ").strip()
        amount = float(input("Amount: "))
        return CryptoPayment(wallet, amount, currency)

    elif choice == "4":
        account_name = input("Account holder name: ").strip()
        account_number = input("Account number (will store last 4 only): ").strip()
        amount = float(input("Amount: $"))
        return BankTransfer(account_name, account_number, amount)

    else:
        print("Invalid choice.")
        return None


def main():
    transaction = Transaction()

    while True:
        print("\n========== Payment System ==========")
        print("1. Add payment")
        print("2. View transaction")
        print("3. Process all")
        print("4. Exit")
        choice = input("Select option (1-4): ").lower()

        if choice == "1":
            payment = add_payment_cli()
            if payment:
                transaction.payments.append(payment)
                print(f"Added: {payment}")

        elif choice == "2":
            if len(transaction) == 0:
                print("No payments added yet.")
            else:
                print(f"\n{transaction}")

        elif choice == "3":
            if len(transaction) == 0:
                print("No payments to process.")
            else:
                process_all(transaction.payments)

        elif choice == "4":
            print("Exiting.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()