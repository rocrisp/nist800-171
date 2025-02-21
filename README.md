# NIST 800-171 Compliance Tool

This tool helps organizations manage their compliance with **NIST 800-171** requirements by providing a command-line interface to view, update, and generate reports on compliance status.

---

## 📂 **Core Features:**
1. **Display All Compliance Requirements:**  
   View all compliance requirements along with their status (**Compliant**, **Non-Compliant**, **Not Evaluated**).

2. **Search Compliance Requirements:**  
   Search for compliance requirements using **keywords**, **identifiers**, or **control families**.

3. **List Not Evaluated Requirements:**  
   Identify all compliance **identifiers** that have not been updated from the **"Not Evaluated"** status.

4. **Update Compliance Status:**  
   Update the status of compliance requirements to:
   - **Compliant**
   - **Non-Compliant**
   - **Not Applicable**  
   Provide **evidence** while updating the status.

5. **Generate Reports:**  
   Create compliance reports in:
   - **CSV format** (`compliance_report.csv`)
   - **PDF format** (`compliance_report.pdf`)  
   The report includes **status**, **evidence**, and **detailed requirements**.

6. **Automatic Backups:**  
   Automatically **backup compliance data** into the **backups** directory with **timestamped filenames**.

7. **Logging:**  
   All actions are **logged** to **compliance_tool.log**, including:
   - **Errors**
   - **Status updates**
   - **Report generation activities**

---

## 🛠️ **Prerequisites**
1. **Install Python 3.8+**

### **On Windows:**
- Download from the [official Python website](https://www.python.org/downloads/).
- Ensure **Add Python to PATH** is selected during installation.

### **On macOS:**
```sh
brew install python
```

### **On Linux:**
```sh
sudo apt update
sudo apt install python3 python3-pip
```

2. **Required Python packages:**
```sh
pip install pandas
pip install fpdf
```

3. **CSV File:** Place the **CSGNIST800171Compliance.csv** file in the **same directory** as the script.

---

## 🚀 **Setup Instructions**
1. **Clone the Repository:**
```sh
git clone <repository_url>
cd <repository_name>
```

2. **Install Dependencies:**
```sh
pip install pandas
```

3. **Run the Tool:**
```sh
python nist_compliance_tool.py
```

---

## 🛠️ **Tool Usage:**
- **Menu Options:**
```plaintext
1. Display all requirements
2. Search compliance requirements
3. List requirements not evaluated
4. Update compliance status
5. Generate compliance report (CSV & PDF)
6. Backup compliance data
7. Exit
```

---

## 📊 **Report Generation:**
- **CSV Report:** Provides a **detailed tabular view** of the **compliance status**.
- **PDF Report:** Presents a **print-friendly version** of the **compliance data**.

---

## 🛠️ **Troubleshooting**
- **Error loading CSV:** Ensure the **CSGNIST800171Compliance.csv** file is in the **correct format** and **present in the same directory** as the script.
- **Invalid Index:** When updating compliance status, ensure the **index provided is within range**.

---

## 👥 **Contributing**
Feel free to **submit issues** or **pull requests** to improve this tool.

---

## 📄 **License**
This project is **open-source** and available under the **MIT License**.

