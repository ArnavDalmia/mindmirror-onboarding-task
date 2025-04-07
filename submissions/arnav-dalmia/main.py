"""
STUDENT NAME: Arnav Dalmia
"""

from transformers import pipeline
import csv

# Load your chosen models here
def load_emotion_model():
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)
    return classifier
# Process journal entries and return emotion predictions
def detect_emotions(text_entries, emotion_model):
    final = []
    for i in text_entries:
        analysis =  {}
        results = emotion_model(i)
        for j in results[0]:
            analysis[j["label"]] = j["score"]


        with open('emotion.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Journal Entry: " + i])
            writer.writerow(['Emotion', 'Score'])
            for key, value in analysis.items():
                writer.writerow([key, value])
            print(f"Results saved")
        final.append(analysis)
    return final


def load_summarization_model():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer


# Generate summaries for journal entries
def summarize_entries(entries, summarizer):
    final = []
    for i in entries:
        summ = ((summarizer(i, max_length=130, min_length=30, do_sample=False))[0])['summary_text']
        final.append("Original Journal Entry: "+ i + " , Summary: " + summ)

        with open('summaries.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Journal Entry", i])
                writer.writerow(['Summary', summ])
                writer.writerow('')
                print(f"Results saved")
    return final

if __name__ == '__main__':
    # Load models
    emotion_model = load_emotion_model()
    summarizer = load_summarization_model()

    # Example input
    emotion_journal_entries = [
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
        "I finally worked up the confidence to ask my crush out for a date, and she said yes. Weeks of mental torment has all been worth it."]
    
    summary_journal_entries = [
    "I had a busy day with numerous meetings. Initially felt overwhelmed, but finishing my important tasks provided relief. Later, dinner with friends was very enjoyable and relaxing.",
    "I spent the morning catching up on emails, which felt tedious, but finishing them was quite a relief. Later in the day, I took a brief walk outside, which helped clear my mind and re-energize.",
    "Today was filled with running errands and dealing with traffic. I felt slightly annoyed but managed to stay focused, and sharing dinner with family in the evening lifted my mood.",
    "I had a series of calls that left me feeling drained, but completing my to-do list gave a sense of accomplishment. Afterwards, I relaxed with a good book and felt more at ease.",
    "My workload felt overwhelming in the afternoon, and I worried I wouldn't meet my deadlines. However, knocking out a few big tasks boosted my confidence, and a quiet evening helped me unwind."]
    
    # I made sure that the entries are quite simple, should pass all pre processing concerns, but now adding lower casing underneath for any potential problems in the models usage.
    for i in emotion_journal_entries:
        temp = i
        temp.lower()
        i = temp
    for i in summary_journal_entries:
        temp = i
        temp.lower()
        i = temp

    # Apply pipelines
    #emotions = detect_emotions(emotion_journal_entries, emotion_model)
    summaries = summarize_entries(summary_journal_entries, summarizer)

    # Output results
    #print("Emotion Predictions:", emotions)
    print("Summaries:", summaries)