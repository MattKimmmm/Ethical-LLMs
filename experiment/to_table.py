import pandas as pd
import numpy as np

def process(topic, role, model):
    result_file = f"../output/{topic}/{model}_{topic}_{role}.csv"
    model = model.replace("meta-", "")
    data = pd.read_csv(result_file)
    results = data["Result"].values
    util_counts = np.sum(results == "utilitarianism")
    deon_counts = np.sum(results == "deontology")
    skip_counts = np.sum(results == "skip")
    total_responses = len(results)
    print(f"Model: {model}, Role: {role}")
    print(f"For {total_responses} ambiguous actions on utilitarianism and deontology, the model answered {len(results)} times.")
    print(f"Utilitarian: {util_counts}, Deontological: {deon_counts}, Skip: {skip_counts}")
    print("")

    return {
        'Model': model,
        'Role': role,
        'Total Responses': total_responses,
        'Utilitarian': util_counts,
        'Deontological': deon_counts,
        'Skip': skip_counts
    }


def main():
    topic = "utilitarianism_deontology"
    roles = []
    roles.append("chinese_philosopher")
    roles.append("middle_age")
    roles.append("USA")
    models = []
    models.append("gpt-3.5-turbo")
    models.append("gpt-4-turbo")
    models.append("meta/llama-2-7b-chat")
    models.append("meta/llama-2-13b-chat")
    # models.append("meta/llama-2-70b-chat")
    models.append("meta/meta-llama-3-8b")
    # models.append("meta/meta-llama-3-70b")

    all_results = []

    for model in models:
        for role in roles:
            model = model.split('/')[-1]
            result = process(topic, role, model)
            all_results.append(result)

    results_df = pd.DataFrame(all_results)

    # Aggregate results by model
    aggregated_results = results_df.groupby('Model').sum().reset_index()
    # Calculate proportions
    aggregated_results['Utilitarian Proportion'] = aggregated_results['Utilitarian'] / aggregated_results['Total Responses']
    aggregated_results['Deontological Proportion'] = aggregated_results['Deontological'] / aggregated_results['Total Responses']
    aggregated_results['Skip Proportion'] = aggregated_results['Skip'] / aggregated_results['Total Responses']

    # Select only relevant columns for clarity
    final_results = aggregated_results[['Model', 'Utilitarian Proportion', 'Deontological Proportion', 'Skip Proportion']]

    # Save the results to a CSV file
    final_results.to_excel("../output/summary_results.xlsx", index=False)
    print("Aggregated results saved to summary_results.xlsx")


if __name__ == "__main__":
    main()