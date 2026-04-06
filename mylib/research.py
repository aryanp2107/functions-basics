import wikipedia

def get_wiki_summary(topic: str) -> str:
    return wikipedia.summary(topic)

def get_wiki_pages(topic: str) -> list:
    return wikipedia.search(topic)

def get_wiki_keywords(topic: str) -> list:
    summary = wikipedia.summary(topic)
    words = set(summary.lower().split())
    return list(words)