import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create fictitious data
data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Subcategory': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'],
    'Value1': [10, 20, 15, 5, 25, 30, 8, 12, 18],
    'Value2': [8, 12, 6, 3, 15, 10, 6, 9, 12],
    'Value3': [6, 8, 4, 2, 10, 8, 4, 6, 8]
}

df = pd.DataFrame(data)

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Bar plot
sns.barplot(x='Category', y='Value1', hue='Subcategory', data=df, ax=axs[0, 0])
axs[0, 0].set_title('Bar Plot')
axs[0, 0].set_xlabel('Category')
axs[0, 0].set_ylabel('Value1')

# Scatter plot
sns.scatterplot(x='Value1', y='Value2', hue='Category', style='Subcategory', data=df, ax=axs[0, 1])
axs[0, 1].set_title('Scatter Plot')
axs[0, 1].set_xlabel('Value1')
axs[0, 1].set_ylabel('Value2')

# Box plot
sns.boxplot(x='Category', y='Value3', hue='Subcategory', data=df, ax=axs[1, 0])
axs[1, 0].set_title('Box Plot')
axs[1, 0].set_xlabel('Category')
axs[1, 0].set_ylabel('Value3')

# Heatmap
pivot_data = df.pivot_table(index='Category', columns='Subcategory', values='Value1')
sns.heatmap(pivot_data, annot=True, cmap='YlGnBu', ax=axs[1, 1])
axs[1, 1].set_title('Heatmap')
axs[1, 1].set_xlabel('Subcategory')
axs[1, 1].set_ylabel('Category')

# Adjust spacing between subplots
plt.tight_layout()

# Display the plot
plt.show()