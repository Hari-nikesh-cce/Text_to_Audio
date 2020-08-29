
from gtts import gTTS

import os

lan='en'
tex=input("Type:")
obj=gTTS(text=tex, lang=lan, slow=False)

obj.save("Hello.mp3")
os.system('Hello.mp3')
