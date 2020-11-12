from Parser import Parser

parser = Parser()
parser.parse("invatamant-superior-2020.xlsx")

names, parsed = parser.get_parsed()
print(names)
print(parsed[names[0]][0])