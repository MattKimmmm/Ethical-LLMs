from test_llms import test_gpt, test_llama


def main():
    # Define the model and prompts
    # MODEL = "gpt-3.5-turbo"
    # MODEL = "gpt-4-turbo"
    model = "meta/llama-2-7b-chat"
    sentences = "../data/utilitarianism_deontology.csv"

    test_llama(model, sentences)


if __name__ == "__main__":
    main()