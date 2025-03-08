import ollama

MODEL_NAME = "llama3.1"

tools = [
    {
        "type": "function",
        "function": {
            "name": "format_different_translation",
            "description": "output different translation in a json format",
            "parameters": {
                "type": "object",
                "properties": {
                    "orignal_text": {
                        "type": "string",
                        "description": "Original text"
                    },
                    "spanish_text": {
                        "type": "string",
                        "description": "Spanish Translation of Text"
                    },
                    "hindi_text": {
                        "type": "string",
                        "description": "Hindi Translation of Text"
                    },
                    "urdu_text": {
                        "type": "string",
                        "description": "urdu Translation of Text"
                    }
                }
            }
        }
    }
]
def translate(text):
    system_prompt = """
            You are given a input text by user. 
            You need to translate it into  languages, spanish, urdu, hindi.
            You must pass the translation into the tool to get output in a json format.
    """
    print(text)
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": text}]
    response = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
    )
    assistant_message = response.message
    print(assistant_message.tool_calls[0].function.arguments)


translate("How Are You?")
