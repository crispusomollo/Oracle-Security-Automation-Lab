# 🛡️ Oracle Security Automation Lab

A **hands-on, automation-driven Oracle Database Security Portfolio** showcasing how to secure, audit, and automate Oracle environments using **Bash, SQL, and Python**.  
Designed for DBAs and learners who want to understand real-world Oracle security administration on **Oracle Linux 23 AI Free** and **Oracle Database 23c Free**.

---

## 🎯 Project Goals

- Demonstrate **core Oracle security concepts** systematically  
- Build **repeatable, automated workflows** (Bash + SQL + Python)  
- Provide **educational modules** with documentation and sample data  
- Serve as a **portfolio project** highlighting Oracle DBA skills  

---

## 🧩 Topics / Modules

| No. | Module | Focus |
|:---:|:--------|:-------|
| 01 | **Users, Roles & Privileges** | User creation, system/object privileges, role management |
| 02 | **System Auditing** | Standard auditing, log review, and reporting |
| 03 | **VPD & Row-Level Security** | Implementing policies with `DBMS_RLS` |
| 04 | **Data Redaction & Masking** | Protecting sensitive columns dynamically |
| 05 | **Transparent Data Encryption (TDE)** | Wallet configuration and encryption |
| 06 | **Fine-Grained Auditing (FGA)** | Auditing based on conditions/columns |
| 07 | **Security Baselines & Reports** | Password policies, privilege analysis, reports |

> Each module includes its own `README.md`, SQL scripts, and automation wrapper (`module.sh`).

---

## ⚙️ Tech Stack

- **OS:** Oracle Linux 23 AI Free  
- **Database:** Oracle Database 23c Free  
- **Clients:** SQL Developer / SQLcl  
- **Automation:** Bash + SQL + Python 3  
- **Optional Tools:** `cx_Oracle`, `faker`, `draw.io` (for diagrams)

---

## 🚀 Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/crispusomollo/oracle-security-automation-lab.git
cd oracle-security-automation-lab/setup

