# AI Trading Analyst

An AI-powered stock analysis application that combines real-time market data, technical indicators, and Large Language Models (LLMs) to generate trading insights. The application features a Streamlit frontend, a FastAPI backend, and is containerized using Docker before being deployed on Google Cloud Run.

---

## System Architecture

![System Architecture](https://github.com/user-attachments/assets/8d2763c1-57b6-44c4-b114-3839c33b53d1)

The application follows a two-tier architecture where the Streamlit frontend communicates with a FastAPI backend through REST APIs. The backend retrieves historical market data from Yahoo Finance, computes technical indicators, and sends the processed data to the OpenAI API for AI-powered analysis before returning the results to the frontend.

---

## Application

<img width="2344" height="1066" alt="image" src="https://github.com/user-attachments/assets/ee324340-b0ea-4ffa-bba6-f57035615d64" />

The user enters a stock ticker and can optionally upload a stock chart for visual analysis. The frontend sends the request to the backend, which gathers market data and technical indicators before generating an AI-assisted trading report.

---

## AI Trading Report

<img width="2264" height="1042" alt="image" src="https://github.com/user-attachments/assets/d0eff077-6234-462b-b6ac-d5d8ceff04c1" />

The generated report summarizes the market trend, evaluates technical indicators such as RSI, provides short-term market outlook, and produces actionable trading recommendations based on quantitative market data and AI reasoning.

---

## Features

- Real-time stock data retrieval using Yahoo Finance
- AI-generated trading insights using OpenAI API
- Technical indicator calculation (RSI)
- Optional stock chart image upload for visual analysis
- Interactive Streamlit web interface
- REST API built with FastAPI
- Dockerized frontend and backend
- Independent deployment of frontend and backend on Google Cloud Run

---

## Tech Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| AI | OpenAI API |
| Market Data | Yahoo Finance |
| Language | Python |
| Containerization | Docker |
| Cloud Platform | Google Cloud Run |
| Container Registry | Google Artifact Registry |

---

## How to Run

### Clone the repository

```bash
git clone <repository-url>
cd Trading_AI
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file containing:

```text
OPENAI_API_KEY=your_api_key
BACKEND_URL=http://localhost:8000
```

### Run the backend

```bash
uvicorn backend.main:app --reload
```

### Run the frontend

```bash
streamlit run app.py
```

---

## Future Improvements

- Support multiple LLM providers (OpenAI, Gemini, etc.)
- Portfolio management and watchlists
- Authentication and user accounts
- Advanced technical indicators
- Historical trade performance analysis
