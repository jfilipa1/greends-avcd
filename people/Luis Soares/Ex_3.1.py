import pandas as pd
import zipfile
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('people\Luis Soares\EFIplus_medit.zip',compression='zip', sep=";")

#print(df)

sample_sizes = [10, 50, 100, 150, 200, 250, 300, 500, 1000]
means = []

for i in sample_sizes:
    sample = df.sample(n=i)
    mean_temp_ann = np.mean(sample["temp_ann"])
    means.append(mean_temp_ann)

sns.barplot(x=np.array(sample_sizes), y=np.array(means), color = 'blue')

plt.xlabel("Sample size")
plt.ylabel("Mean temp_ann")
plt.title("temp_ann mean for different sample sizes")

plt.show()