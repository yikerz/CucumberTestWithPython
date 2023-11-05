class TaxCalculator:
    
    @staticmethod
    def calculate_total_bill(initial_bill_amount, tax_rate):
        return initial_bill_amount * (1 + tax_rate/100)