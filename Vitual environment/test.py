import pandas as pd

print("Pandas version:", pd.__version__)

data = {
    "Name": ["Ankur", "Rahul"],
    "Age": [20, 21]
}

df = pd.DataFrame(data)

print(df)
