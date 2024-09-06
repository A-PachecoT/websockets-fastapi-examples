# FastAPI WebSocket Showcase

This project demonstrates the use of WebSockets with FastAPI in Python. It includes a simple chat application and a real-time data streaming example.

## Features

- Real-time chat application
- Live data streaming (simulated sensor data)
- FastAPI backend with WebSocket support
- Simple HTML/JavaScript frontend

## Project Structure

```
fastapi-websocket-showcase/
├── README.md
├── requirements.txt
├── main.py
├── static/
│ ├── chat.html
│ ├── chat.js
│ ├── data_stream.html
│ └── data_stream.js
└── app/
├── init.py
├── chat.py
├── data_stream.py
└── utils.py
```

## Setup and Running

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn main:app --reload`
4. Open your browser and navigate to:
   - Chat application: `http://localhost:8000/static/chat.html`
   - Data streaming: `http://localhost:8000/static/data_stream.html`

## Technologies Used

- Python 3.8+
- FastAPI
- WebSockets
- HTML/JavaScript (for frontend)

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or find any bugs.

## License

This project is open-source and available under the MIT License.
