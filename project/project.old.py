from dotenv import load_dotenv
import stdiomask
import os
import openai as oi


def main():
    # 1. Ask for API encrypted and store it locally

    api_key = check_api_key()
    oi.api_key = api_key

    # 2. Ask for model to use
    model_selection = select_model()

    # 3. Ask for prompt
    print(f"Hi, I'm a helpful assistant.")
    prompt = input("What can I do for you? ")

    # Generate and print response
    response = generate_response(model_selection, prompt)
    print(response)


def check_api_key():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    if not api_key:
        api_key = get_api_key()
        print("API key saved to .env file.")
    else:
        while True:
            try:
                print(f"Using API key: sk-{api_key[-4:]}")
                answer = input("Is this correct? (Y/N) ")
                if answer.lower() == 'n':
                    api_key = get_api_key()
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


def get_api_key():
    while True:
        try:
            api_key = stdiomask.getpass(prompt="Enter your OpenAI API key: ")
            if len(api_key) == 51 and api_key[0:3] == 'sk-':
                with open(".env", "w") as file:
                    file.write(f'API_KEY="{api_key}"')
                return api_key
            else:
                print(f'API Key is not valid, it should consist of "sk-" at beginning and than 48 alphanumeric characters')
        except ValueError:
            print(f'API Key is not valid, it should consist of "sk-" at beginning and than 48 alphanumeric characters')


def select_model():
    models = ["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4"]

    for model in models:
        print(f'{models.index(model)}: {model}')

    while True:
        try:
            choice = int(input(f"Select GPT model (0-{len(models) - 1}): "))
            if choice in range(len(models)):
                return models[choice]
            else:
                print(f"Invalid choice. Please enter a number between 0 and {len(models) - 1}: ")
        except ValueError:
            print(f"Invalid choice. Please enter a number between 0 and {len(models) - 1}: ")


def generate_response(model_selection, prompt):
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
