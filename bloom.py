def chatbot(prompt):
    import requests

    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
    # You can get your API_KEY here: https://huggingface.co/settings/tokens
                                    # Paste it below.
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        try: return response.json()
        except Exception as e: 
            if "JSONDecodeError" in str(e):
                print(e)
        
    output = query({
        "inputs": prompt,
    })

    return output