import streamlit as st
import time

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
            ("🔎", "Research Planner", "Breaking the business question into research tasks"),
            ("🌐", "Source Discovery", "Finding relevant evidence sources"),
            ("📄", "Evidence Extraction", "Extracting important claims and information"),
            ("✅", "Verification", "Checking evidence and source reliability"),
            ("⚖️", "Comparison", "Comparing different pieces of information"),
            ("⚠️", "Contradiction Detection", "Identifying conflicting information"),
            ("🧠", "Synthesis", "Combining verified evidence"),
            ("📊", "Executive Agent", "Preparing the final decision brief")
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

        st.header("📊 Executive Decision Brief")

        st.info(
            "This prototype demonstrates how an Agentic AI research pipeline "
            "organizes evidence before preparing an executive brief."
        )

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Verified Facts")

            st.write(
                "• The system separates research evidence from final conclusions."
            )
            st.write(
                "• Multiple sources can be compared before synthesis."
            )
            st.write(
                "• Evidence can be classified according to verification status."
            )

        with col2:
            st.subheader("⚠️ Conflicting Information")

            st.write(
                "• Different sources may report different market conditions."
            )
            st.write(
                "• Conflicting claims should be highlighted instead of hidden."
            )
            st.write(
                "• Additional verification may be required before a decision."
            )

        st.subheader("🧠 Inferences")

        st.write(
            "Based on the available evidence, the research agent can identify "
            "potential opportunities, risks and areas requiring further investigation."
        )

        st.subheader("❓ Unknown Information")

        st.write(
            "• Current company-specific financial data is not available."
        )
        st.write(
            "• Customer-level research data is not available."
        )
        st.write(
            "• Additional real-world sources would be required for a final business decision."
        )

        st.divider()

        st.subheader("📌 Research Question")

        st.write(question)

        st.caption(
            "Demo prototype — real-time external research can be connected through APIs."
        )
