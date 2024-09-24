<iframe width="560" height="315" src="https://www.youtube.com/embed/ldBsvhjEREc?si=0U_BXnkMPg1cNXBU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Langchain
<img src="./media/langchain1.png">
<img src="./media/langchain1.1.png">

[Documentation](https://js.langchain.com/v0.2/docs/concepts/#langsmith)

## Langgraph

<img src="./media/langgraph.png">

## Data collection and preprocessing
- Gather relevant datasets for training (e.g., text, images).
- Preprocess data:
  - Text: tokenization, stopword removal, stemming/lemmatization, embedding.
  - Images: resizing, normalization.

## RAG chain components

1. Retriever: The Librarian
Imagine a librarian who searches for relevant books (information) in a vast library (external knowledge sources). The retriever's job is to:
Find relevant information related to the user's question.
Fetch this information from various sources (e.g., PDF documents, databases).
Provide this information to the next step in the chain.
2. Ranker: The Filter
The ranker acts like a filter, sorting the retrieved information by relevance:
Determines which pieces of information are most useful.
Ranks them in order of importance.
Ensures the most relevant information is used to answer the user's question.
3. Generator: The Answer Writer
The generator takes the ranked information and writes a clear, concise answer:
Uses the retrieved and ranked information to generate a response.
Ensures the answer is relevant, accurate, and easy to understand.
Provides the final answer to the user.
4. History Awareness: The Memory Keeper
History awareness keeps track of the conversation history:
Remembers previous questions and answers.
Understands the context of the conversation.
Helps the retriever and generator provide more accurate and relevant responses.
Think of it like a conversation with a friend:
Retriever: "Hey, I found some info about that!"
Ranker: "Let me sort it out and prioritize the important stuff."
Generator: "Here's the answer!"
History Awareness: "Remember, we were just talking about this related topic."
Together, these components work together to provide accurate, informative, and contextually relevant responses!

## Tools & Agents
Tools are interfaces that an agent, chain, or LLM can use to interact with the world.

In LangChain, *tools* are pre-built components that simplify building AI-powered language applications. 

Think of them as a toolbox for:
- Text processing
- Language understanding
- Response generation
- Conversation management
Examples of tools include:
- Text classification
- Sentiment analysis
- Translation
- Summarization
- These tools make development easier and faster.

In LangChain, an *agent* is a program that:
- Interacts with language models
- Performs specific tasks
- Uses LangChain tools
Types of agents:
- LLaMA Agent (conversational, text generation)
- Plugin Agent (integrates external services/APIs)

Think of an agent as a virtual assistant that automates tasks and enhances language model capabilities.

### Text summarization
- If content fits in llm context window we can pass it directly to llm.
- If content doesn't fits in llm context window we can apply these two common approaches for this are:

    - `Stuff`: Simply "stuff" all your documents into a single prompt. This is the simplest approach .

    - `Map-reduce` (Larger file): Summarize each document on its own in a "map" step and then "reduce" the summaries into a final summary.
        * Single prompt template
        * Multi prompt template
    - `Refine`
    
<img src="./media/summarization.png">

[Documentation](https://python.langchain.com/docs/tutorials/summarization/#concepts)
