import pandas as pd
read_csv = pd.read_csv('etlex-utf8.csv')
df = read_csv[['e-search', 't-entry']]
df.to_csv('data_word_thai_eng.csv')
df