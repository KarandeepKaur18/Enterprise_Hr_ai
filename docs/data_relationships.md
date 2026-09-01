# Data Relationships

**1. Attrition -> Engagement**
* **Tables:** `employee_attrition_processed.csv` <-> `Employee_Performance_Dataset.csv`
* **Join Key:** `EmployeeNumber` <-> `Employee ID`
* **Relationship:** One-to-One. It's the same employee's performance record.

**2. Attrition -> Occupation Data**
* **Tables:** `employee_attrition_processed.csv` <-> `occupation_master.csv`
* **Join Key:** `JobRole` (or equivalent title column)
* **Relationship:** Many-to-One. Multiple employees share the same role master reference[cite: 2].

**3. Occupation Data -> Skills**
* **Tables:** `occupation_master.csv` <-> `essential_skills_processed.csv` & `software_skills_processed.csv`
* **Join Key:** Element ID / Role ID
* **Relationship:** One-to-Many. One role requires multiple specific skills[cite: 2].