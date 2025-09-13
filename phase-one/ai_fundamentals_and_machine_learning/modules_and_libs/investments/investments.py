def return_on_investment(initial_value, final_value):
    """
    Calculate the Return on Investment (ROI) as a percentage.

    ROI measures the gain or loss generated on an investment relative to its initial cost.

    Parameters:
    - initial_value (float): The starting value or cost of the investment.
    - final_value (float): The ending value or return from the investment.

    Returns:
    - float: The ROI expressed as a percentage.

    Example:
    >>> return_on_investment(1000, 1200)
    20.0
    """

    roi = (final_value - initial_value) / initial_value * 100
    return roi

def compound_interest(principal, anual_tax_interest, periods):

    """
    Calculate the compound interest over a number of periods.

    This function computes the future value of an investment based on 
    compound interest, assuming the interest is applied once per period.

    Parameters:
    - principal (float): The initial amount of money invested or loaned.
    - anual_tax_interest (float): The annual interest rate as a percentage.
    - periods (int): The number of compounding periods (typically years).

    Returns:
    - float: The final value of the investment after compounding.

    Example:
    >>> compound_interest(1000, 5, 2)
    1102.5
    """
    decimal_interest_tax = anual_tax_interest / 100
    final_value = principal * (1 + decimal_interest_tax) ** periods
    return final_value

def convert_anual_tax_to_monthly(anual_tax):

    monthly_tax = (1 + anual_tax / 100) ** (1 / 12) - 1
    return monthly_tax * 100

def calculate_cagr(initial, final, years):

    cagr = ((final / initial) ** (1 / years) - 1) * 100
    return cagr