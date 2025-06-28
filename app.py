from flask import Flask, render_template,request,jsonify
from sqlalchemy import text
from database import db,init_db
app=Flask(__name__)

init_db(app)

@app.route('/')
def home():
    try:
        # Try running a simple query
        with app.app_context():
          db.session.execute(text('SELECT 1'))
        return '✅ Database connected!'
    except Exception as e:
        return f'❌ Failed to connect: {str(e)}'
    #return render_template('home.html')
    
@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html')


    

if __name__ == '__main__':
    app.run(debug=True)
