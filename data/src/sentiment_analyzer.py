import pandas as pd
from textblob import TextBlob

# Load comments dataset
df = pd.read_csv("data/comments.csv")

# Function to determine sentiment
def analyze_sentiment(comment):
    polarity = TextBlob(str(comment)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["comment"].apply(analyze_sentiment)

# Count sentiments
sentiment_counts = df["Sentiment"].value_counts()

# Display results
print("\nSentiment Analysis Results:\n")
print(df)

print("\nSentiment Summary:\n")
print(sentiment_counts)

# Save results
df.to_csv("sentiment_results.csv", index=False)

print("\nResults saved to sentiment_results.csv")
