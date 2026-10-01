import streamlit as st
import time
from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.set_page_config(
    page_title="AI Business Research Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Business Research & Competitive Intelligence Agent")
st.caption("Agentic AI system for evidence-based business research and decision support")

question = st.text_area(
    "🔍 Enter your strategic business question",
    placeholder="Example: Should our company expand into the electric scooter market?",
    height=100
)

if st.button("🚀 Start Research", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a business question.")

    else:
        st.success("Research process started!")

        st.subheader("🤖 Agent Workflow")

        agents = [
            ("🔎", "Research Planner",
             "Breaking the business question into research tasks"),

            ("🌐", "Source Discovery",
             "Finding relevant information sources"),

            ("📄", "Evidence Extraction",
             "Extracting important claims from sources"),

            ("✅", "Verification",
             "Checking evidence and source reliability"),

            ("⚖️", "Comparison",
             "Comparing evidence from different sources"),

            ("⚠️", "Contradiction Detection",
             "Identifying conflicting information"),

            ("🧠", "Synthesis",
             "Combining verified evidence"),

            ("📊", "Executive Agent",
             "Preparing the final decision brief")
        ]

        progress = st.progress(0)

        for i, (icon, name, description) in enumerate(agents):

            with st.container(border=True):
                st.write(f"{icon} **{name}**")
                st.caption(description)

            progress.progress((i + 1) / len(agents))
            time.sleep(0.15)

        st.success("✅ Research pipeline completed")

        st.divider()

        st.header("📚 Research Evidence")

        st.info(
            "Demo evidence is used for this prototype. "
            "It is simulated data for demonstrating the agent workflow."
        )

        sources = [
            {
                "name": "📄 Market Research Report",
                "type": "Demo Source",
                "evidence": "Electric mobility can create opportunities for businesses, "
                            "but infrastructure availability should be evaluated."
            },
            {
                "name": "🏢 Industry Report",
                "type": "Demo Source",
                "evidence": "Lower operating costs can be a potential advantage "
                            "for electric mobility solutions."
            },
            {
                "name": "📊 Customer Survey",
                "type": "Demo Source",
                "evidence": "Some potential customers may be concerned about "
                            "charging availability and vehicle range."
            }
        ]

        for source in sources:

            with st.container(border=True):
                st.subheader(source["name"])
                st.caption(source["type"])
                st.write(source["evidence"])

        st.divider()

        st.header("📊 Executive Decision Brief")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Verified Facts")

            st.write(
                "• The research system separates evidence from conclusions."
            )

            st.write(
                "• Multiple sources can be compared before synthesis."
            )

            st.write(
                "• Evidence is classified according to verification status."
            )

        with col2:

            st.subheader("⚠️ Conflicting Information")

            st.write(
                "• Industry evidence indicates potential operating-cost benefits."
            )

            st.write(
                "• Customer evidence highlights charging and range concerns."
            )

            st.write(
                "• These differences require additional verification."
            )

        st.subheader("🧠 Inferences")

        st.write(
            "The evidence suggests that market expansion could involve "
            "both opportunities and infrastructure-related risks. "
            "A detailed company-specific analysis would be required "
            "before making a final business decision."
        )

        st.subheader("❓ Unknown Information")

        st.write(
            "• Company-specific financial data is unavailable."
        )

        st.write(
            "• Competitor-specific pricing data is unavailable."
        )

        st.write(
            "• Real customer demand data is unavailable."
        )

        st.divider()

        st.subheader("📌 Research Question")

        st.write(question)

        st.caption(
            "Prototype: live external research can be connected through APIs."
        )
