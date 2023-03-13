#!/usr/bin/env python
# coding: utf-8

# EMI SCHEDULE CALCULATOR 

# In[ ]:


# This code is purely generated via chatgpt, if you find any man made mistakes then it is your mistake. 


# In[1]:


def loan_repayment_schedule(loan_amount, annual_interest_rate, loan_tenure_years, tuition_fee_usd, books_usd, health_insurance_usd, usd_to_inr):
    loan_tenure_months = loan_tenure_years * 12
    emi_start_month = 36 # EMI starts after 3 years (36 months)
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Convert tuition fee, books, and health insurance to INR
    tuition_fee_inr = tuition_fee_usd * usd_to_inr
    books_inr = books_usd * usd_to_inr
    health_insurance_inr = health_insurance_usd * usd_to_inr

    # Calculate the loan amount after deducting tuition fee, books, and health insurance
    disbursed_amount = loan_amount - tuition_fee_inr - books_inr - health_insurance_inr

    # Calculate the EMI amount using the formula
    emi = (disbursed_amount * monthly_interest_rate * (1 + monthly_interest_rate)**loan_tenure_months) / ((1 + monthly_interest_rate)**loan_tenure_months - 1)

    outstanding_balance = disbursed_amount
    print("{:<10} {:<25} {:<25} {:<25} {:<25} {:<25}".format("Month", "Principal paid (INR)", "Interest paid (INR)", "Total paid (INR)", "Outstanding balance (INR)", "EMI (INR)"))
    for month in range(1, loan_tenure_months + 1):
        # Calculate interest and principal for the month
        if month < emi_start_month:
            interest_paid = outstanding_balance * monthly_interest_rate
            principal_paid = 0
        else:
            interest_paid = outstanding_balance * monthly_interest_rate
            principal_paid = emi - interest_paid

        # Calculate interest only on the disbursed amount
        if outstanding_balance == disbursed_amount:
            interest_paid = disbursed_amount * monthly_interest_rate

        # Check if the user is paying the EMI from this month onwards
        if month >= 37:
            outstanding_balance -= emi

        total_paid = interest_paid + principal_paid
        outstanding_balance -= principal_paid

        # Print the details for the month
        print("{:<10} {:<25,.2f} {:<25,.2f} {:<25,.2f} {:<25,.2f} {:<25,.2f}".format(month, principal_paid, interest_paid, total_paid, outstanding_balance, emi))

        # Check if outstanding balance has become 0
        if outstanding_balance <= 0:
            print("Outstanding balance has become 0 in month", month)
            break


# Example usage
loan_amount = 4000000
annual_interest_rate = 9.55
loan_tenure_years = 10
tuition_fee_usd = float(input("Enter tuition fee (in USD): "))
books_usd = float(input("Enter books cost (in USD): "))
health_insurance_usd = float(input("Enter health insurance cost (in USD): "))
usd_to_inr = float(input("Enter USD to INR conversion rate: "))

loan_repayment_schedule(loan_amount, annual_interest_rate, loan_tenure_years, tuition_fee_usd, books_usd, health_insurance_usd, usd_to_inr)

