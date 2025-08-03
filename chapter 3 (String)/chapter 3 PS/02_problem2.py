name = "Aiman"
date = "13 May, 2006"

# letter = f'''  
# Dear {name}, 
# You are selected! 
# {date}
# ''' 
# print(letter)

letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
print(letter)

# letterFormated = letter.replace("<|Name|>", name).replace("<|Date|>", date)    #strings at immutable hence we need to create another string here
# print(letterFormated)
# print(letter)