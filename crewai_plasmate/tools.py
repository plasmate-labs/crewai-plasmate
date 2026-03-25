"""Plasmate tools for CrewAI agents."""

import subprocess
import json
from crewai_tools import BaseTool


class PlasmateFetchTool(BaseTool):
    name: str = "Plasmate Web Fetch"
    description: str = (
        "Fetch a web page and get a clean semantic representation (SOM) "
        "instead of raw HTML. Uses 10-16x fewer tokens than Chrome. "
        "Best for reading/extracting web content."
    )

    def _run(self, url: str) -> str:
        try:
            result = subprocess.run(
                ["plasmate", "fetch", url],
                capture_output=True,
                text=True,
                timeout=30,
            )
            if result.returncode == 0:
                return result.stdout
            return f"Error fetching {url}: {result.stderr}"
        except FileNotFoundError:
            return "Plasmate not installed. Run: pip install plasmate"
        except subprocess.TimeoutExpired:
            return f"Timeout fetching {url}"
