import streamlit as st
import xml.etree.ElementTree as ET
from io import BytesIO

# Page title
st.title("Financial Data Form")
st.write("Fill in the financial data below and download the form as an XML file.")

# Create the form
with st.form("financial_form"):
    st.header("Financial Data Input")
    
    # Basic financial information
    company_name = st.text_input("Company Name")
    fiscal_year = st.text_input("Fiscal Year")
    report_date = st.date_input("Report Date")
    
    # Financial metrics
    revenue = st.number_input("Revenue (in millions)", value=0.0, step=0.01)
    expenses = st.number_input("Expenses (in millions)", value=0.0, step=0.01)
    profit = st.number_input("Profit (in millions)", value=0.0, step=0.01)
    liabilities = st.number_input("Liabilities (in millions)", value=0.0, step=0.01)
    assets = st.number_input("Assets (in millions)", value=0.0, step=0.01)
    
    # Submit button
    submitted = st.form_submit_button("Submit")

# If the form is submitted, generate the XML
if submitted:
    with st.spinner("Generating XML file..."):
        # Create XML structure
        root = ET.Element("FinancialData")
        ET.SubElement(root, "CompanyName").text = company_name
        ET.SubElement(root, "FiscalYear").text = fiscal_year
        ET.SubElement(root, "ReportDate").text = report_date.isoformat() if report_date else None
        ET.SubElement(root, "Revenue").text = str(revenue)
        ET.SubElement(root, "Expenses").text = str(expenses)
        ET.SubElement(root, "Profit").text = str(profit)
        ET.SubElement(root, "Liabilities").text = str(liabilities)
        ET.SubElement(root, "Assets").text = str(assets)

        # Convert XML tree to a downloadable file
        xml_bytes = BytesIO()
        tree = ET.ElementTree(root)
        tree.write(xml_bytes, encoding="utf-8", xml_declaration=True)
        xml_bytes.seek(0)

        st.success("Form submitted successfully!")
        st.download_button(
            label="Download XML File",
            data=xml_bytes,
            file_name="financial_data.xml",
            mime="application/xml",
        )
