Voice Assistant using Python 🎤🧐

A simple and interactive Voice Assistant built using Python that performs various tasks based on voice commands. This project leverages Python libraries for speech recognition, text-to-speech, and automation to create a basic yet functional assistant.

Features:

*Play Songs 🎵: Plays your favorite songs on YouTube when you say commands like "Play [song name]."

*Tell Time ⏰: Provides the current time when asked, e.g., "What is the time?"

*Search Information 🔍: Fetches brief summaries from Wikipedia for queries like "Who is [person's name]?"

*Open Websites 🌐: Opens Google or performs a web search based on your command.

*Interactive Responses 🗣️: Uses text-to-speech to provide vocal feedback.

Technologies Used:

Python Libraries

*speech_recognition: Captures and recognizes voice commands.

*pyttsx3: Converts text to speech for interactive responses.

*pywhatkit: Automates tasks like playing YouTube videos.

*datetime: Retrieves and formats the current time.

*wikipedia: Fetches summaries from Wikipedia.

*webbrowser: Opens web pages or performs Google searches.

How It Works:

1.The program listens for your voice commands via a connected microphone.

2.It processes and recognizes the commands using the speech_recognition library.

3.Based on the command, the assistant:

*Plays songs on YouTube.

*Tells the current time.

*Provides brief information from Wikipedia.

*Opens websites like Google or performs searches.

4.The assistant responds with vocal feedback using pyttsx3.

Installation:

1.Clone the Repository:

git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant

2.Install the Required Libraries:
Install the necessary Python packages using pip:

pip install speechrecognition pyttsx3 pywhatkit wikipedia

3.Run the Script:
Start the assistant by running:

python voice_assistant.py

Usage:

*Activate the Assistant: The assistant listens to your commands.

*Supported Commands:

"Play [song name]."

"What time is it?"

"Who is [person's name]?"

"Open Google."

"Search [query]."

*Exit: Say "quit" to stop the program.

Example Interaction

User: Alexa, play Shape of You.
Assistant: Playing Shape of You on YouTube.

User: What time is it?
Assistant: The current time is 10:45 AM.

User: Who is Albert Einstein?
Assistant: Albert Einstein was a theoretical physicist who developed the theory of relativity.

User: Open Google.
Assistant: Opening Google.

Contributions:

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.



Acknowledgments:

Python

SpeechRecognition Documentation

pyttsx3 Documentation

Wikipedia API