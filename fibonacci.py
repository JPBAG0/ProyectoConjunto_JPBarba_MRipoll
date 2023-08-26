def fibonacci_series(n):
    series = [0, 1]  # Inicializamos la serie con los dos primeros términos

    while len(series) < n:
        next_term = series[-1] + series[-2]  # Calculamos el siguiente término
        series.append(next_term)

    return series

# Generar la serie de Fibonacci para los primeros 100 términos
fibonacci_terms = fibonacci_series(100)

# Imprimir la serie
for term in fibonacci_terms:
    print(term, end=", ")
