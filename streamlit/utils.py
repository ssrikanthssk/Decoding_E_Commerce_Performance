# utils.py — helper functions for formatting dashboard values

def format_currency(value):
    if value is None:
        return "R$ 0.00"
    return f"R$ {value:,.2f}"

def format_number(value):
    if value is None:
        return "0"
    return f"{value:,.0f}"

def format_percent(value):
    if value is None:
        return "0%"
    return f"{value:.1f}%"

def format_days(value):
    if value is None:
        return "N/A"
    return f"{value:.1f} days"

def format_rating(value):
    if value is None:
        return "N/A"
    return f"{value:.2f} ⭐"