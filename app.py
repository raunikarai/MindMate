from flask import Flask, render_template,request,jsonify
from sqlalchemy import text
from database import db,init_db
from config import OPENAI_API_KEY
import openai
app=Flask(__name__)

init_db(app)

@app.route('/')
def home():
    '''try:
        # Try running a simple query
        with app.app_context():
          db.session.execute(text('SELECT 1'))
        return '✅ Database connected!'
    except Exception as e:
        return f'❌ Failed to connect: {str(e)}'''
    return render_template('home.html')
    
@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

'''@app.route('/chat')
def chat_page():
    return render_template('chat.html')'''


    

if __name__ == '__main__':
    app.run(debug=True)
