

from test_llms import test_gpt, test_llama

# Define the model and prompts
# MODEL = "gpt-3.5-turbo"
# MODEL = "gpt-4-turbo"
MODEL = "meta/llama-2-7b-chat"
PROMPTS = "../data/utilitarianism_deontology_gpt4.xlsx"

# test_gpt(MODEL, PROMPTS)

test_llama(MODEL, PROMPTS)