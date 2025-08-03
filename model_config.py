from llama_cpp import Llama

def load_model(model_path="models/gemma-3n-it-Q4_K_M.gguf"):
    return Llama(
        model_path=model_path,
        n_ctx=2048,
        n_threads=6,
        use_mlock=True  # Optional
    )
    
