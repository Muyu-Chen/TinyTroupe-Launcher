import json
from tinytroupe import *
from tinytroupe.environment import TinyWorld, TinySocialNetwork
from tinytroupe.agent import TinyPerson
from tinytroupe.extraction import ResultsExtractor


def create_team_member(name, role, morning_task, description, skills, interests):
    person = TinyPerson(name=name)

    # 初始化 interests 组
    if "interests" not in person._configuration:
        person._configuration["interests"] = []

    if "skills" not in person._configuration:
        person._configuration["skills"] = []

    if "role" not in person._configuration:
        person._configuration["role"] = []
    
    if "morning_task" not in person._configuration:
        person._configuration["morning_task"] = []
    
    if "description" not in person._configuration:
        person._configuration["description"] = []
    
    person.define_several(
        group="skills",
        records=skills,
    )
    person.define_several(
        group="interests",
        records=interests,
    )
    person.define_several(
        group="role",
        records=role,
    )
    person.define_several(
        group="morning_task",
        records=morning_task,
    )
    person.define_several(
        group="description",
        records=description,
    )

    return person


def main():
    # 这里创建了很多小人，他们有不同的技能，兴趣，角色，早上的任务，描述等等
    # 相当于你招聘的员工，你把你想要招聘的员工的信息写上去，格式按照8行的格式写
    world = TinyWorld(
        "AI Chatbot Team",
        [
            create_team_member(
                "Ethan",
                "Full Stack Developer",
                "Morning: System monitoring and backend work.",
                "Focuses on backend architecture, system optimization, and API integration.",
                ["Python, Java, Node.js", "Microservices", "Docker, Kubernetes"],
                ["AI system integration", "Tech performance optimization"],
            ),
            create_team_member(
                "Samantha",
                "Product Manager",
                "Morning: Review feedback and prioritize tasks.",
                "Defines features, prioritizes tasks, and manages product roadmap.",
                ["Agile methodology", "Market research", "KPI analysis"],
                ["User experience", "Customer feedback"],
            ),
            create_team_member(
                "Tina",
                "UX Designer",
                "Morning: Sketch design ideas and review feedback.",
                "Creates intuitive user interfaces for chatbots, ensuring smooth interactions.",
                ["Figma, Sketch", "User testing", "UI design"],
                ["Photography", "Piano"],
            ),
            create_team_member(
                "Alex",
                "Engineering Manager",
                "Morning: Planning meetings, afternoons supporting the team.",
                "Guides development, balances tech debt and new features, manages team growth.",
                ["Agile development", "Project management", "Tech strategy"],
                ["Team leadership", "Long-term planning"],
            ),
            create_team_member(
                "Liam",
                "Frontend Developer",
                "Morning: Review designs and implement UI components.",
                "Converts designs into interfaces, ensuring performance and responsiveness.",
                ["HTML, CSS, JavaScript", "React, Vue.js", "UI performance"],
                ["Frontend animations", "Responsive design"],
            ),
            create_team_member(
                "Max",
                "Data Analyst",
                "Morning: Analyze user data, afternoon: create reports.",
                "Analyzes chatbot usage data to improve features, monitors KPIs.",
                ["Python (Pandas, NumPy)", "SQL", "A/B testing"],
                ["User behavior analysis", "Data visualization"],
            ),
        ],
    )

    # 这里写你需要他们做什么事情？
    world.broadcast(
        """
        Team, let's discuss developing an innovative AI chatbot with unique features to stand out in the market.
        Consider adding features, improving user experience, applying new technologies, and balancing innovation with practicality.
    """
    )

    # 这里是你需要讨论几轮，这里是讨论2轮
    world.run(2)

    # 这里是你需要谁来总结这次讨论的结果，这里是Alex，以及你需要ta总结什么
    rapporteur = world.get_agent_by_name("Alex")
    rapporteur.listen_and_act(
        """
        Summarize the main outcomes: innovative features, tech suggestions, UX improvements, challenges, and solutions.
    """
    )

    extractor = ResultsExtractor()
    results = extractor.extract_results_from_agent(
        rapporteur,
        # 这里写你想要提取的信息，如何总结等等，你也可以让ta全部提取出来
        extraction_objective="Summarize ideas for innovative AI chatbot features with technical feasibility and market impact.",
        situation="AI Chatbot Innovation Discussion",
    )

    print("\n====== AI Chatbot Innovation Summary ======\n")
    print(results)


if __name__ == "__main__":
    main()
