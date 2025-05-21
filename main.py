
import streamlit as st
import matplotlib.pyplot as plt
from fpdf import FPDF

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# Title
st.title("Carbon Emissions Tracker")
st.subheader("Estimate your carbon footprint from daily activities")

# Activity input
activity = st.selectbox("Choose an activity:", ["Driving", "Flying", "Electricity Use"])
value = st.number_input("Enter distance (km) or energy used (kWh):", min_value=0.0)

# Emission factors
factors = {
    "Driving": 0.21,
    "Flying": 0.25,
    "Electricity Use": 0.233
}

# Calculate emissions
if st.button("Add to Report"):
    emissions = value * factors[activity]
    st.session_state.history.append((activity, value, emissions))
    st.success(f"Added: {emissions:.2f} kg CO₂ for {value} units of {activity}")

# Show history and total
if st.session_state.history:
    st.subheader("Emission Breakdown")
    total = 0
    breakdown = {}
    for act, val, emis in st.session_state.history:
        total += emis
        breakdown[act] = breakdown.get(act, 0) + emis

    # Show pie chart
    fig, ax = plt.subplots()
    ax.pie(breakdown.values(), labels=breakdown.keys(), autopct='%1.1f%%')
    st.pyplot(fig)
    st.write(f"**Total emissions:** {total:.2f} kg CO₂")

    # Export to PDF
    if st.button("Download PDF Report"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Carbon Emissions Report", ln=True, align='C')
        pdf.ln(10)

        for act, val, emis in st.session_state.history:
            pdf.cell(200, 10, txt=f"{act}: {val} units → {emis:.2f} kg CO₂", ln=True)

        pdf.cell(200, 10, txt=f"Total Emissions: {total:.2f} kg CO₂", ln=True)

        # Save and download
        pdf.output("carbon_emissions_report.pdf")
        with open("carbon_emissions_report.pdf", "rb") as file:
            st.download_button(
                label="Click to Download Report",
                data=file,
                file_name="carbon_emissions_report.pdf",
                mime="application/pdf"
            )
