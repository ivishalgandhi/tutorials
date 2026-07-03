# SQL Server DBA — Established Prior Knowledge

The user is a senior SQL Server DBA with production experience. They have deep knowledge of SQL Server logins, users, roles (db_datareader, db_datawriter, db_ddladmin, sysadmin), SQL Audit, Windows Authentication, Kerberos, SQL Server Certificate Manager, and Always On Availability Groups. This changes the entire teaching approach: every PostgreSQL concept should be anchored to the SQL Server equivalent where one exists, and explicitly flagged where PostgreSQL works fundamentally differently.

**Evidence:** User's initial request explicitly stated "strong SQL Server DBA experience" and asked for SQL Server mappings throughout.

**Implications:** Skip basics of relational security (users, permissions, audit concepts) — user knows these. Focus on how PostgreSQL implements them differently. Prioritise: pg_hba.conf (no SQL Server equivalent), role inheritance model (very different), search_path hijacking (no SQL Server equivalent), ALTER DEFAULT PRIVILEGES (SQL Server DBAs always miss this).
