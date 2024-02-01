worker_name = str(input("What is your name? \n"))
task_name = str(input("what task did you perfom? \n"))
hours_worked = int(input("For how long did you work? \n"))
RATE = 30000
# Computing netwage
wage = RATE * hours_worked
allowance = int(0.05 * wage)
gorss_wage = int(allowance + wage)
tax = int(0.05 * gorss_wage)
net_wage = int(gorss_wage - tax)
print(f"\nwage: {wage} \nAllowance: {allowance} \nGross wage: {gorss_wage} \nTax: {tax} \nNet wage: {net_wage}")