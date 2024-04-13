from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

llm = 'llama2'
#llm='openhermes'
#llm='mistral'
ollama_llm = Ollama(model=llm)
topic = input("Topic?")
print(topic)

researcher = Agent(
    role=f"{topic} Researcher",
    goal=f'Research {topic}.',
    backstory=f'world-famous {topic} researcher',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm,
    )

writer = Agent(
    role='Writer',
    goal='write',
    backstory='world-famous writer',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm,
    )

task1 = Task(
    description=("Investigate."),
    expected_output='3 paragraphs long report.',
    agent=researcher,
    )
task2 = Task(
    description=('Write'),
    expected_output='3 paragraphs long report.',
    agent=writer,
    )

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1,task2],
    verbose=2,
    process=Process.sequential
    )

result=crew.kickoff()
print('#########################################')
print(result)
