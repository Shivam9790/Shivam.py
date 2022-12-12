one = "computer"
two = "science"  
   
print("Strings before swapping: " + one + " " + two)
one = one+ two
two = one[0 : (len(one) - len(two))]
one = one[len(two):]
print("Strings after swapping: " + one + " " + two)
