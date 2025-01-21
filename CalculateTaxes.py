"""
Write a program to calculate tax if Salary and Tax Brackets are given as list in the form
[ [10000, .3],[20000, .2], [30000, .1], [None, .1]]. You don’t know in the beginning how many tax brackets are there.
You have to test for all of them.

TC - O(n) -- since moving through all tax slabs
However, since number of tax slabs will always be finite, we can also say TC is O(1)
SC - O(1)
"""


class TaxCalculator():
    def __init__(self):
        pass

    def calculateTax(self, taxSlabs, salary):
        remainingSalary = salary
        tax = 0
        currentLevel = 0
        previousTaxAmount = 0

        while remainingSalary > 0:
            # current taxSlab and percent
            taxSlab = taxSlabs[currentLevel]
            percent = taxSlab[1]

            if taxSlab[0] is None:
                tax += remainingSalary * percent
                return tax

            upperLimitAmt = taxSlab[0]
            taxableSalary = min(remainingSalary, upperLimitAmt - previousTaxAmount)

            # add to total tax, update leftover salary and current taxSlab
            tax += taxableSalary * percent
            remainingSalary -= taxableSalary
            previousTaxAmount = upperLimitAmt
            currentLevel += 1

        return tax


if __name__ == '__main__':
    taxSlabs = []
    taxSlabs.append([10000.0, 0.1])
    taxSlabs.append([20000.0, 0.2])
    taxSlabs.append([30000.0, 0.3])
    taxSlabs.append([None, 0.4])

    tc = TaxCalculator()
    tax = tc.calculateTax(taxSlabs, 45000)

    print(tax)