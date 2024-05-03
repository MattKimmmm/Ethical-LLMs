from test_llms import test_gpt, test_llama, parse_output, save, get_prompt
import pandas as pd
import replicate

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
    models.append("meta/llama-2-70b-chat")
    models.append("meta/meta-llama-3-8b")
    models.append("meta/meta-llama-3-70b")

    for model in models:
        for role in roles:
            test(model, topic, role)


def test(model, topic, role):
    data_file = f"../data/{topic}/{topic}_{role}.xlsx"
    data = pd.read_excel(data_file).values
    choices = []
    results = []
    for row in data:
        action = row[1]
        label = row[2]

        print("Prompt:", get_prompt(action))

        if "llama" in model:
            output = test_llama(model, action)
        else:
            output = test_gpt(model, action)

        # output_str = ''.join(output).strip().lower()
        # output_str = output_str.lstrip()
        print("Output:", output)

        choice, result = parse_output(output, label)
        choices.append(choice)
        results.append(result)
    util_counts = results.count("utilitarianism")
    deon_counts = results.count("deontology")
    skip_counts = results.count("skip")
    print(f"For 100 ambiguous actions on utilitarianism and deontology, the model answered {len(results)} times.")
    print(f"Utilitarian: {util_counts}, Deontological: {deon_counts}, Skip: {skip_counts}")
    save_file = f"../output/{topic}/{model.split("/")[-1]}_{topic}_{role}.csv"
    save(data, choices, results, save_file)


if __name__ == "__main__":
    main()
