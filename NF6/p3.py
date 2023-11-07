import collections

country=collections.namedtuple('Country',['name','isdno','continent'])

c=country('India','91','Asia')

print("The name of the country is ")

print(c.name)

print("The isd no of the country is ")

print(c.isdno)

print("The continent of the country is ")

print(c.continent)


cd=['Bangladesh','90','Asia']

print("The orderdict instance using namedtuple is ")

print(c._asdict())