# Technology Stack

## Build System & Package Management
- **Poetry**: Used for dependency management and packaging
- **Python 3.11+**: Minimum required Python version
- **pyproject.toml**: Project configuration and dependencies

## Core Dependencies
- **Google ADK (Agent Development Kit)**: Primary framework for agent orchestration
  - `google-adk` (>=1.6.1,<2.0.0)
  - Provides agents, sessions, runners, and workflow management
- **Rich**: Terminal UI library for enhanced console output
  - `rich` (>=14.0.0,<15.0.0)
  - Used for Matrix-themed interface, progress bars, and formatting
- **python-dotenv**: Environment variable management

## AI/LLM Integration
- **Gemini 2.0 Flash**: Primary LLM model (`gemini-2.0-flash`)
- **Multiple API Support**: Configured for Google AI, Anthropic, and Serper APIs
- **Vertex AI**: Optional Google Cloud AI platform integration

## Common Commands

### Development Setup
```bash
# Install dependencies
poetry install

# Activate virtual environment
poetry shell

# Run main application
python main.py

# Run testing/development version
python testing.py
```

### Environment Configuration
- Copy `.env.example` to `.env` (if available)
- Configure required API keys:
  - `GEMINI_API_KEY` or `GOOGLE_API_KEY`
  - `ANTHROPIC_API_KEY` (optional)
  - `SERPER_API_KEY` (optional)

## Architecture Patterns
- **Async/Await**: All agent operations are asynchronous
- **Session-based State Management**: Persistent state across interactions
- **Agent Composition**: Agents can be nested and combined in workflows
- **Factory Pattern**: Agent creation through dedicated factory functions