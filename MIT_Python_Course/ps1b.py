total_cost=float(input('Enter the cost of dream home: '))
portion_down_payment= 0.25 * total_cost

annual_salary = float(input('Enter the starting annual salary: '))

semi_annual_rise= float(input('Enter the semi-annual rise: '))
return_on_investment=0.04


portion_saved=float(input('Enter the amount that you want to save: '))

monthly_savings=(annual_salary/12) * portion_saved


current_savings=0
number_of_months=0

while current_savings < portion_down_payment:

    current_savings += monthly_savings + (current_savings * return_on_investment)/12

    number_of_months+=1

    if number_of_months % 6 == 0 :

        annual_salary += ( semi_annual_rise*annual_salary)
        monthly_savings= (annual_salary/12) * portion_saved

print(f"The number of months : {number_of_months} " )