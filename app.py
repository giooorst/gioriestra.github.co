from flask import Flask, jsonify

client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route("/prompt")
def prompt():
    question = request.args.get('question')

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question}
        ]
    )
    data = {'response': completion.choices[0].message.content}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)