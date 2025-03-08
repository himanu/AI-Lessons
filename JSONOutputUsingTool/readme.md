# Using Tools with LLM for Structured Responses

## Overview

This project demonstrates how to utilize Large Language Models (LLMs) to generate structured responses using tools. In this case, we are using the `ollama` library to interact with the LLM and format translations into a JSON structure.

## Getting Started

### Prerequisites

- Python 3.x
- `ollama` library installed. You can install it using pip:


### Project Structure

The main file in this project is `index.py`, which contains the implementation of the translation tool.

### How It Works

1. **Define the Model**: The model to be used is specified at the beginning of the `index.py` file. In this case, we are using `llama3.1`.

2. **Define Tools**: The tools are defined in a list, where each tool has a type and a function. The function specifies the name, description, and parameters required for the tool.

3. **Translation Function**: The `translate` function takes an input text and prepares a system prompt for the LLM. It sends the prompt along with the user input to the LLM using the `ollama.chat` method.

4. **Structured Output**: The response from the LLM is processed to extract the structured output, which is printed in JSON format.

### Example Usage

To use the translation tool, simply call the `translate` function with the desired text:

This will output the translations in Spanish, Hindi, and Urdu in a structured JSON format.

## Conclusion

This project showcases how LLMs can be effectively used with tools to generate structured responses. By defining the tools and using the LLM's capabilities, you can easily format outputs in a way that is useful for various applications.