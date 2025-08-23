import gradio as gr
import time
import textwrap
import json

# --- 1. CSS & HTML for Styling ---
app_css = """
/* General Styling */
.gradio-container { font-family: 'Inter', sans-serif; background-color: #f8fafc; }

/* Main Layout */
.main-container { display: flex; flex-direction: row; gap: 2rem; }
.chat-column { flex-grow: 2; }
.memory-column { flex-grow: 1; min-width: 350px; }

/* Chatbot Styling */
.chatbot { background-color: #f1f5f9; border-radius: 1rem; }
.chatbot .message-bubble { box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1) !important; }
.chatbot .user { background: #2563eb !important; color: white !important; }
.chatbot .bot { background: white !important; color: #1e293b !important; }

/* Memory Panel Styling */
.memory-panel {
    background-color: white;
    border: 1px solid #e2e8f0;
    border-radius: 1rem;
    padding: 1.5rem;
    height: 100%;
}
.memory-panel h2 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
}
.memory-panel h2 i { margin-right: 0.75rem; color: #6366f1; }
.memory-panel .json-output {
    background-color: #f8fafc;
    border-radius: 0.5rem;
    padding: 1rem;
    font-family: monospace;
    font-size: 0.875rem;
    white-space: pre-wrap;
    word-wrap: break-word;
}

/* Icon Styling */
.fa-spinner { animation: fa-spin 2s infinite linear; }
@keyframes fa-spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
"""

# --- 2. SIMULATED AGENT & MEMORY LOGIC ---
# In-memory database to simulate SqliteMemoryDb
SIMULATED_MEMORY_DB = {}

def get_user_memories(user_id):
    """Retrieves memories for a given user."""
    return SIMULATED_MEMORY_DB.get(user_id, [])

def add_user_memory(user_id, memory_text):
    """Adds a new memory for a user."""
    if user_id not in SIMULATED_MEMORY_DB:
        SIMULATED_MEMORY_DB[user_id] = []
    # Avoid duplicate memories
    if memory_text not in SIMULATED_MEMORY_DB[user_id]:
        SIMULATED_MEMORY_DB[user_id].append(memory_text)

def clear_user_memories(user_id):
    """Clears all memories for a user."""
    if user_id in SIMULATED_MEMORY_DB:
        SIMULATED_MEMORY_DB[user_id] = []
    return f"Memories cleared for user: {user_id}"

# This function simulates the response from your memory agent.
def memory_chat(message, history, user_id):
    """
    Simulates a conversational response that interacts with memory.
    """
    if not user_id:
        # Handle case where user_id is not provided
        yield history + [(message, "Please provide a User ID before starting the chat.")], "[]"
        return

    history = history or []
    
    # Simulate agent processing
    time.sleep(1.5)

    # --- Memory Interaction Logic ---
    response_text = ""
    if "my name is" in message.lower():
        name = message.split("is")[-1].strip().replace('.', '')
        add_user_memory(user_id, f"User's name is {name}.")
        response_text = f"Nice to meet you, {name}! I'll remember that."
    elif "i support" in message.lower():
        team = message.split("support")[-1].strip().replace('.', '')
        add_user_memory(user_id, f"User supports {team}.")
        response_text = f"Got it. I've noted that you're a fan of {team}."
    elif "i live in" in message.lower():
        city = message.split("in")[-1].split(",")[0].strip().replace('.', '')
        add_user_memory(user_id, f"User lives in {city}.")
        response_text = f"Okay, I'll remember that you live in {city}. If you're looking for places to visit, some options within a 4-hour drive could be Digha for the seaside or Shantiniketan for a cultural trip."
    elif "tell me about" in message.lower():
        memories = get_user_memories(user_id)
        if not memories:
            response_text = "I don't have any memories about you yet. Tell me something about yourself!"
        else:
            response_text = "Here's what I know about you:\n" + "\n".join([f"- {mem}" for mem in memories])
    else:
        response_text = "I'm a memory agent. You can tell me facts about yourself, and I'll remember them for our next conversation."

    history.append((message, response_text))
    
    # Update the memory display
    current_memories = get_user_memories(user_id)
    formatted_memories = json.dumps(current_memories, indent=2)
    
    yield history, formatted_memories


# --- 3. GRADIO UI LAYOUT ---
with gr.Blocks(css=app_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        textwrap.dedent("""
        # <i class="fas fa-brain" style="color:#6366f1;"></i> Memory Agent
        <p style="font-size:0.9rem; color:#475569;">I remember details from our conversation to provide a personalized experience.</p>
        """)
    )
    
    with gr.Row(elem_classes=["main-container"]):
        # --- Left Panel: Chat ---
        with gr.Column(elem_classes=["chat-column"]):
            chatbot = gr.Chatbot(
                elem_id="chatbot",
                bubble_full_width=False,
                height=600,
                label="Conversation with Agent"
            )
            
            with gr.Row():
                user_id_input = gr.Textbox(
                    placeholder="Enter a unique User ID...",
                    label="User ID",
                    scale=1
                )
                message_input = gr.Textbox(
                    placeholder="Type your message here...",
                    label="Your Message",
                    scale=3
                )
            
            submit_btn = gr.Button("Send Message", variant="primary")

        # --- Right Panel: Memory Display ---
        with gr.Column(elem_classes=["memory-column"]):
            with gr.Column(elem_classes=["memory-panel"]):
                gr.Markdown(
                    '<h2><i class="fas fa-database"></i>Stored Memories</h2>'
                )
                memory_display = gr.JSON(
                    label="Current Memories for User",
                    elem_classes=["json-output"]
                )
                clear_memory_btn = gr.Button("Clear Memories for this User")


    # --- Event Listeners ---
    # Combine message submission and chat logic
    submit_btn.click(
        fn=memory_chat,
        inputs=[message_input, chatbot, user_id_input],
        outputs=[chatbot, memory_display]
    ).then(
        lambda: "", message_input, message_input # Clear input after send
    )

    message_input.submit(
        fn=memory_chat,
        inputs=[message_input, chatbot, user_id_input],
        outputs=[chatbot, memory_display]
    ).then(
        lambda: "", message_input, message_input # Clear input after send
    )
    
    # Logic for clearing memories
    clear_memory_btn.click(
        fn=clear_user_memories,
        inputs=[user_id_input],
        outputs=None # No direct output, but it clears the backend
    ).then(
        fn=lambda: ([], "[]"), # Immediately clear the UI
        inputs=None,
        outputs=[chatbot, memory_display]
    )


if __name__ == "__main__":
    demo.queue()
    demo.launch(debug=True)
