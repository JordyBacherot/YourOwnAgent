from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import ollama

def call_llm(message, apibase, model, historique, context, key=None):
    llm = None
    match apibase :
        case "openai":
            llm = ChatOpenAI(
                model=model,
                api_key=key,
                temperature=0.2,
            )
        case "groq":
            llm = ChatGroq(
                model=model,
                api_key=key,
                temperature=0.2,
            )
        case "ollama":
            llm = ChatOllama(
                model=model,
                temperature=0.2,
            )


    template = """
    Conversation précédente:
    {historique}
    
    Nouveau message humain : 
    {message}
    """

    promptTemplate = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                context,
            ),
            ("human", template),
        ]
    )

    chain = promptTemplate | llm | StrOutputParser()
    try :
        response = chain.invoke(
            {
                "historique": historique,
                "message": message,
            }
        )
    except Exception as error:
        print(error)
        if "try pulling it first" in str(error):
            response = "The model you are trying is not downloaded, start of the download"
        else :
            response = "An error occured in the call of the LLM"
    return response

def download_model_ollama(model):
    ollama.pull(model)


