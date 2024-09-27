##### What is LLM ?

##### LLM VS Generative AI 

##### What is Langchain ?

##### LLMs and Chat Models

| **Characteristics** | **Large Language Models (LLMs)** | **Chat Models** |
| --- | --- | --- |
| **Purpose** | Versatile models for various language tasks | Specialized models for conversational use |
| **Examples of Tasks** | Translation, Summarization, Question Answering, Content Creation | Chatbots, Virtual Assistants, Customer Support Systems |
| **How they Work** | Pre-trained on large data, fine-tuned for specific tasks | Often backed by LLMs, tuned for conversational responses |
| **Input and Output** | Perform various tasks | Take chat messages as input, return AI message as output |

#### [Chat Model Messages](https://python.langchain.com/v0.1/docs/modules/model_io/chat/)
- Message Structure
  - Role: Describes who is saying the message (e.g., human, AI, system)
  - Content: Describes the message content (string, list of dictionaries)
  - Additional_kwargs: Additional information about the message (provider-specific)

- Message Types
  - HumanMessage: User-generated message
  - AIMessage: Model-generated message (may include additional_kwargs)
  - SystemMessage: System-generated message (tells model how to behave)
  - FunctionMessage: Result of a function call (includes function name)
  - ToolMessage: Result of a tool call (includes tool call ID)

```python
from langchain import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    FunctionMessage,
    ToolMessage
)


# HumanMessage example
human_msg = HumanMessage(content="Hello, how are you?")
print(human_msg)


# AIMessage example
ai_msg = AIMessage(content="I'm doing well, thanks!", additional_kwargs={"tool_calls": ["search"]})
print(ai_msg)


# SystemMessage example
system_msg = SystemMessage(content="You are a programmer")
print(system_msg)


# FunctionMessage example
func_msg = FunctionMessage(content="Result: 42", name="calculate_answer")
print(func_msg)


# ToolMessage example
tool_msg = ToolMessage(content="Search results:", tool_call_id="search_123")
print(tool_msg)
```

#### [Prompt Template in LangChain](https://python.langchain.com/v0.1/docs/modules/model_io/prompts/quick_start/)

Prompt templates are pre-designed formats that help you ask questions or provide tasks to language models. They ensure you get accurate and relevant responses.

1. PromptTemplate
Base class for all prompt templates. Defines the structure for generating prompts.

There are 2 way to create prompt:
```python
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
prompt_template.format(adjective="funny", content="chickens")
```
Using template parameters
```python
from langchain import PromptTemplate

# Define template string
template = "Answer the following {question} with a detailed explanation."

# Define input variables
input_variables = ["question"]

# Create PromptTemplate
prompt_template = PromptTemplate(
    template=template,
    input_variables=input_variables
)
```

2. ChatPromptTemplate
Template for chat-based prompts. Includes conversation history and context.
```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)

messages = chat_template.format_messages(name="Bob", user_input="What is your name?")
```
3. ChatMessagePromptTemplate
Specific template for chat messages. Formats messages for language models.

```python
from langchain import ChatMessagePromptTemplate

template = ChatMessagePromptTemplate(
    template="{role}: {content}.",
    role="Assistant"
)

prompt = template.format(content="I'm here to help!")
print(prompt)
# Output: Assistant: I'm here to help!
```

4. Message Prompt Templates
LangChain offers various MessagePromptTemplate types to create specific message prompts:
Common Types
- AIMessagePromptTemplate: Creates AI-generated messages.
- SystemMessagePromptTemplate: Creates system-generated messages.
- HumanMessagePromptTemplate: Creates human-generated messages.



5. MessagesPlaceholder
MessagesPlaceholder gives you control over messages rendered during formatting.
- Benefits :
  - Flexibility: Uncertain role? Insert messages dynamically.
  - Customization: Insert lists of messages during formatting.
- Use Cases
  - Dynamic message insertion
  - Role uncertainty
  - Custom message lists

```python
template = PromptTemplate(template="...", messages_placeholder=MessagesPlaceholder())
prompt = template.format(messages=[message1, message2])
```

##### Where to use format ,format_messages & from_template

1. `format()` 
 Usage: Replace placeholders in the template with specific values.

```python
template = AIMessagePromptTemplate(
    template="Translate '{content}' from English to Spanish."
)
prompt = template.format(content="Hello, how are you?")
```
2. `format_messages()`
Usage: Replace placeholders with multiple messages.

```python
template = ChatMessagePromptTemplate(
    template="{role}: {content}"
)
messages = [
    {"role": "User", "content": "Hello"},
    {"role": "AI", "content": "Hi!"}
]
prompt = template.format_messages(messages)
```
3. `from_template()`
Usage: Create a new template from an existing one.

```python
base_template = AIMessagePromptTemplate(
    template="Translate '{content}' from English to Spanish."
)
new_template = AIMessagePromptTemplate.from_template(
    base_template, template="Translate '{content}' from Spanish to French."
)
```

#### [Few-shot prompt](https://python.langchain.com/v0.1/docs/modules/model_io/prompts/few_shot_examples/)
A few-shot prompt is a type of prompt that provides a limited number of examples (typically 2-5) of the desired output, along with a clear instruction or task. This approach enables language models to understand the context and generate high-quality responses.
```
**Task:** Write a short story about a character who discovers a hidden world.

**Examples:**

1. Alice fell down the rabbit hole and found Wonderland.
2. Dorothy Gale discovered Oz after a tornado.

**Your turn:** Write a similar story about a character named Max.
```
```python

example_prompt = PromptTemplate(
    input_variables=["task", "examples"],
    template="{examples}\nTask: {task}\n",
)

from langchain_core.prompts.few_shot import FewShotPromptTemplate

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

prompt.format(input="Write a humorous poem about a Toast.")
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/ldBsvhjEREc?si=0U_BXnkMPg1cNXBU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


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


<!-- PromptTemplate and ChatPromptTemplate implement the Runnable interface, the basic building block of the LangChain Expression Language (LCEL). This means they support invoke, ainvoke, stream, astream, batch, abatch, astream_log calls. -->