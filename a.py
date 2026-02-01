import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
df["flower_names"] = df.target.apply(lambda x: iris.target_names[x])

# Separate each flower type
df0 = df[:50]
df1 = df[50:100]
df2 = df[100:150]

# --- First scatter plot (sepal) ---
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")

plt.scatter(df0["sepal length (cm)"], df0["sepal width (cm)"], color="red", marker="+", label="Setosa")
plt.scatter(df1["sepal length (cm)"], df1["sepal width (cm)"], color="blue", marker=".", label="Versicolor")
plt.scatter(df2["sepal length (cm)"], df2["sepal width (cm)"], color="green", marker="*", label="Virginica")

plt.legend()
plt.show()

# --- Second scatter plot (petal) ---
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.scatter(df0["petal length (cm)"], df0["petal width (cm)"], color="red", marker="+", label="Setosa")
plt.scatter(df1["petal length (cm)"], df1["petal width (cm)"], color="blue", marker=".", label="Versicolor")
plt.scatter(df2["petal length (cm)"], df2["petal width (cm)"], color="green", marker="*", label="Virginica")

plt.legend()
plt.show()
