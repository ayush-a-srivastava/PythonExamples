from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ['Pikachu','Squirtle','Charmender','Dragonite','Pidgeot'])
table.add_column("Type", ['Electric','Water','Fire','Dragon','Flying'])

table.align = 'r'
print(table)