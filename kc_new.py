# untuk melakukan akar kuadrat
import math

# library digunakan hanya untuk membaca file csv saja
import pandas as pd

# baca file csv
df = pd.read_csv("kc.csv")

# konversi price, karena disitu uangnya string dan ada tanda dollar
df['price'] = df['price'].str.replace(
    '[$,]', '', regex=True).astype(float)


# kolom yang dipilih / tanpa date
start_row = 0
end_row = 10808
dfNew = df.iloc[0:3300][["price", "bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors",
                         "waterfront", "view", "condition", "grade", "sqft_above", "sqft_basement", "yr_built", "yr_renovated", "zipcode", "lat", "long", "sqft_living15", "sqft_lot15"]]


# rumus correlation
def calculate_correlation(data, column1, column2):
    X = data[column1]
    Y = data[column2]
    n = len(X)
    xy = X * Y

    # sum x
    x_sum = X.sum()

    # sum y
    y_sum = Y.sum()

    # sum xy
    xy_sum = xy.sum()

    # sum (sig X)^2
    X_sum = (x_sum) ** 2

    # sum (sig Y)^2
    Y_sum = (y_sum) ** 2

    # x^2
    X_quadrat = X ** 2

    # sum x^2
    X_quadrat_sum = X_quadrat.sum()

    # y^2
    Y_quadrat = Y ** 2

    # sum y^2
    Y_quadrat_sum = Y_quadrat.sum()

    # hitung pembilang dan penyebut
    pembilang = xy_sum - (x_sum * y_sum / n)
    penyebut_x = X_quadrat_sum - (X_sum / n)
    penyebut_y = Y_quadrat_sum - (Y_sum / n)

    # rumus akhir
    correlation = pembilang / math.sqrt(penyebut_x * penyebut_y)

    return correlation


# inisialisasi untuk matrix
correlation_matrix = {}

# menghitung correlation tiap tiap kolom
for column1 in dfNew.columns:
    correlation_matrix[column1] = {}
    for column2 in dfNew.columns:
        correlation_matrix[column1][column2] = calculate_correlation(
            dfNew, column1, column2)

# Print hasil
for column1 in dfNew.columns:
    for column2 in dfNew.columns:
        correlation = correlation_matrix[column1][column2]
        status = ""
        if correlation > 0:
            status = "positive"
        elif correlation < 0:
            status = "negative"
        else:
            status = "-"
        print(
            f"Correlation between {column1} and {column2}: {correlation_matrix[column1][column2]:.2f} ({status} correlation)")
        print("")
