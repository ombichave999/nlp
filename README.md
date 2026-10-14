# Generative AI & Data Analytics Practicals (Google Colab Notebook)

Live Google Colab Notebook: https://examhack-py.vercel.app/
Direct GitHub Pages: https://ombichave999.github.io/nlp/

TinyURLs:
- https://tinyurl.com/examcolab
- https://tinyurl.com/om05colab
- https://tinyurl.com/examhack-py
- https://tinyurl.com/om05py

---

## Practical No. 1: Mini Generative AI – Next Word Prediction
### Aim
To understand the basic concept of Generative Artificial Intelligence by developing a simple next-word prediction model using Python.

### Python Program
```python
import random

sentences = [
    "I love data science",
    "I love machine learning",
    "data science is amazing",
    "machine learning is powerful",
    "I enjoy learning python"
]

model = {}
for sentence in sentences:
    words = sentence.split()
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word not in model:
            model[current_word] = []
        model[current_word].append(next_word)

print("Learned Model")
print(model)

word = input("\nEnter starting word: ")
generated_text = word

for i in range(5):
    if word in model:
        word = random.choice(model[word])
        generated_text = generated_text + " " + word
    else:
        break

print("\nGenerated Text:")
print(generated_text)
```

---

## Practical No. 2: Text Generation and Text Summarization
### Part A: Text Generation
```python
responses = {
    "ai": "Artificial Intelligence is transforming the world.",
    "python": "Python is a popular programming language for AI.",
    "data": "Data is the foundation of machine learning."
}

word = input("Enter a keyword (ai/python/data): ").lower()
if word in responses:
    print("\nGenerated Text:")
    print(responses[word])
else:
    print("No text available for the given keyword.")
```

### Part B: Text Summarization using Hugging Face Transformer
```python
# !pip uninstall -y transformers torch torchvision torchaudio
# !pip install -q torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0
# !pip install -q transformers==4.52.4 sentencepiece accelerate

from transformers import pipeline

summarizer = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn"
)

text = """
Artificial Intelligence is transforming every industry by automating tasks,
improving decision-making, and generating human-like content.
Generative AI is a branch of AI capable of creating text, images,
music, videos, and even software code.
"""

summary = summarizer(text, max_length=40, min_length=15)
print("Original Text:\n", text)
print("\nGenerated Summary:\n", summary[0]["summary_text"])
```

---

## Practical No. 3: AI Tutor Chatbot using Google Gemini API
```python
import os
from google import genai

client = genai.Client(api_key="AQ." + "Ab8RN6JkmZk7st62RATnSJpe-0NqOvT2JBmN-YSJ0eWorqxnVw")

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=genai.types.GenerateContentConfig(
        system_instruction="You are a brilliant AI tutor explaining coding to beginners. Be encouraging and use emojis."
    )
)

print("AI Tutor: Hello! I'm your GenAI tutor. Ask me anything!")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI Tutor: Thank you! Happy Learning 😊")
        break
    response = chat.send_message(user_input)
    print("AI Tutor:", response.text)
    print()
```

---

## Practical No. 4: Introduction to Generative AI using Gemini API
### Sub-Part 1: Basic Text Generation
```python
# !pip -q install google-generativeai
import google.generativeai as genai

API_KEY = "AQ." + "Ab8RN6JkmZk7st62RATnSJpe-0NqOvT2JBmN-YSJ0eWorqxnVw"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")
response = model.generate_content("Explain Artificial Intelligence in simple words.")
print(response.text)
```

### Sub-Part 2: Story Generation
```python
topic = input("Enter topic: ")
prompt = f"Write a short story on {topic}"
response = model.generate_content(prompt)
print(response.text)
```

### Sub-Part 3: Question Answering
```python
question = input("Ask anything: ")
response = model.generate_content(question)
print(response.text)
```

### Sub-Part 4: Text Translation
```python
text = "Artificial Intelligence is the future."
prompt = f"Translate into Hindi:\n{text}"
response = model.generate_content(prompt)
print(response.text)
```

### Sub-Part 5: Professional Leave Application
```python
prompt = "Write a professional leave application for 2 days."
response = model.generate_content(prompt)
print(response.text)
```

### Sub-Part 6: MCQ Generation
```python
topic = "Machine Learning"
prompt = f"Generate 10 multiple-choice questions on {topic} with answers."
response = model.generate_content(prompt)
print(response.text)
```

---

## Practical No. 5: Text Generation & Prompt-Based Responses
### Sub-Part 1: Local Text Generation using GPT-2
```python
# !pip install transformers torch
from transformers import pipeline

def generate_local_text(prompt_text: str):
    generator = pipeline('text-generation', model='gpt2')
    outputs = generator(prompt_text, max_length=60, num_return_sequences=1, pad_token_id=50256)
    return outputs[0]['generated_text']

if __name__ == "__main__":
    result = generate_local_text("Artificial Intelligence will change the future of programming by")
    print(result)
```

### Sub-Part 2: Customer Service Email Reply
```python
import os
from google import genai

client = genai.Client(api_key="AQ." + "Ab8RN6JkmZk7st62RATnSJpe-0NqOvT2JBmN-YSJ0eWorqxnVw")

refund_policy = "Policy: We only allow refunds if the item is broken and reported within 7 days."
customer_email = "Hi, I bought a shirt 2 days ago but the zipper is completely broken. Can I get my money back?"

prompt = f"""
Use our company policy to answer the customer email politely.
{refund_policy}
Customer Email: {customer_email}
"""

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt
)
print("Drafted Email Reply:")
print(response.text)
```

---

## Practical No. 6: Data Analysis and Visualization (Superstore)
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/Sample - Superstore.csv", encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 1. Yearly Sales Trend
df_grouped = df.groupby(df['Order Date'].dt.year)['Sales'].sum()
df_grouped.plot(kind='line', marker='o', title='Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.show()

# 2. Sales by Category
plt.figure(figsize=(6, 4))
sns.barplot(x=df['Category'], y=df['Sales'], estimator=sum, ci=None)
plt.title('Total Sales by Category')
plt.xticks(rotation=45)
plt.show()

# 3. Profit vs Sales
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df['Sales'], y=df['Profit'], alpha=0.5)
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()
```

---

## Practical No. 7: Dimensionality Reduction using PCA (Wine Dataset)
```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine

data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

pca = PCA(n_components=2)
pca_data = pca.fit_transform(df_scaled)

print("Original Features:", df.shape[1])
print("Reduced Features:", pca_data.shape[1])

plt.scatter(pca_data[:, 0], pca_data[:, 1], c=data.target, cmap="viridis", edgecolors="k")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA on Wine Dataset")
plt.show()
```

---

## Practical No. 8: Statistical Analysis and Hypothesis Testing
### Part A: One-Way ANOVA
```python
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

class_A = [85, 90, 88, 82, 87]
class_B = [76, 78, 80, 81, 75]
class_C = [92, 88, 94, 89, 90]

f_statistic, p_value = stats.f_oneway(class_A, class_B, class_C)
print("F-Statistic:", f_statistic)
print("P-Value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Reject the Null Hypothesis: There is a significant difference in the mean exam scores.")
else:
    print("Fail to Reject the Null Hypothesis: There is no significant difference in the mean exam scores.")
```

### Part B: One-Sample T-Test
```python
import scipy.stats as stats

student_scores = [72, 88, 64, 74, 67, 79, 85, 75, 89, 77]
hypothesized_mean = 70

t_statistic, p_value = stats.ttest_1samp(student_scores, hypothesized_mean)
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The sample mean is significantly different from 70.")
else:
    print("Fail to reject the null hypothesis: The sample mean is not significantly different from 70.")
```

### Part C: Two-Sample T-Test
```python
import scipy.stats as stats

group1 = [85, 95, 100, 80, 90, 97, 104, 95, 88, 92, 94, 99]
group2 = [83, 85, 96, 92, 100, 104, 94, 95, 88, 90, 93, 94]

t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in the mean times.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in the mean times.")
```
