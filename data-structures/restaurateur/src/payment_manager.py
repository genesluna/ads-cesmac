class PaymentManager:
    def __init__(self):
        self.payment_stack = []

    def process_payment(self, payment):
        self.payment_stack.append(payment)

    def get_last_payment(self):
        if len(self.payment_stack) > 0:
            return self.payment_stack[-1]
        else:
            return None

    def get_all_payments(self):
        return self.payment_stack.copy()
