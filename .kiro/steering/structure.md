# Project Structure

## Root Level
- `main.py`: Primary application entry point with main agent orchestration
- `testing.py`: Development/testing entry point for experimenting with agents
- `pyproject.toml`: Poetry configuration and dependencies
- `.env`: Environment variables and API keys (not committed)
- `.gitignore`: Git ignore patterns for Python projects

## Core Directories

### `/agents`
Individual agent implementations organized by agent type:
- Each agent has its own subdirectory (e.g., `cpu_agent/`, `task_planner_agent/`)
- Agent factory functions follow naming pattern: `get_{agent_name}_agent()`
- `__init__.py`: Package initialization (currently empty)

### `/agents_workflows`
Complex agent workflows and orchestration patterns:
- `self_reflect_agent_workflow.py`: Main workflow combining agents with self-reflection
- Individual workflow subdirectories for complex workflows
- Factory functions follow pattern: `get_{workflow_name}_workflow()`

### `/global_tools`
Shared tools and utilities available to all agents:
- `exit_loop_tool.py`: Tool for breaking out of agent loops
- Reusable agent tools and utilities

### `/ui`
Rich-based terminal interface components:
- `components.py`: Core UI components with Matrix theme
- `agent_response.py`: Agent response formatting
- `data_display.py`: Data visualization components
- `input.py`: User input handling
- `layouts.py`: UI layout management
- `output.py`: Output formatting
- `status.py`: Status display components
- `scheduler_display.py`: Scheduler-related UI
- `event_content.py`: Event content display
- `metadata.py`: Metadata display utilities

### `/utils`
Utility functions and helpers:
- `/llm`: LLM-related utilities and helper functions
- Common utilities shared across the application

## Naming Conventions

### Agent Files
- Agent directories: `{agent_name}_agent/`
- Agent factory functions: `get_{agent_name}_agent()`
- Agent workflow functions: `get_{workflow_name}_workflow()`

### State Management
- Session state keys use snake_case
- Common state keys: `user_request`, `last_response`, `last_reflect`
- Task-specific keys: `task_for_powershell_script_writer`

### Code Style
- All async functions for agent operations
- Factory pattern for agent creation
- Rich library for all terminal output
- Environment variables for configuration