class LanguageModel:
    def __init__(self, model):
        self.model = model

    def generate_response(self, prompt):
        """Generates a decision or response using the language model."""
        return self.model.generate(prompt)
