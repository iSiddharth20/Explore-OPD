from llama_index.llms.ollama import Ollama

class OllamaResponse:
    def __init__(self):
        ''' Ollama will assume Meta-Llama-3.1-8B '''
        self.llm = Ollama(model="llama3.1")
        self.query = None
        self.response = None
    
    def get_query(self, query):
        ''' Get Query from Client '''
        self.query = query

    def add_context_to_query(self, context):
        ''' Add Retrieved Context to Query '''
        self.query = f'''
        <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
        You are a helpful AI assistant. Use the provided context to answer the user's query as accurately and concisely as possible. 
        If the answer cannot be found in the provided context, or if the context is insufficient, respond just with "I don't have enough context to answer the query."
        <|eom_id|>
        <|start_header_id|>user<|end_header_id|>
        # Query: 
        {self.query}
        ----
        # Context:
        {context}
        <|eom_id|>
        <|start_header_id|>assistant<|end_header_id|>
        '''

    def get_response_from_ollama(self):
        ''' Send Query to Ollama, Get Response from Ollama '''
        self.response = self.llm.complete(self.query)


if __name__ == '__main__':

    query = r"What the favourite color of LLMs?"

    test_run_1 = OllamaResponse()
    context = r"The sun rises from East and sets in West."
    test_run_1.get_query(query)
    test_run_1.add_context_to_query(context)
    test_run_1.get_response_from_ollama()
    print(f'\nQuery    : {query} \nContext  : {context} \nResponse : {test_run_1.response}')

    test_run_2 = OllamaResponse()
    context = r"LLMs prefer the color Blue over all others."
    test_run_2.get_query(query)
    test_run_2.add_context_to_query(context)
    test_run_2.get_response_from_ollama()
    print(f'\nQuery    : {query} \nContext  : {context} \nResponse : {test_run_2.response}\n')
