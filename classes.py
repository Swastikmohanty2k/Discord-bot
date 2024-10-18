from llama_index.readers.discord import DiscordReader
from llama_index.core import Settings, VectorStoreIndex, Document
from llama_index.llms.openai import OpenAI
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter

class DiscordMessageIngestor:
    def __init__(self, discord_token, channel_ids):
        self.discord_token = discord_token
        self.channel_ids = channel_ids

    def load_messages(self, limit=100):
        reader = DiscordReader(discord_token=self.discord_token)
        messages = reader.load_data(channel_ids=self.channel_ids, oldest_first=False, limit=limit)
        return messages

    def combine_messages(self, messages):
        combined_text = "\n".join(
            [f"{message.metadata['created_at']} - {message.metadata['username']}: {message.text}" for message in messages]
        )
        return [Document(text=combined_text)]

class LlamaIndexEngine:
    def __init__(self, api_key, model="gpt-4o-mini"):
        self.client = OpenAI(api_key=api_key)
        Settings.llm = OpenAI(temperature=0, model=model)

    def create_index(self, documents):
        pipeline = IngestionPipeline(transformations=[TokenTextSplitter(chunk_size=512, chunk_overlap=256, separator="\n")])
        nodes = pipeline.run(documents=documents)
        index = VectorStoreIndex(nodes=nodes)
        return index

    def query_index(self, index, query, top_k=3):
        query_engine = index.as_query_engine(similarity_top_k=top_k)
        response = query_engine.query(query)
        return response.response
