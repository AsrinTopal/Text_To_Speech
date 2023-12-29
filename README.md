# Text to Speech Application

## Overview

This Text-to-Speech (TTS) application is a simple Python program with a graphical user interface (GUI) built using the Tkinter library. The application allows users to convert entered text into speech, with options to customize the voice gender and speech speed. Users can also download the spoken text as an MP3 file.

## Features

- **Text-to-Speech Conversion:** Enter the desired text, choose the voice gender, and select the speech speed to hear the text spoken aloud.
- **Voice Gender Options:** Select between Male and Female voices for the speech.
- **Speech Speed Control:** Choose from three speed settings: Fast, Normal, and Slow.
- **MP3 Download:** Save the spoken text as an MP3 file for offline use.


## Project Structure

- `main.py`: The main Python script containing the application code.
  
- `speak.png`, `mainlogo.png`: Image files used for the application icons.
  
## Requirements

Ensure you have the following prerequisites installed:

- **Python:** The application is built using Python. If you don't have it installed, download and install it from [python.org](https://www.python.org/).

- **Tkinter:** Tkinter is included with most Python installations, so no additional installation is required.

- **pyttsx3:** This library is used for text-to-speech functionality. Install it using the following command:

   ```bash
   pip install pyttsx3
   pip install tk
    ```
## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/AsrinTopal/Text_To_Speech.git
   cd Text_To_Speech
   python main.py
## Usage

1. Launch the application using the instructions above.
2. Enter the desired text in the provided text area.
3. Choose the voice gender from the "VOICE" dropdown.
4. Select the speech speed from the "SPEED" dropdown.
5. Click the "SPEAK" button to listen to the spoken text.
6. Click the "DOWNLOAD" button to save the spoken text as an MP3 file.
## Complexity Analysis

### Time Complexity

The time complexity of the Text-to-Speech (TTS) application is primarily determined by the length of the input text (`n`). The key operations impacting time complexity are the text-to-speech conversion and download operations. The time complexity for these operations is linear with respect to the length of the input text, expressed as O(n), where 'n' is the length of the text.

### Space Complexity

The space complexity of the TTS application is influenced by the amount of memory required to store the input text (`n`). Similar to time complexity, the primary factor affecting space complexity is the text-to-speech conversion and download operations, both having a space complexity of O(n). GUI operations, such as button clicks and combobox selections, generally contribute a constant factor to the overall space complexity (O(1)).

It's important to note that these complexities are high-level estimates, and the actual performance may depend on factors such as the underlying implementation details of the pyttsx3 library and the GUI framework used in the application.

These complexity analyses provide an overview of how the application's performance scales with the input size and memory requirements. For most practical use cases, the application's efficiency should meet the needs of typical text-to-speech scenarios.
## User-Friendly GUI

The Text-to-Speech (TTS) application features an intuitive and user-friendly graphical user interface (GUI) designed to enhance the user experience. With a sleek design, the GUI allows users to effortlessly enter text, select voice options, and control speech speed. The application's simplicity ensures that users, whether tech-savvy or newcomers, can easily navigate and utilize its powerful text-to-speech capabilities. Additionally, clear instructions for each functionality are provided within the GUI, making the application accessible to a wide range of users.

[![TEXT TO SPEECH](https://i.postimg.cc/CKHBY3Ch/Ekran-g-r-nt-s-2023-12-29-223825.png)](https://postimg.cc/PLJrQFF9)
