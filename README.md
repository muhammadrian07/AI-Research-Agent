# AI-Research-Agent

# System Architecture

<img width="680" height="369" alt="AI Research Agent" src="https://github.com/user-attachments/assets/25c1dd51-d1e1-45c6-a34f-5b6e95505664" />





# Use Case
Perfect for:

Research assistants
Knowledge aggregation systems
AI-powered documentation tools
Automated report generation




# 🔎 Multi-Tool Research Agent

An intelligent research assistant powered by **Google Gemini**, **LangChain**, and multiple research tools.  
It automatically selects the best information source, performs iterative reasoning, and returns structured research results.

---

## 🚀 Features

### 🧠 Multi-Tool Intelligence
Automatically decides whether to use:
- 🌐 **Web Search (DDGS)** for real-time information  
- 📖 **Wikipedia Summary** for quick overviews  
- 📚 **Wikipedia Detailed** for in-depth topic research  

Based on the user’s query, the agent selects the most relevant tool.

---

### 🔁 Agentic Loop
- Executes tools iteratively  
- Integrates feedback from previous results  
- Continues refining the answer  
- Stops when a comprehensive response is ready  

---

### 📦 Structured Output
Returns research findings in a well-defined format:

- **Topic**
- **Summary**
- **Sources**
- **Tools Used**

---

### 🔍 Smart Source Selection
- Tracks which tools were used  
- Documents sources for transparency  
- Ensures explainability of results  

---

## 🛠 Tools

### 🌐 Web Search
- Real-time web results using **DDGS**

### 📖 Wikipedia Summary
- Quick topic overviews

### 📚 Wikipedia Detailed
- In-depth Wikipedia content

---

## ⚙️ How It Works

1. User asks a research question  
2. Gemini AI analyzes the query  
3. The agent decides which tools to use  
4. Selected tools execute and return results  
5. Results are fed back into the AI for synthesis  
6. The loop continues until a complete answer is generated  
7. Final response is formatted into structured output:
   - `topic`
   - `summary`
   - `sources`
   - `tools_used`

---

## 🧰 Tech Stack

- 🐍 **Python**
- 🔗 **LangChain**
- 🤖 **Google Gemini API**
- 🌐 **DDGS (DuckDuckGo Search)**
- 📖 **Wikipedia Library**

---

## 📌 Example Output Format

```json
{
  "topic": "Artificial Intelligence",
  "summary": "Artificial Intelligence (AI) refers to...",
  "sources": [
    "https://en.wikipedia.org/...",
    "https://example.com/..."
  ],
  "tools_used": [
    "Wikipedia Summary",
    "Web Search"
  ]
}
