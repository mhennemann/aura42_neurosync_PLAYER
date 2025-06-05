# config.py
import os

USE_LOCAL_LLM = True
USE_STREAMING = True
LLM_API_URL = "http://127.0.0.1:5050/generate_llama"
LLM_STREAM_URL = "http://127.0.0.1:5050/generate_stream"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR-KEY-GOES-HERE")

MAX_CHUNK_LENGTH = 500
FLUSH_TOKEN_COUNT = 300

DEFAULT_VOICE_NAME = 'bf_isabella'
USE_LOCAL_AUDIO = True
LOCAL_TTS_URL = "http://127.0.0.1:8000/generate_speech" 
USE_COMBINED_ENDPOINT = False

ENABLE_EMOTE_CALLS = False
USE_VECTOR_DB = False


BASE_SYSTEM_MESSAGE = "You are Mai, be nice.\n\n"

# ---------------------------
# Emote Sender Configuration (new)
# ---------------------------
EMOTE_SERVER_ADDRESS = "127.0.0.1"
EMOTE_SERVER_PORT = 7777

# ---------------------------
# Transcription Server Configuration (new)
# ---------------------------
TRANSCRIPTION_SERVER_URL = "http://127.0.0.1:6969/transcribe"

# ---------------------------
# Embedding Configurations (new)
# ---------------------------
# Toggle between local embeddings and OpenAI embeddings.
USE_OPENAI_EMBEDDING = False
# Local embedding server URL:
EMBEDDING_LOCAL_SERVER_URL = "http://127.0.0.1:7070/get_embedding"
# OpenAI embedding model and size.
EMBEDDING_OPENAI_MODEL = "text-embedding-3-small"
LOCAL_EMBEDDING_SIZE = 768
OPENAI_EMBEDDING_SIZE = 1536

# ---------------------------
# Neurosync API Configurations (new)
# ---------------------------

NEUROSYNC_LOCAL_URL = "http://127.0.0.1:5000/audio_to_blendshapes" # if using the realtime api below, you can still access this endpoint from it, just change the port to 6969

# ---------------------------
# TTS with Blendshapes Endpoint (new)
# ---------------------------
TTS_WITH_BLENDSHAPES_REALTIME_API = "http://127.0.0.1:8000/synthesize_and_blendshapes"

### ignore these
NEUROSYNC_API_KEY = "YOUR-NEUROSYNC-API-KEY" # ignore this 
NEUROSYNC_REMOTE_URL = "https://api.neurosync.info/audio_to_blendshapes" #ignore this


def get_llm_config(system_message=None):
    """
    Returns a dictionary of LLM configuration parameters.
    
    If no system_message is provided, it defaults to BASE_SYSTEM_MESSAGE.
    """
    if system_message is None:
        system_message = BASE_SYSTEM_MESSAGE
    return {
        "USE_VECTOR_DB":USE_VECTOR_DB,
        "USE_LOCAL_LLM": USE_LOCAL_LLM,
        "USE_STREAMING": USE_STREAMING,
        "LLM_API_URL": LLM_API_URL,
        "LLM_STREAM_URL": LLM_STREAM_URL,
        "OPENAI_API_KEY": OPENAI_API_KEY,
        "max_chunk_length": MAX_CHUNK_LENGTH,
        "flush_token_count": FLUSH_TOKEN_COUNT,
        "system_message": system_message,
    }


def setup_warnings():
    """
    Set up common warning filters.
    """
    import warnings
    warnings.filterwarnings(
        "ignore", 
        message="Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work"
    )
