import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2 as cv

plt.style.use("seaborn")
sns.set_style("whitegrid", {"axes.grid": False})

imagem = cv.imread("imagens/russia.jpg", cv.IMREAD_COLOR)
print(f"Largura (w): {imagem.shape[1]} pixels")
print(f"Altura (h): {imagem.shape[0]} pixels")

