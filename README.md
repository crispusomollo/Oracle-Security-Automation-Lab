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

## 🧩 Modules

| No. | Module                                | Focus / Key Concepts                                         | Automation       |
|:---:|:-------------------------------------|:-------------------------------------------------------------|:----------------|
| 01  | **Users, Roles & Profiles**           | User creation, role assignment, password policies            | SQL + Bash       |
| 02  | **Object Privileges**                 | Grant/revoke system/object privileges                        | SQL              |
| 03  | **Role-Based Access Control (RBAC)**  | Hierarchical roles, least privilege enforcement              | SQL + Python     |
| 04  | **Password & Resource Policies**      | Account lockouts, password limits, secure authentication    | SQL              |
| 05  | **Virtual Private Database (VPD)**    | Row-level security using `DBMS_RLS` policies                 | SQL + Python     |
| 06  | **Fine-Grained Auditing (FGA)**       | Audit SELECT/UPDATE operations based on conditions          | SQL + Bash       |
| 07  | **Transparent Data Encryption (TDE)** | Tablespace encryption, wallet setup                           | SQL + Bash       |
| 08  | **Database Vault (DBV)**              | Security realms, separation of duty, command rules          | SQL + Bash       |
| 09  | **Unified Auditing**                  | Centralized audit policy management                           | SQL + Python     |
| 10  | **Oracle Label Security (OLS)**       | Data classification, access labels                             | SQL + Python     |
| 11  | **Login Reports & Monitoring**        | Track logins, failed attempts, user activity                | SQL + Python     |
| 12  | **TNS Listener & Network Security**   | Listener hardening, network access controls                 | Bash + Python    |
| 13  | **OS Hardening (Oracle Linux 23 AI)** | File, service, firewall, and package security               | Bash             |
| 14  | **Compliance Scanner & Reporting**    | Auto-scan all modules, generate compliance reports          | Python + SQL     |
| 15  | **Audit Vault / Data Masking**        | Centralized audit collection, dynamic masking of sensitive data | SQL + Python |
| 16  | **DB Links Security**                 | Secure remote database access, monitor DB links             | SQL + Bash       |
| 17  | **TLS / Encryption in Transit**       | Client-server encryption, certificate management            | Bash + Python    |
| 18  | **Backup & Recovery Security**        | Encrypted backups, RMAN access control                      | SQL + Bash       |
| 19  | **Session & Privilege Analysis**      | Active session monitoring, privilege abuse detection         | SQL + Python     |

> Each module includes its own `README.md`, SQL scripts, and automation wrapper (`module.sh` or `module.py`).

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

