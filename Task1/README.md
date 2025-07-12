# Airtable NLP Chatbot

This project is a command-line chatbot that uses Google Gemini and Airtable data to answer user questions. The chatbot fetches data from an Airtable table and uses the Gemini API to generate concise answers based on the table data and chat history.

## How It Works

- Loads Airtable data using API credentials.
- Accepts user questions in a loop.
- Sends the Airtable data and chat history to Gemini for generating a one-line answer.
- Displays the answer and maintains chat history.

## Setup Instructions

1. **Clone or Download the Repository**

2. **Install Dependencies**

   ```bash
   pip install pyairtable google-generativeai python-dotenv
   ```

3. **Add the `.env` File**

   You will receive the `.env` file via email.  
   Simply place the `.env` file in the `/Users/gagan/Documents/NLP_VIT/Task1/` directory (the same location as `airtable_nlp.py`).

4. **Run the Script**

   ```bash
   python airtable_nlp.py
   ```

5. **Usage**

   - Enter your question when prompted.
   - Type `q` to exit
## Notes

- Make sure your API keys and IDs are correct in the `.env` file.
- The script will print concise answers based on your Airtable data.
   - Enter your question when prompted.
   - Type `q` to exit.
- Make sure your API keys and IDs are correct in the `.env` file.
- The script will print concise answers based on your Airtable data.

## Demo Video Link

[Watch the demo video here](https://vimeo.com/1100875865?share=copy)
