import os
import json
from pyairtable import Api
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
api = Api(os.environ['AIRTABLE_API'])
table = api.table(os.environ['AIRTABLE_BASE_ID'], os.environ['AIRTABLE_TABLE_ID'])
tableInfo = table.all()

table_info_text = json.dumps(tableInfo, indent=2)
chat_history = []

while True:
    query = input("Enter your question (type 'q' to exit): ")
    if query.lower() == 'q':
        print("Exiting...")
        break
    chat_history.append({"role": "user", "content": query})
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = (
        "Here is the Airtable data:\n"
        f"{table_info_text}\n"
        "Chat history:\n"
        f"{json.dumps(chat_history, indent=2)}\n"
        f"Respond to the latest user question. The response should be a one-liner answer."
    )
    response = model.generate_content(prompt)
    chat_history.append({"role": "assistant", "content": response.text})
    print(response.text)