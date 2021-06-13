import pyttsx3
import PyPDF2
import datetime

with open('sample.pdf', 'rb') as book:

    fullContent = ''

    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 150)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        fullContent += content

    output = f"Output{datetime.datetime.now()}.mp3"
    audio_reader.save_to_file(fullContent , output)
    print(f"Your audio file was saved as {output}")
    audio_reader.runAndWait()