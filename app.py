from app import create_app, db
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")
        print(f"Secret key loaded: {'Yes' if app.config['SECRET_KEY'] else 'No'}")
    
    print("Starting Flask application...")
    print("API Documentation available at: http://localhost:5000/api/health")
    app.run(host='127.0.0.1', port=5000, debug=True)
