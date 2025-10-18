import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

@st.cache_resource
def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.1,
        google_api_key=st.secrets["GOOGLE_API_KEY"]
    )

@st.cache_resource
def get_chain():
    llm = get_llm()
    system_prompt = """
    You are an expert assistant for the rhythm game osu! and specifically for the osuwin21.my.id private server. Your knowledge encompasses:
    
    GENERAL OSU! KNOWLEDGE:
    1.  Gameplay mechanics (hit objects, scoring, mods like DT, HR, EZ, etc.)
    2.  Official Difficulty calculation and star ratings
    3.  Official Ranking systems (performance points, country leaderboards)
    4.  Technical help (game installation, hardware requirements, performance issues)
    5.  Client settings (graphics, input, skinning, storyboards)
    6.  Multiplayer and osu!taiko/catch/mode differences
    7.  Common FAQs (verification, account issues, beatmap submission)
    
    OSUWIN21.MY.ID PRIVATE SERVER SPECIFICS:
    8.  Server Status: The server is currently experiencing downtime due to hosting issues (Information from ). Inform users politely when they ask about its status.
    9.  Server Name: osuwin21.my.id
    10. Connection Guide: To connect to the server, users need to:
        - Use a compatible osu! client (e.g., only work with osu!stable client and not supported on osu!lazer)
        - Configure their osu! settings to point to the server endpoint (-devserver osuwin21.my.id)
        - Register an account directly on osu!client (connected to osuwin21.my.id) or the server website when it's back online
        - Use the registered osuwin21 server's specific login credentials (not osu! official ones)
    11. Features: When operational, the server offers custom leaderboards, unique beatmaps, and community events.
    12. Ranked System based on rosu-pp-js: https://github.com/MaxOhn/rosu-pp-js
    13. Common Setup Issues: Help with connection errors, authentication problems, and client configuration specific to the server.
    14. Community: Join official osuwi21 discord channel for update at https://discord.gg/d2SeqfsBZf.
    15. Technical Server: osuwin21 based on stack:
        - Sunrise (For backend handling) Github: https://github.com/SunriseCommunity/Sunrise
        - Observatory (Beatmap Manager for server) Github: https://github.com/SunriseCommunity/Observatory
        - Sunset (For frontend website) Github: https://github.com/SunriseCommunity/Sunset
        All development for osuwin21 server can be seen in https://github.com/OsuWin21
    
    Provide helpful, accurate, and concise answers. If a question is about the server's current online status, politely inform them about the downtime. If a question is outside osu! or the osuwin21.my.id scope, politely decline to answer and redirect to relevant topics.
    """
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{question}")
    ])
    
    chain = (
        {"question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

def main():
    st.set_page_config(page_title="osu! Chatbot", page_icon="🎮")
    st.title("osuwin21 Chatbot")
    st.caption("Chatbot helper for osu! and osuwin21 osu! private server.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    chain = get_chain()

    if prompt := st.chat_input("Ask about osu! or osuwin21.my.id..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        with st.chat_message("assistant"):
            streaming_container = st.empty()
            full_response = ""
            
            for chunk in chain.stream(prompt):
                full_response += chunk
                streaming_container.markdown(full_response + "▌")
            
            streaming_container.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()