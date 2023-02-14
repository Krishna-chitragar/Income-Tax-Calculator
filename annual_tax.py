//calculate tax
print("Enter your annual salary:")
a=0;b=0 ;c=0; d=0; e=0; f=0;
n=int(input())
if n in range(250000,500000):
    a=(((n-250000)*5)/100)
if (n > 500000) or (n == 250000) or (n == 500000):
    a=(((500000-250000)*5)/100)

if n in range(500000,750000):
    b=(((n-500000)*10)/100)
if (n > 750000) or (n == 750000) :
    b=(((750000-500000)*10)/100)

if n in range(750000,1000000):
    c=(((n-750000)*15)/100)
if (n >= 1000000):
    c=(((1000000-750000)*15)/100)

if n in range(1000000,1250000):
    d=(((n-1000000)*20)/100)
if (n >= 1250000):
    d=(((1250000-1000000)*20)/100)

if n in range(1250000,1500000):
    e=(((n-1250000)*25)/100)
if (n >= 1500000):
    e=(((1500000-1250000)*25)/100)

if (n > 1500000):
    f=(((n-1500000)*30)/100)

#tax_2021=a+b+c+d+e+f
#tax_with_cess_2021=(tax_2021*4)/100
#new_tax_2021=tax_2021+tax_with_cess_2021
#print("The new income tax for 2021 is:\n","Rs.",new_tax_2021,"/- only")

#import pdb
#pdb.set_trace()
n=n-200000
if n in range(250000,500000):
    a_2020=(((n-250000)*5)/100)
if (n > 500000) or (n == 250000) or (n == 500000):
    a_2020=(((500000-250000)*5)/100)

if n in range(500000,1000000):
    b_2020=(((n-500000)*20)/100)
if (n > 500000) or (n == 1000000) or (n == 500000):
    b_2020=(((1000000-500000)*20)/100)
	
if (n > 1000000):
    c_2020=(((n-1000000)*30)/100)

tax_2020 = a_2020 + b_2020 + c_2020
tax_cess_2020 = (tax_2020*4)/100
old_tax_2020=tax_2020+tax_cess_2020
print("The old income tax for 2020 is:\n","Rs.",old_tax_2020,"/- only")

tax_2021=a+b+c+d+e+f
tax_with_cess_2021=(tax_2021*4)/100
new_tax_2021=tax_2021+tax_with_cess_2021
print("The new income tax for 2021 is:\n","Rs.",new_tax_2021,"/- only")

if (new_tax_2021 > old_tax_2020):
	diff = new_tax_2021-old_tax_2020
	print("2020 is better",diff,"more")
else:
	diff = old_tax_2020-new_tax_2021
	print("2021 is better",diff,"more")



