#620. Not Boring Movies
from tabulate import tabulate


table = [['id','movie name','rating'], ['1', 'KGF',9.5], ['2', 'pushpa',8.5 ], ['3', 'bahubali', 9.4]]

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))




