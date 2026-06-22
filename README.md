# AI Research Assistant Using Gemini and Tavily

## Overview
This project is an AI-powered Research Assistant built using Google's Gemini API and Tavily Search API. It can perform web research, gather information from multiple sources, and generate concise summaries for user queries.

The assistant combines the power of Large Language Models (LLMs) with real-time web search to provide accurate and up-to-date information.

## Features
- Real-time web search using Tavily API
- AI-powered summarization using Gemini
- User-friendly interface
- Fast and accurate research results
- Easy to customize and extend

## Technologies Used
- Python
- Google Gemini API
- Tavily Search API
- Streamlit (if used)
- Environment Variables (.env)

## Project Structure

```text
AI-Research-Assistant-Using-Gemini-and-Tavily/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
└── screenshots/
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Research-Assistant-Using-Gemini-and-Tavily.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-Research-Assistant-Using-Gemini-and-Tavily
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Run the Application

```bash
python app.py
```

## How It Works

1. User enters a research query.
2. Tavily searches the web for relevant information.
3. Retrieved content is processed and analyzed.
4. Gemini generates a concise and meaningful summary.
5. Results are displayed to the user.

## Example Query

```text
What are the latest advancements in Artificial Intelligence?
```

## Example Output

```text
Recent advancements in AI include multimodal models, AI agents,
reasoning models, healthcare applications, and autonomous systems.
```

## Learning Outcomes

Through this project, I learned:

- Working with APIs
- Prompt Engineering
- AI Agent Development
- Web Search Integration
- Environment Variable Management
- Research Automation

## Future Improvements

- Multi-source citation support
- PDF report generation
- Voice-based interaction
- Advanced research workflows
- Export results to documents

## Author

**Hans Chauhan**

B.Tech CSE (AI & ML) Student  
AI Enthusiast | NDA Aspirant | Python Learner

## Demo Video

Add your Loom video link here:

```
https://your-loom-link.com
```

## License

This project is created for educational and learning purposes.
