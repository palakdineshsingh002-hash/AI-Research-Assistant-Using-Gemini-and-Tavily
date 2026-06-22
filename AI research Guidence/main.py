from tavily import TavilyClient
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# API Keys
gemini_key = os.getenv("GEMINI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

# Configure Gemini
genai.configure(api_key=gemini_key)

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Tavily Client
tavily = TavilyClient(api_key=tavily_key)

print("===== AI RESEARCH ASSISTANT =====")

# User Input
topic = input("\nEnter Research Topic: ")

print("\nSearching the Internet...\n")

# Search using Tavily
search_result = tavily.search(
    query=topic,
    search_depth="advanced",
    max_results=5
)

# Collect search content
research_text = ""

for item in search_result["results"]:
    research_text += item["content"] + "\n\n"

print("Generating Research Report...\n")

# Prompt
prompt = f"""
You are an AI Research Assistant.

Research Topic:
{topic}

Research Data:
{research_text}

Generate a report with:

1. Introduction
2. Top 5 Insights
3. Advantages
4. Challenges
5. Future Scope
6. Conclusion
"""

# Gemini Response
response = model.generate_content(prompt)

print("\n===== RESEARCH REPORT =====\n")
print(response.text)