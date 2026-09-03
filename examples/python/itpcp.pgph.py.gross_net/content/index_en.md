[Income Tax]: <https://www.finanz.at/steuern/lohnsteuertabelle/#Lohnsteuertabelle_2024> "Income Tax - finanz.at"
[Social Security]: <https://www.gesundheitskasse.at/cdscontent/?contentid=10007.870462> "Social Security - sozialversicherung.at"
# Gross Net Calculator

## Introduction

In this task, the goal is to implement a function that calculates the net amount based on a given gross amount. The following information about the Austrian tax system is relevant:

### Income Tax Table

In Austria, the following income tax table applies:
| (Annual) Income (2024) | Tax Rate (2024) |
|------------------|-------------------|
| up to 12,816 Euro | 0 % |
| up to 20,818 Euro | 20 % |
| up to 34,513 Euro | 30 % |
| up to 66,612 Euro | 40 % |
| up to 99,266 Euro | 48 % |
| up to 1,000,000 Euro | 50 % |
| above 1,000,000 Euro | 55 % |

Important: the tax brackets are progressive: i.e., no taxes are paid on the first 12,816 Euro, then 20%, etc.

See also [Income Tax].

### Social Security

For social security, **18.12% is deducted** from the gross salary **before** taxes for income **above 518 Euro (monthly)**. The **maximum contribution base is 6,060 Euro per month**, so you pay a maximum of 13,176.86 Euro (6,060 * 12 * 0.1812) in social security per year. All additional income above 72,720 Euro (6,060 * 12) therefore does not further increase the social security contribution.

Note: The rules for the social security contribution have been slightly adjusted.

See also [Social Security].

### Example 21,000 Euro Gross Annual Income

21,000 * 18.12% = 3,805.20 Euro (Social Security contribution - below the maximum contribution base of 72,720 Euro p.a. but above 518 Euro per month)
Tax base = 17,194.80 Euro
up to 12,816 Euro -> 12,816 * 0% = 0
up to 20,818 Euro -> 4,378.80 * 20% = 875.76
Total taxes: 875.76

Net salary: 16,319.04 Euro


## Task
1. Write a function that takes a gross salary (float) and outputs the corresponding net salary rounded to the nearest cent.


## Hints

* Relevant for our calculation here is only the income tax from the gross amount minus social security. This is a modified formula from the one actually used.
