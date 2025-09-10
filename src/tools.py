from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool
from dotenv import load_dotenv

load_dotenv()

def init_tools():
  serp_wrapper = SerpAPIWrapper()
  serp_tool = Tool(
      name="Search",
      func=serp_wrapper.run,
      description="Useful for answering questions by searching the web"
  )
  wiki=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

  return [wiki,serp_tool]
