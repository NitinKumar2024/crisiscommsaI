from google.adk.agents import SequentialAgent
from monitor_agent.agent import monitor_agent
from verifier_agent.agent import verifier_agent
from writer_agent.agent import writer_agent


# 2. Create the Workflow
# We use SequentialAgent because the output of one steps leads to the next
# Monitor -> Verifier -> Writer
root_agent = SequentialAgent(
    name="CrisisWorkflow",
    sub_agents=[monitor_agent, verifier_agent, writer_agent]
)

