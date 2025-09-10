from agents import init_agent
from memory import init_memory
from prompts import narrative_prompt, combat_prompt, npc_prompt
from retriever import build_vector_store, save_vector_store, add_event_to_vectorstore
from utils import load_story, save_story
from dotenv import load_dotenv

load_dotenv()

def run_game():
    print("🌌 Welcome to Chronicles of the Multiverse! (Type Q to quit)")

    memory = init_memory()
    agent = init_agent(memory)
    story_state = load_story()
    vectorstore = build_vector_store()  # safe: returns None if no events

    while True:
        user_input = input("You: ")
        if user_input.strip().upper() == "Q":
            print("Master: Farewell, traveler.")
            save_story(story_state)
            save_vector_store(vectorstore)
            break

        # Select prompt type
        if "fight" in user_input.lower() or "attack" in user_input.lower():
            prompt = combat_prompt
        elif "talk" in user_input.lower() or "npc" in user_input.lower():
            prompt = npc_prompt
        else:
            prompt = narrative_prompt

        # Format input
        chat_history = memory.load_memory_variables({})["chat_history"]
        query = prompt.format(input=user_input, chat_history=chat_history)

        # Run agent
        response = agent.invoke(query)

        # Extract the actual text safely
        if isinstance(response, dict):
            ai_text = response.get("output", "")
        else:
            ai_text = str(response)

        print("Master:", ai_text)

        # Save major events dynamically
        major_event = None
        if "quest" in ai_text.lower():
            story_state["quests"].append(ai_text)
            major_event = f"Quest: {ai_text}"
        if "sword" in ai_text.lower() or "item" in ai_text.lower():
            story_state["inventory"].append(ai_text)
            major_event = f"Item acquired: {ai_text}"

        if major_event:
            vectorstore = add_event_to_vectorstore(vectorstore, major_event)


if __name__ == '__main__':
    run_game()
