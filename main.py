import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("irisdata.csv")
# df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

sns.lmplot(x="sepal_ln", y="sepal_wd", col="name", hue="name", data=data,
           col_wrap=3,
           ci=95,# chestia de langa linie
           palette="pastel",
           scatter_kws={"s": 10, "alpha": 1})
plt.show()
