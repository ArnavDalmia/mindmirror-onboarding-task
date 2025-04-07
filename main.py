"""
STUDENT NAME:
STUDENT ID:
"""

from transformers import pipeline

# Load your chosen models here
def load_emotion_model():
    # Research and return a pre-trained emotion detection pipeline
    pass

def load_summarization_model():
    # Research and return a pre-trained summarization pipeline
    pass

# Process journal entries and return emotion predictions
def detect_emotions(text_entries, emotion_model):
    # Implement logic to process entries and extract emotions
    pass

# Generate summaries for journal entries
def summarize_entries(entries, summarizer):
    # Implement logic to summarize each entry
    pass

if __name__ == '__main__':
    # Load models
    emotion_model = load_emotion_model()
    summarizer = load_summarization_model()

    # Example input
    journal_entries = [
        "Felt anxious about my exam, but happy after completing it.",
        "It rained all day and I stayed inside feeling calm.",
        "Went out with some old friends, it was nostalgic and I want to do it more often.", #writing harder entries, not directly showing the emotions, and want the model to pickup contextual info
        "Had a fight with my partner, and I don't know how to approach them to make up.",
        "I wen't for a run after a long time, feeling tired but excited for tomorrow again.",
        "Bought some new clothes today, but they got ruined by some bird poop, felt stressed and angry with everything. Really ruined my mood for the entire day.",
        "Went to my local cafe for my daily coffee, and it was by far the best coffee I've had so far. Made me feel happy and ready for the day.",
        "The sale section of holister ran out of my size, felt annoyed as I was looking forward to some nice finds.",
        "Finally picked up a lego set I've been wanting for so long, can't wait to open it up and put it together.",
        "Someone stole my laptop, I'm so angry! I have to spend money, I've lost valuable information, nothing good has come of this.",
        "I finally worked up the confidence to ask my crush out for a date, and she said yes. Weeks of mental torment has all been worth it."
    ]

    # Apply pipelines
    emotions = detect_emotions(journal_entries, emotion_model)
    summaries = summarize_entries(journal_entries, summarizer)

    # Output results
    print("Emotion Predictions:", emotions)
    print("Summaries:", summaries)