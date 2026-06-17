# Expression Execution

# String and Numeric values can operate together with * (REPEAT)
A,B=2,3
Txt="@"
print(2*Txt*3) # @@@@@@

# String and string can operate with + (concatination)
A,B="2",3
Txt="@"
print((A+Txt)*B) #2@2@2@

# Numeric values can operate with all arithematic operators
A,B=2,3
C=4
print(A+B+C) # 14


#Airthematic expression with integer and float will result in float.
A,B=10,5.0
C=A*B
print(C) # 50.0

# Result of divisin operator with two integer will be float.
A,B=1,2
C=A/B
print(C) # 0.5

# Integer division with float and init will give int dispalyed as float
A,B=1.5,3
C=A//B
print(C, A/B) # 0.0,0.5

# Floor gives closet integer, which is lesser than or equal to the float value.
# Result of (A // B) is same a floor (A / B)
A,B=12,5
C=A//B
print(C) #2

A,B =-12,5
C=A//B
print(C) # -3

A,B=12,-5
C=A//B
print(C) # -3

# Remainder is negative when denominator is negative.
A,B=-5,2
C=A%B
print(C) # 1

A,B=5,2
C=A%B
print(C) # 1

A,B=5,-2
C=A%B
print(C) # -1