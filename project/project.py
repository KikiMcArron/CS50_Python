from dotenv import load_dotenv
import stdiomask
import os
import openai as oi


def main():
    api_key = setup_api_key()
    model_selection = select_model()
    prompt = get_user_prompt()

    response = generate_response(api_key, model_selection, prompt)
    print(response)


def setup_api_key():
    load_dotenv()
    api_key = os.getenv('API_KEY')

    if not api_key:
        api_key = get_api_key_from_user()
        print("API key saved to .env file.")
    else:
        api_key = confirm_api_key(api_key)

    return api_key


def get_api_key_from_user():
    while True:
        try:
            api_key = stdiomask.getpass(prompt="Enter your OpenAI API key: ")
            if is_valid_api_key(api_key):
                with open(".env", "w") as file:
                    file.write(f'API_KEY="{api_key}"')
                return api_key
            else:
                print("Invalid API Key format. It should start with 'sk-' and than have 48 alphanumeric characters.")
        except ValueError:
            print("Invalid API Key format. It should start with 'sk-' and than have 48 alphanumeric characters.")


def is_valid_api_key(api_key):
    return len(api_key) == 51 and api_key[:3] == 'sk-' and api_key[3:].isalnum()


def confirm_api_key(api_key):
    while True:
        try:
            print(f"Using API key: sk-{api_key[-4:]}")
            answer = input("Is this correct? (Y/N) ")
            if answer.lower() == 'n':
                api_key = get_api_key_from_user()
                print("API key saved to .env file.")
            elif answer.lower() == 'y':
                break
            else:
                os.system('clear')
                print("Invalid Entry!")
        except ValueError:
            os.system('clear')
            print("Invalid Entry!")
    return api_key


def select_model():
    models = ["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4"]

    for index, model in enumerate(models):
        print(f'{index}: {model}')

    while True:
        try:
            choice = int(input(f"Select GPT model (0-{len(models) - 1}): "))
            if choice in range(len(models)):
                return models[choice]
            else:
                print(f"Invalid choice. Please enter a number between 0 and {len(models) - 1}.")
        except ValueError:
            print(f"Invalid choice. Please enter a number between 0 and {len(models) - 1}.")


def get_user_prompt():
    print("Hi, I'm a helpful assistant.")
    prompt = input("What can I do for you? ")
    return prompt


def generate_response(api_key, model_selection, prompt):
    oi.api_key = api_key
    completion = oi.ChatCompletion.create(
        model=model_selection,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    return completion['choices'][0]['message']['content']


if __name__ == '__main__':
    main()
