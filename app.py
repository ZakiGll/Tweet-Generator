import streamlit as st
from ctransformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
        'mistral-7b-instruct-v0.1.Q5_K_M.gguf', 
        model_type='mistral',
        temperature=0.8, 
        )

def main():

    st.set_page_config(page_title="TweetCraft", page_icon="📝")
    st.header("📝 Let's Craft Outstanding Tweets Together!")
    prompt_input = st.text_input("🎯 Enter the topic of your next tweet...")

    if prompt_input != "":
        for i in range(3):
            tweet = model(f"Your mission: creat a tweet of three sentences with the perfect hashtags at the end of the tweet for this topic:'{prompt_input}' A:")
            with st.expander(f"Tweet suggestion {i+1}"):
                st.write(tweet)


if __name__ == '__main__':
    main()