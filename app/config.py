import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    GEMINI_API_KEY: str
    # OPENAI_API_KEY: str
    PORT: str = "8080" 
    HOST: str = "0.0.0.0"  


dotenv.load_dotenv()
Settings = _Settings()