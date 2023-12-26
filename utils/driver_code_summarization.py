# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
summarizer_model="facebook/bart-large-cnn"

summarizer = pipeline(task="summarization", model=summarizer_model)
