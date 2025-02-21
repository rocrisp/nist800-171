import pandas as pd
import os
import csv
from datetime import datetime

COMPLIANCE_FILE = 'CSGNIST800171Compliance.csv'
OUTPUT_FILE = 'compliance_report.csv'

class ComplianceTool:
    def __init__(self, compliance_file: str):
        self.compliance_file = compliance_file
        self.data = self.load_compliance_data()

    def load_compliance_data(self) -> pd.DataFrame:
        """Load compliance data from the CSV file."""
        try:
            df = pd.read_csv(self.compliance_file)
            df.columns = df.columns.str.strip()  # Strip whitespace from column names
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
            return df
        except Exception as e:
            print(f"Error loading compliance data: {e}")
            return pd.DataFrame()

    def display_requirements(self):
        """Display all compliance requirements with their status."""
        for index, row in self.data.iterrows():
            print(f"{index+1}. [{row['Status']}] {row['Identifier']} - {row['Security Requirement']} - {row['Discussion']}")

    def update_status(self, index: int, status: str, evidence: str = ''):
        """Update the compliance status of a specific control."""
        if 0 <= index < len(self.data):
            self.data.at[index, 'Status'] = status
            self.data.at[index, 'Evidence'] = evidence
        else:
            print("Invalid index. Please try again.")

    def generate_report(self):
        """Generate a CSV report of the compliance status."""
        try:
            self.data.to_csv(OUTPUT_FILE, index=False)
            print(f"Compliance report generated: {OUTPUT_FILE}")
        except Exception as e:
            print(f"Error generating report: {e}")

if __name__ == '__main__':
    tool = ComplianceTool(COMPLIANCE_FILE)
    while True:
        print("\nNIST 800-171 Compliance Tool")
        print("1. Display all requirements")
        print("2. Update compliance status")
        print("3. Generate compliance report")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            tool.display_requirements()
        elif choice == '2':
            try:
                index = int(input("Enter requirement index: ")) - 1
                status = input("Enter status (Compliant, Non-Compliant, Not Applicable): ")
                evidence = input("Enter evidence (optional): ")
                tool.update_status(index, status, evidence)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            tool.generate_report()
        elif choice == '4':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please try again.")
