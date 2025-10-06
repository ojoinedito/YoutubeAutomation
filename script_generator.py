from llama_cpp import Llama

def generate_spanish_script():
    model = Llama(model_path="path/to/llama2-7B.ggmlv3.q4_0.bin")
    prompt = "Kısa bir İspanyolca korku-gerilim hikayesi yaz. Süre 45 saniyeyi geçmesin."
    output = model(prompt, max_tokens=256, temperature=0.7)
    script = output['choices'][0]['text'].strip()
    with open("script.txt", "w", encoding="utf-8") as f:
        f.write(script)

if __name__ == "__main__":
    generate_spanish_script()
    print("script.txt oluşturuldu.")
