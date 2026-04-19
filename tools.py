




from langchain_core.tools import Tool
from ddgs import DDGS
import wikipedia


def search_web(query: str) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)
        return "\n\n".join(
            f"Title: {r['title']}\nURL: {r['href']}\nSnippet: {r['body']}"
            for r in results
        )


def get_wikipedia_info(query: str, response_type: str = "simple") -> str:
    """
    Get information from Wikipedia.
    
    response_type: 'simple' for just summary, 'detailed' for summary + content
    """
    try:
        page = wikipedia.page(query)
        
        if response_type == "simple":
            return f"Title: {page.title}\n\nSummary:\n{page.summary}"
        
        else:  # detailed
            content = f"Title: {page.title}\n\nSummary:\n{page.summary}\n\n"
            content += f"Full Content:\n{page.content[:2000]}"  # First 2000 chars
            return content
            
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{query}'"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Ambiguous query. Did you mean: {', '.join(e.options[:5])}"


search_tool = Tool(
    name="search",
    func=search_web,
    description="Search the web for information on any topic. Input should be a clear search query.",
)

wikipedia_tool = Tool(
    name="wikipedia",
    func=lambda query: get_wikipedia_info(query, "simple"),
    description="Get information from Wikipedia. Returns a simple summary of the topic.",
)

wikipedia_detailed_tool = Tool(
    name="wikipedia_detailed",
    func=lambda query: get_wikipedia_info(query, "detailed"),
    description="Get detailed information from Wikipedia including full content.",
)