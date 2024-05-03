import pandas as pd
import matplotlib.pyplot as plt

# Load the results from the CSV file
df = pd.read_excel("../output/summary_results.xlsx")

# Set the index to 'Model' for better plotting
df.set_index('Model', inplace=True)

# Plotting
ax = df[['Utilitarian Proportion', 'Skip Proportion', 'Deontological Proportion']].plot(
    kind='bar',
    stacked=True,
    color=['#1f77b4', '#ff7f0e', '#2ca02c'],  # colors for each section
    figsize=(10, 7)
)

# Adding titles and labels
plt.title('Proportions of Responses by Model')
plt.xlabel('Model')
plt.ylabel('Proportion')
plt.xticks(rotation=45)
plt.legend(title='Response Type', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()
