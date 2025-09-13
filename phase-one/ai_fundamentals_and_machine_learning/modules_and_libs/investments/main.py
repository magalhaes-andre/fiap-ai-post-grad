import investments

initial_value = 1000
final_value = 1500
years = 5
annual_tax = 6

roi = investments.return_on_investment(initial_value, final_value)
print(f"ROI was equal to: {roi:.2f}%")

compound = investments.compound_interest(initial_value, annual_tax, years)
print(f"Final value with compound interest: R${compound:.2f}")

monthly_tax = investments.convert_anual_tax_to_monthly(annual_tax)
print(f"Monthly tax: {monthly_tax:.2f}%")

cagr = investments.calculate_cagr(initial_value, final_value, years)
print(f"CAGR: {cagr:.2f}%")