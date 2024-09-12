from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

def call_llm(message, apibase, model, key, historique, context):
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
    response = chain.invoke(
        {
            "historique": historique,
            "message": message,
        }
    )
    return response
