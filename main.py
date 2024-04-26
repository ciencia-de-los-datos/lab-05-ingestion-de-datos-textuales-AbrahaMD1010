import pandas as pd
import numpy as np
from pathlib import Path


carpeta_data = Path("./data")
test = []
train = []
for carpeta in carpeta_data.iterdir():
    if carpeta.name == "__MACOSX":
        continue

    for estado in carpeta.iterdir():
        if estado.name == ".DS_Store":
            continue

        print("\t", estado)
        for archivo in estado.glob("*.txt"):
            frase = archivo.read_text()
            sentimiento = estado.name
            if carpeta.name == "test":
                test.append((frase, sentimiento))

            if carpeta.name == "train":
                train.append((frase, sentimiento))


test_df = pd.DataFrame(test, columns=["phrase", "sentiment"])
train_df = pd.DataFrame(train, columns=["phrase", "sentiment"])

train_df.to_csv("train_dataset.csv", index=False)
test_df.to_csv("test_dataset.csv", index=False)

