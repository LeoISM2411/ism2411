# AI Use Disclosure: I asked chatgpt what IndexError on the debugging exerise meant (line 110) without fix.

# Self Assessment Questions: 1. On Exercise 5, the first bug I spotted was the "total = sale" part in the
# 1st section by using the rubber duck technique, I instantly spotted the = and my mind thought that 
# there should be a plus behind it in order to calculate total correctly which was what we did in the previous module.
# I also used the rubber duck technique on the second part which was the missing colon in for sale in sales. For the third however
# I had to find out by asking AI by pasting the traceback error from the terminal and asking what the error meant. This tells me that
# even though I can spot some simple errors, I can still improve especially with more difficult ones.
# 2. For apply_discount(price, tier) it is taking the original price and the discount tier that is given. 
# It uses the tier to determine the discount which then returns the final price. A colleague would understand
# how to use it since the name "apply_discount" is descriptive and not vague.
# 3. The use of AI definitely helped me to understand what was wrong when I asked what the error was ant not the fix. It gave
# me a clear understanding of the difference between indexes and an actual length of the list for the while loop.



# Exercise 1

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(50, 0.05):.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * (1 - 0.15)
    elif tier == "silver":
        return price * (1 - 0.10)
    elif tier == "bronze":
        return price * (1 - 0.05)
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final Price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final Price: ${total:.2f}")

# Exercise 5
 
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

# The "error" in this even though it doesn't show up in the terminal because everything is syntactically right
# is in "total = sale" because there is no += so 
# the for loop is going through each value in the list and setting the total =
# to the last number in the loop which is 90. To fix it you just have to change = to += in order to get
# $715 by adding every sale in the list.
total = 0
for sale in sales:
    total += sale  
print(f"Total: ${total}")  

# The error in this was not adding a colon after sales, this resulted in a "Syntax Error" since python
# was expecting a ":" in order for the loop to work.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# AI Use: I asked chatgpt what IndexError on line 24 meant without giving me the fix
# and it gave me a hint which was, "Is the loop allowing i to go beyond the last valid index?"
# which led me to conclude that the problem was <= because it was counting the index[5] which does not exist
#in the list since the valid indexes are from 0 through 4 and in order to change that, I got rid of the = in <= so that the loop 
# would stop once it reached the length of the list.
i = 0
while i < len(sales):
   print(sales[i])
   i += 1


# Exercise 6

x = 100 # Global

def double_it():
    x = 999 # Local
    return x * 2

print(x)
print(double_it())
print(x)  # Confirm x is still 100 after calling double_it()
# Scope is the part of the program where the variable can be accesed, in this 
# example there is a global scope which is the variable outside the function "x = 100"
# and a local scope which is "x = 999" located inside the function.