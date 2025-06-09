from transformers import pipeline

model = pipeline("summarization", model="facebook/bart-large-cnn")
response = model("Devansh Rajani is a good boy. He is living in Rajkot. He is passionate to learn AI by doing.")
print(response)
