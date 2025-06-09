from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_story(prompt, max_length=100, num_return_sequences=1):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=num_return_sequences, no_repeat_ngram_size=2, do_sample=True, top_k=50, top_p=0.95, temperature=0.9)
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
