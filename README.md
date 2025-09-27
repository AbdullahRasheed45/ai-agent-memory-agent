# 🧠 AI Agent: Memory Agent

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Agno](https://img.shields.io/badge/Agno-Framework-purple?style=for-the-badge)](https://agno.dev/)

## Overview

**AI Agent: Memory Agent** demonstrates the power of persistent AI memory systems that remember user interactions across conversations. Built with the Agno framework and Nebius AI models, this agent maintains long-term memory, learns from conversations, and provides increasingly personalized responses over time.

Unlike traditional stateless chatbots, this memory agent builds a comprehensive understanding of users, their preferences, history, and context, creating truly personalized AI experiences.

### 🌟 Key Features

- **Persistent Memory System**: SQLite-backed storage for long-term user information retention
- **Autonomous Memory Management**: AI agent automatically creates, updates, and organizes memories
- **Contextual Conversations**: Leverages chat history and user memories for relevant responses
- **Real-time Streaming**: Live response generation with visible processing steps
- **Beautiful Console Output**: Rich library integration for enhanced terminal experience
- **Modular Architecture**: Easy to extend and integrate with other systems
- **Memory Categorization**: Automatically classifies and stores different types of user information

### 🎯 Perfect For

- **Personalized AI Assistants**: Create AI that remembers user preferences and history
- **Customer Service Bots**: Maintain customer interaction history and preferences
- **Educational AI Tutors**: Remember student progress and learning patterns
- **Research & Development**: Explore advanced AI memory architectures
- **Proof of Concept**: Demonstrate persistent AI capabilities to stakeholders

## 🏗️ System Architecture

The Memory Agent uses a sophisticated multi-layer architecture for intelligent memory management:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │ ──▶│   Memory Agent   │ ──▶│   Response      │
│                 │    │   (Agno + AI)    │    │   Generation    │
│ "I support      │    │                  │    │                 │
│  Mohun Bagan"   │    │ • Memory Extract │    │ • Personalized  │
│                 │    │ • Context Build  │    │ • History-aware │
│                 │    │ • Response Gen   │    │ • Streaming     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SQLite Database   │
                    │                     │
                    │ ┌─────────────────┐ │
                    │ │ User Memories   │ │
                    │ │ • Facts         │ │
                    │ │ • Preferences   │ │
                    │ │ • Timestamps    │ │
                    │ └─────────────────┘ │
                    │                     │
                    │ ┌─────────────────┐ │
                    │ │ Agent Sessions  │ │
                    │ │ • Conversations │ │
                    │ │ • Full Context  │ │
                    │ │ • History       │ │
                    │ └─────────────────┘ │
                    └─────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Nebius AI API key
- Basic understanding of AI agents (helpful but not required)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbdullahRasheed45/ai-agent-memory-agent.git
   cd ai-agent-memory-agent
   ```

2. **Set up environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   # Using uv (recommended - faster)
   pip install uv
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

4. **Configure API key:**
   ```bash
   # Create .env file
   echo "NEBIUS_API_KEY=your_nebius_api_key_here" > .env
   ```

### Run the Demo

```bash
uv run main.py
# Or: python main.py
```

## 💫 Demo Experience

The interactive demo showcases three key memory capabilities:

### Step 1: Initial Information Gathering
```
Input: "My name is Arindam and I support Mohun Bagan."

Agent Response: Hello Arindam! Nice to meet a Mohun Bagan supporter! 
I'll remember that you're passionate about one of India's most historic football clubs.

Memory Created:
✓ User name: Arindam
✓ Football team preference: Mohun Bagan
```

### Step 2: Contextual Problem Solving
```
Input: "I live in Kolkata, where should I move within a 4-hour drive?"

Agent Response: Based on your location in Kolkata and your love for Mohun Bagan,
I'd suggest considering Bhubaneswar - it's about 3.5 hours away, has great
infrastructure, and you'll still be close enough to attend Mohun Bagan matches!

Memory Updated:
✓ Location: Kolkata
✓ Considering relocation within 4-hour radius
```

### Step 3: Memory Recall and Personalization
```
Input: "Tell me about Arindam."

Agent Response: You're Arindam, a Mohun Bagan supporter living in Kolkata who's
considering relocating within a 4-hour drive from the city. You seem to value
staying connected to your football passion while exploring new opportunities.

Memory Retrieved:
✓ Complete user profile reconstruction
✓ Contextual relationship understanding
```

## 🔧 Advanced Configuration

### Memory System Customization

```python
# In main.py - customize memory behavior
agent_config = {
    "enable_agentic_memory": True,      # AI manages its own memories
    "enable_user_memories": True,       # Extract user-specific information
    "add_history_to_messages": True,    # Include conversation history
    "num_history_runs": 3,              # Number of previous conversations
}

# Database customization
database_config = {
    "db_path": "custom_memory.db",      # Custom database location
    "memory_retention_days": 365,       # How long to keep memories
    "max_memories_per_user": 1000,      # Memory limit per user
}
```

### Model Configuration

```python
# Switch between different AI models
model_options = {
    "default": "DeepSeek-V3-0324",      # Balanced performance
    "fast": "DeepSeek-Coder",           # Quick responses
    "advanced": "DeepSeek-V3",          # Enhanced reasoning
}
```

## 🗃️ Database Schema

### User Memories Table
```sql
CREATE TABLE user_memories (
    id INTEGER PRIMARY KEY,
    user_id TEXT NOT NULL,
    memory_text TEXT NOT NULL,
    memory_type TEXT DEFAULT 'general',
    importance_score REAL DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Agent Sessions Table
```sql
CREATE TABLE agent_sessions (
    id INTEGER PRIMARY KEY,
    session_id TEXT UNIQUE,
    user_id TEXT NOT NULL,
    messages TEXT NOT NULL,  -- JSON format
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🛠️ Extending the System

### Adding Custom Memory Types

```python
# Example: Location-based memories
class LocationMemoryHandler:
    def extract_location_info(self, message):
        # Custom logic for location extraction
        pass
    
    def update_location_context(self, user_id, location):
        # Update user's location-based memories
        pass
```

### Integration with External Systems

```python
# Example: CRM integration
class CRMIntegration:
    def sync_memories_to_crm(self, user_id, memories):
        # Sync AI memories with CRM system
        pass
    
    def import_customer_data(self, customer_id):
        # Import existing customer data as memories
        pass
```

## 🔍 Memory Analytics

The system provides insights into memory usage and effectiveness:

### Memory Statistics
```python
# View memory statistics
python -c "
from memory_analytics import get_stats
stats = get_stats()
print(f'Total users: {stats.total_users}')
print(f'Total memories: {stats.total_memories}')
print(f'Average memories per user: {stats.avg_memories}')
"
```

### Memory Quality Analysis
- **Relevance scoring**: How useful memories are for responses
- **Retention patterns**: Which memories are accessed most frequently
- **User engagement**: Correlation between memory depth and conversation quality

## 🚨 Troubleshooting

### Common Issues

**"API Key Invalid"**
- Verify Nebius AI API key is correct in `.env` file
- Check API key permissions and rate limits
- Ensure proper environment variable loading

**"Database Connection Error"**
- Check file permissions in project directory
- Verify SQLite installation
- Try deleting `memory_agent.db` to reset database

**"Memory Not Persisting"**
- Confirm database write permissions
- Check for memory extraction configuration
- Verify user_id consistency across sessions

**"Slow Response Times"**
- Adjust `num_history_runs` to reduce context size
- Consider using faster model variants
- Optimize memory query patterns

### Performance Optimization

**Memory Management:**
- Regular cleanup of old, unused memories
- Implement memory importance scoring
- Use efficient indexing for large user bases

**Response Speed:**
- Cache frequently accessed memories
- Optimize database queries with proper indexes
- Consider memory summarization for long histories

## 🔮 Advanced Use Cases

### Multi-User Support
```python
# Handle multiple users with isolated memories
def create_user_session(user_id, session_id):
    return MemoryAgent(
        user_id=user_id,
        session_id=session_id,
        isolation_mode=True
    )
```

### Memory Sharing Between Agents
```python
# Share memories across different AI agents
def share_memories(source_user, target_agent, memory_types):
    shared_memories = get_memories(source_user, memory_types)
    target_agent.import_memories(shared_memories)
```

### Integration with Vector Databases
```python
# For semantic memory search
from vector_memory import VectorMemoryStore

vector_store = VectorMemoryStore()
semantic_memories = vector_store.similarity_search(
    query="football preferences", 
    user_id="user123"
)
```

## 🤝 Contributing

We welcome contributions to enhance the memory agent capabilities!

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/memory-enhancement`
3. Set up development environment: `uv sync --dev`
4. Make your changes and add tests
5. Run tests: `pytest tests/`
6. Submit a pull request

### Contribution Ideas

- **Vector Memory Search**: Implement semantic similarity for memory retrieval
- **Memory Visualization**: Create dashboards for memory analytics
- **Multi-Modal Memories**: Support for images, audio, and video memories
- **Memory Compression**: Efficient storage for long-term memory systems
- **Privacy Controls**: User-controlled memory deletion and privacy settings

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Agno Framework](https://agno.dev/)** for advanced AI agent infrastructure
- **[Nebius AI](https://nebius.ai/)** for powerful language model capabilities
- **[Rich](https://rich.readthedocs.io/)** for beautiful console interfaces
- **SQLite Community** for reliable embedded database technology

## 📞 Contact

**Muhammad Abdullah Rasheed**
- 🌐 Portfolio: [techvibes360.com](https://techvibes360.com)
- 💼 LinkedIn: [abdullah-rasheed](https://www.linkedin.com/in/abdullahrasheed-/)
- 📧 Email: abdullahrasheed45@gmail.com

---

*Built with ❤️ by Muhammad Abdullah Rasheed. Ready to give your AI agents a memory that never forgets?*
