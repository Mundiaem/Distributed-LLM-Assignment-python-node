class ConversationContext(object):
    def __init__(self):
        self.model = None
        self.history = []

    def set_model(self, model):
        self.model = model

    def get_answer(self, question):
        answer = f"Answer from {self.model} for {question}"
        self.history.append({"question": question, "answer": answer})
        return answer

    def get_history(self):
        return self.history
