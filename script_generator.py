import os
from transformers import pipeline

def generate_spanish_script():
    # HUGGINGFACE_TOKEN, repo secrets altında tanımlı olmalı
    token = os.getenv("HUGGINGFACE_TOKEN")
    generator = pipeline(
        "text-generation",
        model="meta-llama/Llama-2-7b-chat-hf", 
        use_auth_token=token,
        device=-1
    )
    prompt = "Kısa bir İspanyolca korku-gerilim hikayesi yaz. Süre 45 saniyeyi geçmesin."
    output = generator(prompt, max_new_tokens=256, do_sample=True, temperature=0.7)
    script = output[0]["generated_text"].strip()
    with open("script.txt", "w", encoding="utf-8") as f:
        f.write(script)

if __name__ == "__main__":
    generate_spanish_script()
    print("script.txt oluşturuldu.")
