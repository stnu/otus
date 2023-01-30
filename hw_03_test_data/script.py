import pandas as pd
import numpy as np
import json


df_books = pd.read_csv('books.csv')
df_users = pd.read_json('users.json')

df_new_books = df_books[['Title', 'Author', 'Pages', 'Genre']]
df_new_users = df_users[['name', 'gender', 'address', 'age']]

books = df_new_books.to_dict('records')
books_s = np.array_split(books, len(df_new_users))
df_new_users['books'] = books_s

with open('result_hw3.json', 'w') as f:
    f.write(json.dumps(json.loads(df_new_users.to_json(orient="records")), indent=4))

