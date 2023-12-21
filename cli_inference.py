import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
#can also load from your local path
tokenizer = AutoTokenizer.from_pretrained("FarReelAILab/Machine_Mindset_zh_ISTJ", use_fast=False, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("FarReelAILab/Machine_Mindset_zh_ISTJ", device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=True)
model.generation_config = GenerationConfig.from_pretrained("FarReelAILab/Machine_Mindset_zh_ISTJ")
messages = []
print("####Enter 'exit' to exit.")
print("####Enter 'clear' to clear the chat history.")
while True:
    user=str(input("User:"))
    if user=="exit":
        break
    elif user=="clear":
        messages=[]
    messages.append({"role": "user", "content": user})
    response = model.chat(tokenizer, messages)
    print("Assistant:", response)
    messages.append({"role": "assistant", "content": str(response)})
