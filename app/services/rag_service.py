import pandas as pd
import numpy as np
import os
from app.services.openai_service import get_embedding, get_completion
from sklearn.metrics.pairwise import cosine_similarity

# Load and embed customer tweets
df = pd.read_csv("data/twitter_data_clean_sample.csv")

# Compute and cache embeddings
if not os.path.exists("embeddings_sample.npy"):
    df["embedding"] = df["customer_tweet"].apply(get_embedding)
    np.save("embeddings_sample.npy", np.stack(df["embedding"].values))
else:
    df["embedding"] = list(np.load("embeddings_sample.npy", allow_pickle=True))

def retrieve_similar(user_embedding, top_k=3):
    all_embeddings = np.stack(df["embedding"].values)
    scores = cosine_similarity([user_embedding], all_embeddings)[0]
    top_indices = scores.argsort()[-top_k:][::-1]
    return "\n".join(df.iloc[i]["customer_tweet"] for i in top_indices)

def generate_response(question):
    question_embedding = get_embedding(question)
    context = retrieve_similar(question_embedding)
    prompt = f"Here are past customer issues:\n{context}\n\nAnswer the user's question: {question}"
    return get_completion(prompt)
