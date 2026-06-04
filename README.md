# LangGraph Learn Project

A simple LangGraph project demonstrating a basic workflow with researcher and writer nodes using OpenRouter's LLM API.

## Project Structure

```
.
├── agent.py          # LLM node implementations (researcher, writer, chatbot)
├── app.py            # Main application that builds and runs the graph
├── state.py          # GraphState definition
├── .env              # Environment variables (API key)
└── README.md
```

## Features

- Uses LangGraph for building stateful workflows
- Demonstrates a simple linear graph: researcher → writer
- Integrates with OpenRouter API via LangChain
- Loads environment variables from `.env`

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- OpenRouter API key (get one at [openrouter.ai](https://openrouter.ai))

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd langgraph-learn
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install langgraph langchain-openai python-dotenv
   ```

4. Set up environment variables:
   - Copy the example `.env` file (if provided) or create a new one:
     ```
     API_KEY=your_openrouter_api_key_here
     ```
   - Replace `your_openrouter_api_key_here` with your actual OpenRouter API key.

## Usage

Run the application:
```bash
python app.py
```

The application will:
1. Initialize a LangGraph with two nodes: researcher and writer
2. Set the entry point to the researcher node
3. Connect researcher → writer
4. Execute the graph with the question: "How does kafka work?"
5. Print the final result

## Code Explanation

### state.py
Defines the `GraphState` TypedDict that flows through the graph:
```python
from typing import TypedDict

class GraphState(TypedDict):
    question: str
    research: str
    answer: str
```

### agent.py
Contains three node functions:
- `chatbot_node`: Simple Q&A using the LLM
- `researcher_node`: Researches a topic and returns research content
- `writer_node`: Takes research and writes a clean answer

All nodes use the same LLM configured via OpenRouter.

### app.py
Builds the graph:
1. Creates a StateGraph with GraphState
2. Adds researcher and writer nodes
3. Sets entry point to researcher
4. Adds edge from researcher to writer
5. Sets finish point to writer
6. Compiles and invokes the graph with initial state

## Customization

### Changing the Question
Modify the question in `app.py` lines 23-25:
```python
result = graph.invoke(
    {
        "question": "Your question here"
    }
)
```

### Adding More Nodes
To expand the workflow:
1. Import or create new node functions in `agent.py`
2. Add nodes in `app.py` using `builder.add_node()`
3. Connect them with `builder.add_edge()`
4. Adjust entry and finish points as needed

### Using Different Models
Change the LLM configuration in `agent.py`:
- Modify `model` parameter in `ChatOpenAI`
- Adjust `base_url` if using a different provider
- Update API key in `.env`

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure `.env` file exists in the project root
   - Verify `API_KEY` is set correctly
   - Check for typos in the key

2. **Import Errors**
   - Make sure all dependencies are installed
   - Try reinstalling: `pip install --upgrade langgraph langchain-openai python-dotenv`

3. **Network Issues**
   - Verify internet connectivity to OpenRouter API
   - Check if OpenRouter service is operational

## Contributing

Feel free to submit issues or pull requests to improve this project.

## License

This project is for educational purposes. Feel free to use and modify as needed.
