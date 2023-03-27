from src.models.payment import Payment
from typing import List


class PaymentManager:
    def __init__(self) -> None:
        self.payment_stack: List[Payment] = []

    def process_payment(self, payment: Payment):
        self.payment_stack.append(payment)

    def get_last_payment(self) -> None:
        if len(self.payment_stack) > 0:
            return self.payment_stack[-1]
        else:
            return None

    def get_all_payments(self) -> list:
        payments = []
        for payment in self.payment_stack:
            payments.append(
                {
                    "Data": payment.payment_time.strftime("%m/%d/%Y %H:%M:%S"),
                    "Mesa": payment.table.name,
                    "Forma de pagamento": payment.payment_method,
                    "Valor": round(payment.amount_due, 2),
                }
            )

        return payments
