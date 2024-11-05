from openai import OpenAI
import cohere
import csv
import re
import pandas as pd
from io import StringIO

client = cohere.Client('63lBFvckn5v3nHuMrJK7PtvixdPvZDcEIYdUKkox')

# Define parameters for dataset generation
SAMPLES = 1  # Number of samples to generate
PROMPT = '''
generate a question answer dataset on matplotlib python learning in this format

<s>[INST] Question [/INST] Answer </s>
'''  # Prompt to start the conversation

def comma_replace(input_string):
    """
    Replace {{,}} with a comma and </s> with </s>,
    """
    output_string = input_string.replace('</s>', '</s>,')
    return output_string

def generate_dataset():
    """
    Generate the dataset using Cohere
    """
    dataset = ''
    for _ in range(SAMPLES):
        response = client.chat(
            message=PROMPT,
        )
        generated_text = response.text
        dataset += generated_text
    
    dataset = comma_replace(dataset)

    return dataset

def save_dataset_to_csv(dataset, filename):
    """
    save dataset to a CSV file
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        file.write(dataset)

def main():
    dataset = generate_dataset()
    save_dataset_to_csv(dataset, 'generated_dataset.csv')
    print("Dataset generation complete. Saved as generated_dataset.csv")

if __name__ == "__main__":
    main()
