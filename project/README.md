# Simple ChatGPT App
#### Video Demo: https://youtu.be/uTTzYBJpwLE?si=xF2-ijpUc124OoO3
#### Description of the program and the libraries used

This is a simple program to communication with ChatGPT via OpenAI API


1. **Setting up the API Key**
    The first step of the program involves setting up the user's secret API Key. 
    Given the sensitive nature of this data, it's crucial to encrypt the entered value. 
    For this purpose, the "stdiomask" library is used. 

    To further enhance security, the key provided by the user is stored locally in an .env file.
    The file will be created the first time a properly validated Key is entered.
    I used the "dotenv" library to read value of the key from .env file and use it as environment variable.

    Before prompting the user for the key, the program checks if the .env file contains any value assigned to the "API_KEY" variable. 
    If a value exists, the prefix 'sk-...' along with the last four characters of the key are displayed on the screen. 
    The user is then asked to confirm if the displayed key is proper. 
    To ensure the .env file (containing the sensitive API Key) is not inadvertently shared, it is added to the .gitignore file.

2. **GPT Model Selection**
    The second step prompts the user to select the GPT model they wish to use. 
    The program displays the available models and asks the user to select a value from 0 to 2.
   (This program displays 3 models, but iterating through the list using a fol loop allows you to expand the list 
    with additional models without having to modify the entire function)

3. **User Prompt**
    The next step introduces the AI model as a helpful assistant and asks the user what it can assist with.

4. **Response Generation**
    The final step involves generating and displaying the assistant's response