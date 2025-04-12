from flask import Flask, request, jsonify, render_template
from groq import Groq

app = Flask(__name__)

def generate_response(user_query):
    client = Groq(api_key="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")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": user_query,
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_query = data.get('query', '')
    
    # Use your generate_response function
    ai_response = generate_response(user_query)
    
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)