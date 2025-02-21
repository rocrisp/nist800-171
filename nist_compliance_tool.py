import pandas as pd
import os
import csv
import logging
from fpdf import FPDF
from datetime import datetime

COMPLIANCE_FILE = 'CSGNIST800171Compliance.csv'
OUTPUT_CSV = 'compliance_report.csv'
OUTPUT_PDF = 'compliance_report.pdf'
BACKUP_DIR = 'backups'
LOG_FILE = 'compliance_tool.log'

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ComplianceTool:
    def __init__(self, compliance_file: str):
        self.compliance_file = compliance_file
        self.data = self.load_compliance_data()

    def load_compliance_data(self) -> pd.DataFrame:
        """Load compliance data from the CSV file."""
        try:
            df = pd.read_csv(self.compliance_file)
            df.columns = df.columns.str.strip()
            df = df[['Control Family', 'Control Type', 'NIST 800-171 Control Number', 'Control Text', 'DFARS 7012 (2013) Covered']]
            df = df.rename(columns={
                'Control Family': 'Family',
                'Control Type': 'Basic/Derived Security Requirement',
                'NIST 800-171 Control Number': 'Identifier',
                'Control Text': 'Security Requirement',
                'DFARS 7012 (2013) Covered': 'Discussion'
            })
            df['Status'] = 'Not Evaluated'
            df['Evidence'] = ''
            logging.info("Compliance data loaded successfully.")
            return df
        except Exception as e:
            logging.error(f"Error loading compliance data: {e}")
            return pd.DataFrame()

    def display_requirements(self):
        for index, row in self.data.iterrows():
            print(f"{index+1}. [{row['Status']}] {row['Identifier']} - {row['Security Requirement']}")

    def list_not_evaluated(self):
        """List all identifiers that have not had their compliance status updated."""
        not_evaluated = self.data[self.data['Status'] == 'Not Evaluated']
        if not_evaluated.empty:
            print("All requirements have been evaluated.")
        else:
            for index, row in not_evaluated.iterrows():
                print(f"{index+1}. [Not Evaluated] {row['Identifier']} - {row['Security Requirement']}")

    def search_requirements(self, search_term: str):
        search_results = self.data[self.data['Security Requirement'].str.contains(search_term, case=False, na=False)]
        for index, row in search_results.iterrows():
            print(f"{index+1}. [{row['Status']}] {row['Identifier']} - {row['Security Requirement']}")

    def update_status(self, index: int, status: str, evidence: str = ''):
        if 0 <= index < len(self.data):
            self.data.at[index, 'Status'] = status
            self.data.at[index, 'Evidence'] = evidence
            logging.info(f"Updated status for control {self.data.at[index, 'Identifier']} to {status}.")
        else:
            print("Invalid index. Please try again.")

    def generate_csv_report(self):
        try:
            self.data.to_csv(OUTPUT_CSV, index=False)
            logging.info("CSV report generated successfully.")
        except Exception as e:
            logging.error(f"Error generating CSV report: {e}")

    def generate_pdf_report(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(200, 10, txt='NIST 800-171 Compliance Report', ln=True, align='C')
        pdf.set_font('Arial', '', 10)
        for index, row in self.data.iterrows():
            pdf.cell(200, 10, txt=f"{index+1}. [{row['Status']}] {row['Identifier']} - {row['Security Requirement']}", ln=True)
        pdf.output(OUTPUT_PDF)
        logging.info("PDF report generated successfully.")

    def backup_data(self):
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        backup_file = os.path.join(BACKUP_DIR, f"compliance_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
        self.data.to_csv(backup_file, index=False)
        logging.info(f"Data backed up to {backup_file}")

if __name__ == '__main__':
    tool = ComplianceTool(COMPLIANCE_FILE)
    while True:
        print("\nNIST 800-171 Compliance Tool")
        print("1. Display all requirements")
        print("2. Search compliance requirements")
        print("3. List requirements not evaluated")
        print("4. Update compliance status")
        print("5. Generate compliance report (CSV & PDF)")
        print("6. Backup compliance data")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            tool.display_requirements()
        elif choice == '2':
            search_term = input("Enter search term: ")
            tool.search_requirements(search_term)
        elif choice == '3':
            tool.list_not_evaluated()
        elif choice == '4':
            try:
                index = int(input("Enter requirement index: ")) - 1
                status = input("Enter status (Compliant, Non-Compliant, Not Applicable): ")
                evidence = input("Enter evidence (optional): ")
                tool.update_status(index, status, evidence)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            tool.generate_csv_report()
            tool.generate_pdf_report()
        elif choice == '6':
            tool.backup_data()
        elif choice == '7':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please try again.")
