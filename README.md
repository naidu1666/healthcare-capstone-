
# Healthcare Secure Transfer

This project provides a secure file transfer system with user authentication, encryption, and MySQL integration.

## How to Run (Non-Docker)

1. Install MySQL server
2. Import database: `mysql -u root -p < mysql/healthcare_db.sql`
3. Start backend:
```
cd backend
pip install -r requirements.txt
python app.py
```
4. Start frontend:
```
cd frontend
npm install
npm start
```
