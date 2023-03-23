# QAP 4 - One Stop Insurance Company
# Evan Davies
# March 20, 2023

# Imports
import datetime
import time

# Constant Imports
f = open("OSICDef.dat", "r")

POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADDITIONAL_DISCOUNT = float(f.readline())
LIABILITY_COVER_COST = float(f.readline())
GLASS_COVER_COST = float(f.readline())
LOANER_COVER_COST = float(f.readline())
TAX_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())

f.close()

# Dollar format function
def dollarform(value):
    valuedollar = "${:,.2f}".format(value)
    return valuedollar

# Beginning of the program
while True:
    # User inputs
    while True:
        firstName = input("Enter customer's first name: ").title()
        if firstName == "":
            print("Must not be empty. Try again.")
        else:
            break

    while True:
        lastName = input("Enter customer's last name: ").title()
        if lastName == "":
            print("Must not be empty. Try again.")
        else:
            break

    while True:
        address = input("Enter customer's street address: ").title()
        if address == "":
            print("Must not be empty. Try again.")
        else:
            break

    while True:
        city = input("Enter customer's city: ").title()
        if city == "":
            print("Must not be empty. Try again.")
        else:
            break

    provList = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
    while True:
        province = input("Enter customer's province (XX): ").upper()
        if not province in provList:
            print("Invalid province. Try again.")
        else:
            break

    while True:
        postCode = input("Enter customer's postal code (X9X9X9): ").upper()
        if postCode == "":
            print("Must not be blank. Try again.")
        elif len(postCode) != 6:
            print("Must be 6 characters. Try again.")
        elif not postCode[0].isalpha() or not postCode[1].isdigit() or not postCode[2].isalpha() or not postCode[3].isdigit() or not postCode[4].isalpha() or not postCode[5].isdigit():
            print("Invalid format. Try again.")
        else:
            break

    while True:
        phoneNum = input("Enter customer's phone number (9999999999): ")
        if phoneNum == "":
            print("Must not be blank. Try again.")
        elif len(phoneNum) != 10:
            print("Must be 10 characters. Try again.")
        elif not phoneNum.isdigit():
            print("Must only include digits. Try again.")
        else:
            break

    print()
    while True:
        try:
            numCars = int(input("Number of cars being insured: "))
        except:
            print("Invalid. Must be a whole number.")
        else:
            break

    while True:
        extraLiability = input("Extra liability? (Y/N): ").upper()
        if extraLiability != "Y" and extraLiability != "N":
            print("Invalid selection. Must be Y or N. Try again.")
        else:
            break

    while True:
        glassCoverage = input("Glass coverage? (Y/N): ").upper()
        if glassCoverage != "Y" and glassCoverage != "N":
            print("Invalid selection. Must be Y or N. Try again.")
        else:
            break

    while True:
        loaner = input("Loaner car? (Y/N): ").upper()
        if loaner != "Y" and loaner != "N":
            print("Invalid selection. Must be Y or N. Try again.")
        else:
            break

    while True:
        fullMonthly = input("Pay in full or pay monthly? (F/M): ").upper()
        if fullMonthly != "F" and fullMonthly != "M":
            print("Invalid selection. Must be F or M. Try again.")
        else:
            break

    # Calculations
    if numCars == 1:
        basicPrem = BASIC_PREM
    else:
        basicPrem = (numCars - 1) * (BASIC_PREM - (BASIC_PREM * ADDITIONAL_DISCOUNT)) + BASIC_PREM

    if extraLiability == "Y":
        liabCost = LIABILITY_COVER_COST * numCars
    else:
        liabCost = 0

    if glassCoverage == "Y":
        glassCost = GLASS_COVER_COST * numCars
    else:
        glassCost = 0

    if loaner == "Y":
        loanerCost = LOANER_COVER_COST * numCars
    else:
        loanerCost = 0

    totalExtraCosts = liabCost + glassCost + loanerCost

    totalPrem = basicPrem + totalExtraCosts

    HST = totalPrem * TAX_RATE

    totalCost = totalPrem + HST

    monthlyPayment = (totalCost + 39.99) / 8

    invoiceDate = datetime.date.today()
    invoiceDate = datetime.datetime.strftime(invoiceDate, "%Y-%m-%d")

    currDate = datetime.datetime.now()
    nextPayment = (currDate.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
    nextPayment = datetime.datetime.strftime(nextPayment, "%Y-%m-%d")

    # Printing the receipt

    print()
    print("            ONE STOP INSURANCE COMPANY")
    print("                 INSURANCE POLICY")
    print()
    print("    ==========================================")
    print()

    fullName = firstName + " " + lastName
    print(f"    {fullName:<26s}    Cars:     {numCars:>2d}")
    addressCity = address + ", " + city
    print(f"    {addressCity:<26s}    Liability: {extraLiability:>1s}")
    provPost = province + ", " + postCode
    print(f"    {provPost:<26s}    Glass:     {glassCoverage:>1s}")
    print(f"    {phoneNum:<10s}                    Loaner:    {loaner:>1s}")
    print()
    print()

    basicPremDsp = dollarform(basicPrem)
    print(f"         Basic Premium:             {basicPremDsp:>10s}")
    liabCostDsp = dollarform(liabCost)
    print(f"         Extra Liability:            {liabCostDsp:>9s}")
    glassCostDsp = dollarform(glassCost)
    print(f"         Glass Coverage:             {glassCostDsp:>9s}")
    loanerCostDsp = dollarform(loanerCost)
    print(f"         Loaner Car:                 {loanerCostDsp:>9s}")
    totalExtraDsp = dollarform(totalExtraCosts)
    print(f"         Total Extra Costs:         {totalExtraDsp:>10s}")
    print("         -------------------------------------")

    totalPremDsp = dollarform(totalPrem)
    print(f"         Total Premium:             {totalPremDsp:>10s}")
    HSTDsp = dollarform(HST)
    print(f"         HST:                        {HSTDsp:>9s}")
    print("         -------------------------------------")

    totalCostDsp = dollarform(totalCost)
    print(f"         TOTAL COST:               {totalCostDsp:>11s}")
    print()

    if fullMonthly == "M":
        print()
        monthlyPaymentDsp = dollarform(monthlyPayment)
        print(f"    Monthly Payment:                {monthlyPaymentDsp:>10s}")
        print()

    print("    ==========================================")
    print()
    print(f"    Policy No.               {POLICY_NUM:>4d}")
    print(f"    Invoice Date:      {invoiceDate:>10s}")
    print(f"    Next Payment Date: {nextPayment:>10s}")

    print()
    print("Saving policy information...")

    f = open("Policies.dat", "a")

    f.write("{}, ".format(POLICY_NUM))
    f.write("{}, ".format(invoiceDate))
    f.write("{}, ".format(firstName))
    f.write("{}, ".format(lastName))
    f.write("{}, ".format(address))
    f.write("{}, ".format(city))
    f.write("{}, ".format(province))
    f.write("{}, ".format(postCode))
    f.write("{}, ".format(phoneNum))
    f.write("{}, ".format(str(numCars)))
    f.write("{}, ".format(extraLiability))
    f.write("{}, ".format(glassCoverage))
    f.write("{}, ".format(loaner))
    f.write("{}, ".format(fullMonthly))
    f.write("{}\n".format(str(totalPrem)))

    f.close()

    time.sleep(5)
    print("Policy information processed and saved.")
    POLICY_NUM += 1

    while True:
        cont = input("Would you like to process another policy (Y/N): ").upper()
        if cont != "Y" and cont != "N":
            print("Invalid selection. Must be Y or N. Try again.")
        else:
            break
    if cont == "N":
        break

f = open("OSICDef.dat", "w")

f.write("{}\n".format(POLICY_NUM))
f.write("{}\n".format(str(BASIC_PREM)))
f.write("{}\n".format(str(ADDITIONAL_DISCOUNT)))
f.write("{}\n".format(str(LIABILITY_COVER_COST)))
f.write("{}\n".format(str(GLASS_COVER_COST)))
f.write("{}\n".format(str(LOANER_COVER_COST)))
f.write("{}\n".format(str(TAX_RATE)))
f.write("{}\n".format(str(PROCESS_FEE)))

f.close()

print("All information saved. Thank you for using this program. Have a nice day.")