from datasets import load_dataset

cv_20 = load_dataset(".\\cv-corpus-20.0\\ka", split="train")

print(cv_20[:5])