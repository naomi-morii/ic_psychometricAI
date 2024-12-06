import ollama
import csv
import json
import sys

# Define model with system constraints
modelfile = '''
FROM llama2:7b
PARAMETER temperature 0.01
SYSTEM "You are a helpful assistant who can only reply with numbers from 1 to 5, and nothing else."
'''

ollama.create(model='llama2:7b', modelfile=modelfile)

json_file = "bfi2facets.json"
with open(json_file, "r") as f:
    bfi_data = json.load(f)

items = bfi_data["BFI-2"]["items"]
statements = "\n".join([f"{item['id']}. {item['statement']}" for item in items])

prompt = (
    "Here are a number of characteristics that may or may not apply to you. "
    "Please indicate the extent to which you agree or disagree with each statement. "
    "1 denotes 'strongly disagree', 2 denotes 'a little disagree', 3 denotes 'neither agree nor disagree', "
    "4 denotes 'little agree', 5 denotes 'strongly agree'."
    "Here are the statements, score them one by one: \n"
    f"{statements}\n\n"
    "Answer format: Provide a list of numbers from 1 to 5 for each statement, separated by commas, and nothing else.")

def query_model(prompt):
    response = ollama.chat(model='llama2:7b', messages=[
        {"role": "system", "content": "You are a helpful assistant who can only reply with numbers from 1 to 5, and nothing else."},
        {"role": "user", "content": prompt}
    ])
    print(response)
    return response['message']['content']

response = query_model(prompt)
scores = [int(score.strip()) for score in response.split(",")]

# Combine items with scores
output_data = [
    {
        "id": item["id"],
        "statement": item["statement"],
        "facet": item["facet"],
        "reversed": item["reversed"],
        "score": scores[index]
    }
    for index, item in enumerate(items)
]

# Save to CSV as novo2.csv
csv_file = sys.argv[1]
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "statement", "facet", "reversed", "score"])
    writer.writeheader()
    writer.writerows(output_data)

print(f"Results saved to {csv_file}")

# # Parse the response into a list of scores
# scores = response.split(',')

# # Write the results to a CSV file
# csv_file = sys.argv[1]
# with open(csv_file, "w", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     # Write the header
#     writer.writerow(["ID", "Statement", "Facet", "Reversed", "Score"])
#     # Write the data rows
#     for item, score in zip(items, scores):
#         writer.writerow([item["id"], item["statement"], item["facet"], item["reversed"], score])

# print(f"Results saved to {csv_file}")
