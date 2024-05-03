import pandas as pd
import matplotlib.pyplot as plt

# Load the results from the CSV file
df = pd.read_excel("../output/summary_results.xlsx")

# select some rows by Model
# df = df[df['Model'].isin(['gpt-4-turbo', 'llama-3-8b'])]

# Set the index to 'Model' for better plotting
df.set_index('Model', inplace=True)

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))
df[['Utilitarian Proportion', 'Skip Proportion', 'Deontological Proportion']].plot(
    kind='bar',
    stacked=True,
    color=['#1f77b4', '#ff7f0e', '#2ca02c'],  # colors for each section
    ax=ax
)
# df[['Utilitarian Proportion', 'Deontological Proportion']].plot(
#     kind='bar',
#     stacked=True,
#     color=['#1f77b4', '#2ca02c'],  # colors for each section
#     ax=ax
# )

# Adding titles and labels
plt.title('Proportions of Responses by Model')
plt.xlabel('Model')
plt.ylabel('Proportion (%)')
plt.xticks(rotation=45)
plt.legend(title='Response Type', bbox_to_anchor=(1.05, 1), loc='upper left')


# Function to add labels to the bars
def add_labels(ax):
    for rect in ax.patches:
        # Find where everything is located
        height = rect.get_height()
        if height > 0:  # Only add labels to non-zero values
            width = rect.get_width()
            x = rect.get_x()
            y = rect.get_y()

            # The height of the bar is the data value and can be used as the label
            label_text = f'{height * 100:.1f}'  # Format to 2 decimal places

            # ax.text(x, y, text)
            label_x = x + width / 2
            label_y = y + height / 2
            ax.text(label_x, label_y, label_text, ha='center', va='center', fontsize=12, color='white')


# Call the function to add labels
add_labels(ax)

# Display the plot
plt.tight_layout()
plt.show()
