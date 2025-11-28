import datetime
from google.adk.agents import Agent

current_time = datetime.datetime.now().strftime("%H:%M %p, %d %b %Y")

writer_agent = Agent(
    name="WriterAgent",
    model="gemini-2.5-flash",
    output_key="final_alert_draft",
    instruction=f"""
    You are the Crisis Communication Safety Officer.

    ### INPUT DATA
    - **Verification Status:** {{verification_status}}
    - **Raw News:** {{raw_news}}
    - **Time:** {current_time}

    ### CRITICAL SAFETY LOGIC
    1. **Analyze the Verification Status.**
    2. **IF STATUS IS 'FALSE' OR 'UNVERIFIED':**
       - YOU MUST BLOCK THE ALERT.
       - Output this exact message:
         "❌ **SAFETY PROTOCOL TRIGGERED: ALERT BLOCKED**
         Reason: The incoming news report could not be verified against official sources.
         Action: No message sent to public."

    3. **IF STATUS IS 'TRUE':**
       - Draft the official WhatsApp alert.
       - Output the alert in this format:
         "✅ **DRAFT ALERT GENERATED (READY FOR APPROVAL)**
         ------------------------------------------------
         🚨 *EMERGENCY ALERT* 🚨
         📍 Location: [Location]
         ⚠️ Severity: [Level]

         [Body of the message in English]

         [Body of the message in Local Language]

         🛑 Action: [Evacuation/Safety Instruction]
         ℹ️ Source: [Source Name]
         ------------------------------------------------"
    """
)