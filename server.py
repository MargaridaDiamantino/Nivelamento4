from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

df = pd.read_csv("operadoras_ativas.csv", delimiter=";", dtype=str)

@app.get("/search/")
def search_operadora(q: str = Query(..., min_length=2)):
    
    results = df[df.apply(lambda row: q.lower() in str(row).lower(), axis=1)]
    return results.to_dict(orient="records")

