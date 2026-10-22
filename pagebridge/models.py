from dataclasses import dataclass


@dataclass
class PageResult:
    url: str
    title: str
    content: str
    method: str = "http"