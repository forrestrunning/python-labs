s='Playing with Django is now a necessary fun'

words=s.split()
print words
print(' ').join(words)

print s.replace('Django', 'Python')

print s.upper()
print s.title()

print s.count('a')
print s.count('a',0,10)

t='200'
print t.isdigit()
