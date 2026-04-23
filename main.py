import Movies as m
title = input("Insert Title Here: ")
year = input("Insert Year Here: ")
result = m.getmovie(title, year)
print(result.keys())