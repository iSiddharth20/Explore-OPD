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
        If the answer cannot be found in the provided context, or if the context is insufficient, respond with "I don't have enough context to answer the query."
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
    test_run = OllamaResponse()
    query = r"Hello! What is your name?"
    test_run.get_query(query)
    context = r"Your name is OllamaBot."
    test_run.add_context_to_query(context)
    test_run.get_response_from_ollama()
    print(test_run.response)