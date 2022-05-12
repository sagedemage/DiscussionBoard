"""
Formatting Functions
"""


def utility_text_processors():
    def format_price(amount, currency="$"):
        return f"{amount:.2f}{currency}"
    
    return dict(format_price=format_price)