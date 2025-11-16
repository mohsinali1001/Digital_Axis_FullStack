# DigitalAxis Full-Stack Attack Detection System

A complete full-stack application for AI-powered attack detection with real-time monitoring, API key management, and dashboard analytics.

## Architecture

- **Backend**: Node.js/Express with PostgreSQL
- **Model Service**: Python FastAPI microservice
- **Frontend**: React + Tailwind CSS
- **Real-time**: Socket.IO for live updates
- **Database**: PostgreSQL

## Project Structure

```
Digital_Axis_FullStack/
├── backend/                 # Node.js/Express backend
│   ├── config/            # Database configuration
│   ├── controllers/       # Route controllers
│   ├── middleware/        # Auth & API key middleware
│   ├── migrations/           # Database setup scripts
│   ├── model/            # Model proxy
│   ├── routes/           # API routes
│   └── server.js         # Main server file
├── model_service/        # Python FastAPI microservice
│   ├── app.py           # FastAPI application
│   ├── model/           # ML model (pipe.pkl)
│   └── requirements.txt
└── Digital_Axis_AI_Attack_Detector_Website/  # React frontend
    ├── src/
    │   ├── components/
    │   │   ├── Dashboard/  # Dashboard pages
    │   │   └── auth/      # Auth components
    │   └── api/           # API client
    └── public/            # Static files
```

## Setup Instructions

### 1. Database Setup

```bash
cd backend
npm install
npm run setup-full-schema
```

### 2. Backend Setup

```bash
cd backend
npm install
# Create .env file with:
# PORT=5000
# JWT_SECRET=your_secret_key
# DATABASE_URL=postgresql://user:password@localhost:5432/digitalaxis_db
npm run dev
```

### 3. Model Service Setup

```bash
cd model_service
pip install -r requirements.txt
# Ensure pipe.pkl is in model_service/model/
uvicorn app:app --reload --port 8000
```

### 4. Frontend Setup

```bash
cd Digital_Axis_AI_Attack_Detector_Website
npm install
npm start
```

## Running the Application

1. **Start PostgreSQL** (ensure it's running on port 5432)

2. **Start the backend**:
   ```bash
   cd backend
   npm run dev
   ```
   Backend runs on http://localhost:5000

3. **Start the model service**:
   ```bash
   cd model_service
   uvicorn app:app --reload --port 8000
   ```
   Model service runs on http://localhost:8000

4. **Start the frontend**:
   ```bash
   cd Digital_Axis_AI_Attack_Detector_Website
   npm start
   ```
   Frontend runs on http://localhost:3000 or http://localhost:5173

## API Endpoints

### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - Login user

### API Keys (JWT required)
- `GET /api/apikeys` - List all API keys
- `POST /api/apikeys` - Create new API key
- `PUT /api/apikeys/:keyId/regenerate` - Regenerate API key
- `DELETE /api/apikeys/:keyId` - Delete API key

### Predictions
- `POST /api/predict` - Make prediction (requires x-api-key header)
- `GET /api/dashboard/overview` - Get dashboard overview (JWT required)
- `GET /api/dashboard/predictions` - Get predictions list (JWT required)

## Client Script Usage

1. Get your API key from the dashboard
2. Copy the client script from the "Client Script" page
3. Replace `YOUR_API_KEY_HERE` with your actual key
4. Paste the script before `</body>` tag in your HTML

The script will automatically send events on page load and expose `window.DA.sendEvent()` for manual events.

## Testing

Use the test client page at `public/test-client.html` to test the API integration.

## Environment Variables

### Backend (.env)
```
PORT=5000
JWT_SECRET=your_secret_key_here
DATABASE_URL=postgresql://postgres:1234@localhost:5432/digitalaxis_db
```

## Features

- ✅ User authentication (JWT)
- ✅ API key management
- ✅ Real-time prediction monitoring (Socket.IO)
- ✅ Dashboard with analytics
- ✅ Client script for easy integration
- ✅ Comprehensive logging and monitoring
- ✅ ML model integration via FastAPI

## License

ISC

