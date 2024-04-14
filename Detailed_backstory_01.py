from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

llm = 'llama2'
#llm='openhermes'
#llm='mistral'
ollama_llm = Ollama(model=llm)
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
    role='Technical Writer',
    goal='write directions for assembly',
    backstory="""Technical writing is a specialized form of communication designed to convey complex information to specific audiences in a clear, concise, and accessible manner. The primary task of technical writing is to simplify the complicated, making technical or specialized knowledge understandable and usable for the intended audience. This can involve a range of activities and responsibilities""",
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm,
    )

# Tasks
task1 = Task(
    description=("Investigate."),
    expected_output='3 paragraphs-long report.',
    agent=researcher,
    )
task2 = Task(
    description=('Report'),
    expected_output="""
1. **Documentation Creation**: Developing various types of documents such as manuals, user guides, installation instructions, and help files. These documents provide step-by-step instructions on how to use products or perform specific tasks.

2. **Information Design**: Organizing and structuring information in a way that makes it easy for users to find, understand, and apply. This involves careful consideration of layout, visual elements, and navigational cues.

3. **Research and Analysis**: Gathering detailed information from subject matter experts, existing documentation, and other relevant sources to ensure accuracy and completeness. This often involves understanding complex technical processes and terminology.

4. **Writing and Editing**: Crafting clear and precise text that adheres to specific style guidelines and technical standards. Technical writers must be meticulous in their use of language to avoid ambiguities and ensure clarity.

5. **Content Management**: Maintaining consistency and accuracy across all documentation for a product or service. This might include updating documents to reflect product updates or new regulations.

6. **Audience Analysis**: Understanding the needs, capabilities, and expectations of the target audience to tailor content appropriately. This is crucial for ensuring that the documentation is useful and accessible to its intended users.

7. **Usability Testing**: Sometimes, technical writers are involved in testing the usability of the documents they create, gathering feedback from actual users, and making adjustments to improve clarity and usefulness.

8. **Collaboration**: Working closely with engineers, product managers, developers, and other stakeholders to ensure that documentation meets technical requirements and aligns with business goals.

9. **Quality Assurance**: Reviewing and revising content to ensure it meets high standards of quality and accuracy, often adhering to legal or regulatory requirements.
""",
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