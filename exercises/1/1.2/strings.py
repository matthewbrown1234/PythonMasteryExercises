# String Manipulation
symbols = 'AAPL IBM MSFT YHOO SCO'
print(symbols[0])
print(symbols[1])
print(symbols[-1])
print(symbols[-2])

print(symbols[:4])
print(symbols[-3:])
print(symbols[5:8])
symbols += ' GOOG'  # concatenate
print(symbols)
symbols = 'HPQ ' + symbols
print(symbols)

print('MSFT' in symbols)
print('MSFTs' in symbols)
print(symbols.lower())
asdf = symbols.lower()
print(asdf)

print(symbols.split())

symbolsArray = symbols.split()

print(symbolsArray[-1])
symbolsArray[2] = 'asdf'

print(symbolsArray)

for symbol in symbolsArray:
    print('s = ', symbol)

print('GOOG' in symbolsArray)

symbolsArray.append('taco')
print(symbolsArray)

symbolsArray.insert(2, 'burrito')
print(symbolsArray)
symbolsArray.remove('burrito')
print(symbolsArray)

print(symbolsArray.index('taco'))
print(symbolsArray[7])

print(symbolsArray.count('taco'))

symbolsArray.sort()
print(symbolsArray)