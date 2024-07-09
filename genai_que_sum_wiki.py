import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAI
#from langchain import LLMChain
from langchain.agents import AgentType, initialize_agent, load_tools
import streamlit as slit
from langchain.prompts.prompt import PromptTemplate

def personality():
    load_dotenv()
    tab1, tab2, tab3 = slit.tabs(["Know your president", "Summarize the Meeting","Wiki"])

    print("first genai test and its token")

    with tab1:
        content = """
                     Frame 3 questions based upon the ${information}. 
                     Each question should have 4 options with 2 options in each line in tabular format and put the answer in the next line. 
                     Question should be of medium difficulty. 
            """
        information = slit.sidebar.text_area("Put the details here","")
        questionTemplate = PromptTemplate(input_variables=["information"],template=content)
        llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
        #chain = LLMChain(llm=llm,prompt=template)
        chain = questionTemplate | llm
        res = chain.invoke(input={"information": information})
        slit.write(res.content)

    with tab2:
        summary = """provide summary of a person with this {information}:
                     1. name
                     2. BirthPlace
                     3. Family details
                     4. Area of work
                     5. Summary
                     6. Is he alcoholic?
                   """

        summaryTemplate = PromptTemplate(input_variables=["information"],template=summary)
        llm = ChatOpenAI(temperature=1,model_name="gpt-3.5-turbo")
        chain = summaryTemplate | llm
        res = chain.invoke(input={"information": information})
        slit.write(res.content)

    with tab3:
        llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")
        tools = load_tools(["wikipedia"],llm=llm)
        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
        res = agent.run("summarize about Donald Trump in 10 bullet points ")
        slit.write(res)



if __name__ == "__main__":
    personality()
