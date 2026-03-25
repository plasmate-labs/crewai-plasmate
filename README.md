# crewai-plasmate

Plasmate web browsing tool for CrewAI agents. Get clean semantic page content using 10-16x fewer tokens than Chrome.

## Install

```bash
pip install crewai-plasmate
```

## Usage

```python
from crewai import Agent, Task, Crew
from crewai_plasmate import PlasmateFetchTool

researcher = Agent(role="Researcher", tools=[PlasmateFetchTool()])
task = Task(description="Fetch https://example.com and summarize it", agent=researcher)
Crew(agents=[researcher], tasks=[task]).kickoff()
```

## What is Plasmate?

[Plasmate](https://plasmate.dev) is a lightweight web browsing engine for AI agents. It returns a Semantic Object Model (SOM) instead of raw HTML, reducing token usage by 10-16x compared to headless Chrome.

## Links

- [Plasmate Documentation](https://plasmate.dev)
- [W3C Web Agents Community Group](https://www.w3.org/community/web-agents/)
- [GitHub](https://github.com/nicobailey/plasmate)

## License

Apache 2.0
