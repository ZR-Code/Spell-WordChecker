words = input('What do you want to word check: ')

split = words.split(" ")
spaceless = [x for x in split if x != '']
print(spaceless)
print(len(spaceless))
