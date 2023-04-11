#!/usr/bin/python3
import requests
import json
import argparse

def read_api_key(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config["api_key"]

api_key = read_api_key("api_key.json")
url = 'https://api.openai.com/v1/engines/davinci-codex/completions' # Replace 'davinci-codex' with the desired model name, like 'chatgpt'.
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

def chatgpt_query(prompt, max_tokens=50, n=1, stop=None, temperature=0.7):
    data = {
        'prompt': prompt,
        'max_tokens': max_tokens,
        'n': n,
        'stop': stop,
        'temperature': temperature
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['text']
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Query ChatGPT with a given prompt.')
    parser.add_argument('prompt', type=str, help='The prompt to send to ChatGPT')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    response_text = chatgpt_query(args.prompt)
    print(response_text)
