# TinyTroupe-Launcher
TinyTroupe Launcher 是一个为 TinyTroupe Python 库提供的简化启动工具。通过这个启动器，用户可以轻松创建和配置自定义的 AI Agent 和模拟环境，并快速启动和运行模拟。无需复杂的设置，只需修改小人（Agent）和环境（Environment）的描述，即可启动模拟。  
TinyTroupe Launcher is a simplified startup tool for the TinyTroupe Python library. With this launcher, users can easily create and configure custom AI agents and simulation environments, and quickly start and run simulations. No complex setup is required—users simply need to modify the descriptions of the agents and the environment to initiate the simulation.  

## 功能特点
简化的 Agent 和环境创建：用户只需提供简单的描述即可创建自定义的 AI Agent 和模拟环境。
快速启动模拟：用户修改描述后，可以立即启动模拟，体验不同的场景和 Agent 行为。
无缝与 TinyTroupe 集成：直接基于 TinyTroupe 库，无需额外配置，简化了使用流程。

TinyTroupe 使用 OpenAI API 进行模型推理，用户需要设置自己的 API 密钥。为了简化配置，按照以下步骤操作：
将 `launcher.py` 文件放置在 `TinyTroupe` 库的根目录下，  
然后更改`tinytroupe/openai_utils.py`下132行（如下）  
TinyTroupe uses the OpenAI API for model inference, and users need to set their own API key. To simplify the configuration, follow these steps:
Place the launcher.py file in the root directory of the TinyTroupe library,
then modify line 132 in tinytroupe/openai_utils.py (as shown below):  
![image](https://github.com/user-attachments/assets/d86dceb9-5fa6-4b67-92c4-18f324abf573)  

`api_key=os.getenv("OPENAI_API_KEY")`改为`api_key="xxxx"`，  
其中`xxxx`是你的api-key。
或者将API-Key加入环境变量中。  
Change api_key=os.getenv("OPENAI_API_KEY") to api_key="xxxx",
where xxxx is your API key.
Alternatively, you can add the API key to your environment variables.  

## 你需要修改的部分 | Parts You Need to Modify
### Line 52-105:
```
# 创建多个小人（Agents），每个小人具备不同的技能、兴趣、角色、任务和描述等信息。
# 这些小人相当于你招聘的员工。你可以根据需求为每个小人填写详细的属性信息，
# 格式请参考下面示例，每个小人的定义应包括姓名、技能、兴趣、角色、任务以及描述等。
# Create multiple agents, each with different skills, interests, roles, tasks, and descriptions.
# These agents are like employees you hire. You can fill in the detailed attributes for each agent based on your needs.
# Please refer to the example below for the format. Each agent's definition should include name, skills, interests, role, tasks, and description.
```
### Line 108-111:
```
# 在此广播你希望小人们讨论的内容。例如，你可以设置团队讨论开发一个创新的 AI 聊天机器人，
# 并考虑如何让它在市场中脱颖而出，包括新功能、用户体验、技术应用等方面。
# Broadcast the topic you want the agents to discuss. For example, you can set the team to discuss developing an innovative AI chatbot,
# and consider how to make it stand out in the market, including new features, user experience, technological applications, and more.
world.broadcast(
    """
    Team, let's discuss developing an innovative AI chatbot with unique features to stand out in the market.
    Think about new features, enhancing user experience, integrating emerging technologies, and balancing innovation with practicality.
    """
)
```
### Line 113:
```
# 设置讨论的轮次。这里我们设置进行 2 轮讨论，调整数字可以控制讨论的轮数。
# Set the number of discussion rounds. Here, we set it to 2 rounds of discussion. Adjust the number to control the number of rounds.
world.run(2)
```
### Line 116-118:
```
# 设置报告员来总结讨论结果。这里指定为 Agent Alex，总结内容包括创新的功能、技术建议、UX 改进等。
# Set the rapporteur to summarize the discussion results. Here, we specify Agent Alex to summarize the outcomes, including innovative features, technical suggestions, UX improvements, and more.
rapporteur = world.get_agent_by_name("Alex")
rapporteur.listen_and_act(
    """
    Summarize the main outcomes: innovative features, technical suggestions, UX improvements, challenges, and solutions.
    """
)
```
### Line 128:
```
# 在此指定从讨论中提取的目标信息。你可以根据需要选择提取讨论的所有内容，或仅提取特定的信息。
# 例如，在此我们提取 AI 聊天机器人的创新功能及其技术可行性与市场影响。
# Specify the information to be extracted from the discussion. You can choose to extract all the discussion content or only specific information as needed.
# For example, here we extract innovative features of the AI chatbot along with its technical feasibility and market impact.  

    results = extractor.extract_results_from_agent(
        rapporteur,
        # 这里写你想要提取的信息，如何总结等等，你也可以让ta全部提取出来
        extraction_objective="Summarize ideas for innovative AI chatbot features with technical feasibility and market impact.",
        situation="AI Chatbot Innovation Discussion",
    )
```
