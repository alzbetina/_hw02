import json
import pandas as pd
import numpy as np

netflix = pd.read_csv("netflix_titles.tsv", sep="\t")

netflix_data = netflix[["PRIMARYTITLE", "STARTYEAR", "GENRES", "DIRECTOR", "CAST"]]

netflix_data = netflix_data.applymap(lambda x: [] if pd.isna(x) else x)

netflix_data = netflix_data.rename(columns={
    "PRIMARYTITLE": "title", 
    "STARTYEAR" : "year", 
    "GENRES": "genres", 
    "DIRECTOR": "directors", 
    "CAST": "cast"})

netflix_data["genres"] = netflix_data["genres"].str.split(",")

netflix_data["cast"] = netflix_data["cast"].apply(lambda x: x.split(",") if isinstance(x, str) else x)

netflix_data["decade"] = netflix_data["year"] // 10 * 10

netflix_data = netflix_data.drop(columns=["year"])

netflix_result = netflix_data.to_dict(orient="records")

with open("hw02_output.json", mode="w", encoding="utf-8") as file:
    json.dump(netflix_result, file, sort_keys=False, ensure_ascii=False, indent=4)

