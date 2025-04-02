# Spot VM Snapshot Automation 📸☁️

This project automates snapshots of Azure Spot VMs using a serverless Python Azure Function. It’s designed to run on a schedule, identify Spot VMs in a resource group, and take snapshots of their OS disks for cost-effective backup.

---

## 🚀 Features
- ⏰ Hourly snapshot automation (CRON scheduled)
- 🧠 Uses Azure Managed Identity to access VM resources
- 💾 Snapshots tagged by VM name and timestamp
- 🛠️ Deployed via Azure Bicep + Azure CLI

---

## 🛠 Tech Stack
- **Azure Functions (Python)**
- **Bicep (Infrastructure as Code)**
- **Azure CLI**
- **Azure Compute + Storage**

---

## 📂 Folder Structure
```
spotvm-snapshot-automation/
├── function-app/              # Azure Function code
│   ├── __init__.py
│   ├── function.json
│   ├── host.json
│   └── requirements.txt
├── main.bicep                # Bicep template to deploy infrastructure
├── .gitignore
└── README.md                 # You're here!
```

---

## ⚙️ How to Deploy

### 🧱 1. Deploy infrastructure with Bicep:
```bash
az deployment group create \
  --resource-group <your-rg> \
  --template-file main.bicep
```

### 🐍 2. Deploy the Function (from local machine):
```bash
cd function-app
func azure functionapp publish <your-function-app-name>
```

---

## 📈 To-Do / Improvements
- [ ] Add GitHub Actions for CI/CD
- [ ] Add email or Teams alert on snapshot failure
- [ ] Add snapshot retention policy automation

---

## 🙌 Author
Built by [@HOODIE3](https://github.com/HOODIE3) to demonstrate cost-effective Azure automation with serverless architecture and IaC.

> 💡 💪
