# write a programm to fill in a letter template given below with name and date.""

letter = ''' Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Ankur").replace("<|Date|", "24 September 2050"))