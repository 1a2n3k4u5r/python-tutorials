import pandas as pd

print("Pandas version:", pd.__version__)

df = pd.DataFrame({
    "Name": ["Ankur", "Rahul"],
    "Age": [20, 21]
})

print(df) 