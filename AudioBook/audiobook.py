import pyttsx3, PyPDF2

#take file location from user
file = input("Enter File(.pdf) location: ")
#Read the pdf file
pdfReader = PyPDF2.PdfFileReader(open(file,'rb'))
#convert text to speech
speaker = pyttsx3.init()
#playback speed
speed = int(input("Please enter the playback speed(100 being 1x): "))
rate = speaker.getProperty('rate')
speaker.setProperty('rate', speed)
#change voice
v = int(input("Select the gender voice (0 = Male, 1 = Female): "))
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[v].id)

#play the audio
for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
