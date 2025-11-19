import feedparser`nRSS="https://cryptopanic.com/feed/?filter=important"`ndef get_news():`n    f=feedparser.parse(RSS)`n    return [{"title":e.title,"link":e.link} for e in f.entries[:3]]
