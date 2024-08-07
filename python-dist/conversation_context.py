import datetime

from transformers import AutoTokenizer, AutoModelForCausalLM, LlamaTokenizer, LlamaForCausalLM, \
    LlamaForQuestionAnswering
from transformers.models import llama

HUGGING_FACE_TOKEN = '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'
from huggingface_hub import login

login(token=HUGGING_FACE_TOKEN)


class ConversationContext(object):
    def __init__(self):
        self.model = None
        self.history = []
        self.transformer = Transformers()

    def set_model(self, model):
        self.model = model

    def get_answer(self, question):
        if self.model == 'Llama2':
            response = self.get_llama_answer(question)
            return response
        else:
            response = self.get_mistral_answer(question)
            return response

    def get_llama_answer(self, question):
        try:
            llama2_model, llama2_tokenizer = self.transformer.load_llma2_model()
            context = "Previous context if any."
            response = self.transformer.generate_response(llama2_model, llama2_tokenizer, question, context)
            date = datetime.datetime.now()
            answer = {'success': True, 'question': question, date: date, response: response}
            self.history.append(answer)
            return answer
        except Exception as e:
            # Handle exception and return an error message
            return {"success": False, 'error': str(e)}

    def get_mistral_answer(self, question):
        try:
            mistral_model, mistral_tokenizer = self.transformer.load_mistral_model()
            context = "Previous context if any."
            response = self.transformer.generate_response(mistral_model, mistral_tokenizer, question, context)
            date = datetime.datetime.now()
            answer = {'success': True, 'question': question, date: date, response: response}
            self.history.append(answer)
            return answer
        except Exception as e:
            # Handle exception and return an error message
            return {"success": False, 'error': str(e)}

    def get_history(self):
        # sort by date descending
        history = sorted(self.history, key=lambda x: x['date'], reverse=True)
        return history

    def get_model(self):
        return self.model


class Transformers(object):

    def load_llma2_model(self):
        model_name = 'meta-llama/Llama-2-7b-hf'
        # tokenizer = LlamaForQuestionAnswering.from_pretrained("meta-llama/Llama-2-70b-chat-hf", token=HUGGING_FACE_TOKEN)
        # model = LlamaForQuestionAnswering.from_pretrained("meta-llama/Llama-2-70b-chat-hf", token=HUGGING_FACE_TOKEN)
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_authtoken=True)
        model = AutoModelForCausalLM.from_pretrained(model_name, use_authtoken=True)
        return model, tokenizer

    def load_mistral_model(self):
        model_name = 'mistralai/Mistral-Large-Instruct-2407'
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_authtoken=True)
        model = AutoModelForCausalLM.from_pretrained(model_name, use_authtoken=True)
        return model, tokenizer

    def generate_response(self, question, model, tokenizer, context=None):
        if context:
            inputs = tokenizer(context + question, return_tensors="pt")
        else:
            inputs = tokenizer(question, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=512)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
