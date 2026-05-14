# Scraping Pipeline — Material de Estudo

Projeto prático para estudo de web scraping em Python, construído de forma incremental cobrindo desde fundamentos até uma pipeline completa de coleta de dados.

## Tecnologias

- **Python 3.10+**
- **aiohttp** — requisições HTTP assíncronas
- **BeautifulSoup4** — parsing de HTML
- **SQLAlchemy** — ORM e acesso ao banco de dados
- **FastAPI** — API REST
- **Docker** — containerização
- **pytest** — testes

## Estrutura do Projeto

```
src/
├── models/          # Entidades de dados (dataclasses)
├── scrapers/        # Scrapers síncronos e assíncronos
├── parsers/         # Estratégias de parsing (Strategy pattern)
├── repositories/    # Acesso a dados (Repository pattern)
├── utils/           # Utilitários (retry, rate limiting, etc.)
└── api/             # API REST com FastAPI
tests/
├── unit/
└── integration/
```

## Conceitos Abordados

- Padrões de projeto: Strategy, Template Method, Repository, Factory
- Princípios SOLID aplicados a scraping
- Programação assíncrona com `asyncio` e `aiohttp`
- Controle de concorrência com `Semaphore`
- Retry com backoff exponencial
- Persistência com SQLAlchemy (async)
- Testes com pytest e mocks
- Containerização com Docker e Docker Compose

## Como rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a pipeline
python3 -c "
import asyncio
from src.parsers.parser import SimpleHTMLParser
from src.repositories.repository import InMemoryArticleRepository
from src.scrapers.async_scraper import AsyncScraper

async def main():
    scraper = AsyncScraper(
        parser=SimpleHTMLParser(),
        repository=InMemoryArticleRepository(),
        max_concurrent=5
    )
    await scraper.run_many(['https://agenciabrasil.ebc.com.br/'])
    
asyncio.run(main())
"
```
