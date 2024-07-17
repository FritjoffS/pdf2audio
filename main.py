import PyPDF2
from gtts import gTTS
import os

# Insert name of your pdf 
pdfreader = PyPDF2.PdfReader(open('book.pdf', 'rb'))
full_text = ""

for page in pdfreader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    full_text += clean_text + " "

# Create a gTTS object
tts = gTTS(text=full_text, lang='en')

# Save to file
tts.save("story.mp3")

print("Audio file saved as 'story.mp3'")