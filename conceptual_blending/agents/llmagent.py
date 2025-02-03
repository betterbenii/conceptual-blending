from openai import OpenAI


endpoint = "https://models.inference.ai.azure.com"
client = OpenAI(
    base_url=endpoint,
)


class ChatGPTAgent():

    def __init__(self, model="gpt-4o"):
        self._model = model

    def __call__(self, messages, functions=[]):
        if functions == []:
            response = client.chat.completions.create(model=self._model,
                messages=messages,
                temperature=0,
                timeout = 15)
        else:
            response = client.chat.completions.create(model=self._model,
                messages=messages,
                functions=functions,
                function_call="auto",
                temperature=0,
                timeout = 15)
        return response.choices[0].message
