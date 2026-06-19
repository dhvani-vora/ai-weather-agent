from flask import Flask, render_template, request, redirect, url_for, session
from main_agent import agent
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/')
def home():
    if 'messages' not in session:
        session['messages'] = []

    return render_template('chat.html', messages=session['messages'])
   
@app.route('/chat', methods=['POST'])
def send():

    if 'messages' not in session:
        session['messages'] = []

    user_message = request.form['message']

    response = agent.invoke(
        {"messages": [{"role": "user", "content": user_message}]},
        {"configurable": {"thread_id": "1"}}
    )

    ai_response = response["messages"][-1].content

    session['messages'].append({
        "type": "human",
        "content": user_message
    })

    ai_content = response['messages'][-1].content

    if isinstance(ai_content, list):
        ai_content = " ".join(
            item.get("text", "")
            for item in ai_content
            if isinstance(item, dict)
    )

    session['messages'].append({
        "type": "ai",
        "content": ai_content
    })

    session.modified = True


    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)