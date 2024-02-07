import pandas as pd
import glob

data_paths=glob.glob('./crawling_data/*')
print(data_paths)

df=pd.DataFrame()

for path in data_paths:
    df_temp=pd.read_csv(path)
    # df_temp.columns = ['title', 'sub_category','author','image_path','review']
    # df_temp.dropna(inplace=True)
    df=pd.concat([df, df_temp], ignore_index=True)

# df.drop_duplicates(inplace=True)
df.info()
# print(df['<?xml version="1.0" encoding="UTF-8"?>'].unique())
df.to_csv('./novel.csv', index=False)
