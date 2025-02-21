# NIST 800-171 Compliance Tool

This tool helps organizations manage their compliance with **NIST 800-171** requirements by providing a command-line interface to view, update, and generate reports on compliance status.

---

## 📂 **Features**
- Display all **compliance requirements** with status.
- Update compliance status (**Compliant**, **Non-Compliant**, **Not Applicable**).
- Generate a **CSV report** of the compliance status with **evidence**.

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

## 📊 **How to Use**
1. **Display All Requirements:**
   - Choose option **1** to view all **compliance requirements**.

2. **Update Compliance Status:**
   - Choose option **2**.
   - Enter the **requirement index**, **status**, and **optional evidence**.

3. **Generate a Compliance Report:**
   - Choose option **3** to export the **compliance report** as **compliance_report.csv**.

4. **Exit the Tool:**
   - Choose option **4**.

---

## 📁 **Output**
- Generates a **CSV report** named **compliance_report.csv** in the **project directory**.

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

