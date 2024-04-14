from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama


###  Researched with Mistral, written with llama2
llm = 'llama2'
#llm='openhermes'
llm2='mistral'
ollama_llm = Ollama(model=llm)
ollama_llm2 = Ollama(model=llm2)
topic = input("Topic?")
print(topic)
# Agents
researcher = Agent(
    role=f"{topic} Researcher",
    goal=f'Research {topic}.',
    backstory=f'You are a world-famous {topic} researcher.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm,
    )

writer = Agent(
    role='Writer',
    goal='write',
    backstory='You are a world-famous writer.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm2,
    )

# Tasks
task1 = Task(
    description=("Investigate."),
    expected_output='3 paragraphs-long report.',
    agent=researcher,
    )
task2 = Task(
    description=('Report'),
    expected_output='Write a 3 paragraphs-long report.',
    agent=writer,
    )

# Your Crew
crew = Crew(
    agents=[researcher, writer], #Add agents as required
    tasks=[task1,task2], #Add tasks as required
    verbose=2,
    process=Process.sequential
    )

result=crew.kickoff()
print('#########################################')
print(result)