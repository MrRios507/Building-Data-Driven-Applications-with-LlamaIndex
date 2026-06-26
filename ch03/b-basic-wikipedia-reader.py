import wikipedia
from llama_index.readers.wikipedia import WikipediaReader

# Forzamos un User-Agent para que Wikipedia no rechace la conexión
wikipedia.set_user_agent("MiAplicacionLlamaIndex/1.0 (contacto@tu-email.com)")

loader = WikipediaReader()
documents = loader.load_data(
    pages=['Pythagorean theorem','Large Language Model']
)

print(f"loaded {len(documents)} documents")