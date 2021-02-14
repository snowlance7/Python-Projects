tax_rate = 0.06

def sales_tax(total):
    return round(total * tax_rate,2)

def total_after_tax(total):
    return round(total + (total * tax_rate),2)