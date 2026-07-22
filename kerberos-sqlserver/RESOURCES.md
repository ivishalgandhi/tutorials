# Kerberos for SQL Server Resources

## Knowledge

- [Microsoft Learn: Register a Service Principal Name for Kerberos Connections - SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/register-a-service-principal-name-for-kerberos-connections?view=sql-server-ver17)
  The canonical reference for SQL Server SPN formats, automatic vs. manual registration, and the `auth_scheme` check. Use for every SPN decision.

- [Microsoft Learn: Configure Windows Service Accounts and Permissions - SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-windows-service-accounts-and-permissions?view=sql-server-ver17)
  Covers gMSA, MSA, virtual accounts, and the per-service-SID model. Use when choosing or changing a SQL service account.

- [Microsoft Learn: Manage Group Managed Service Accounts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/manage-group-managed-service-accounts)
  How to create, install, and verify gMSAs. Use for the Kerberos + gMSA prerequisites section.

- [Microsoft Learn: Using Kerberos Configuration Manager for SQL Server](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/connect/using-kerberosmngr-sqlserver)
  Diagnostic tool that reports missing/duplicate SPNs and delegation settings. Use for troubleshooting and generating fix scripts.

- [PostgreSQL Documentation: GSSAPI Authentication](https://www.postgresql.org/docs/current/gssapi-auth.html)
  Official guide to configuring PostgreSQL Kerberos/GSSAPI authentication, keytab setup, and pg_hba.conf lines. Use for all PostgreSQL Kerberos work.

- [Microsoft Learn: Linked Servers (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-database-engine?view=sql-server-ver17)
  Official overview of linked-server architecture and pass-through authentication. Use as the base for the double-hop/delegation lessons.

- [Microsoft TechCommunity: Intermittent ANONYMOUS LOGON of SQL Server linked server double hop](https://techcommunity.microsoft.com/blog/sqlserversupport/intermittent-anonymous-logon-of-sql-server-linked-server-double-hop/3694876)
  Microsoft support article covering SPN checklist, constrained delegation, and the intermittent ticket-expiry scenario. Use for linked-server Kerberos troubleshooting.

- [Microsoft Learn: Register a Service Principal Name (SPN) for a report server - SSRS](https://learn.microsoft.com/en-us/sql/reporting-services/report-server/register-a-service-principal-name-spn-for-a-report-server?view=sql-server-ver17)
  SSRS-specific SPN registration. Use when configuring Kerberos for Reporting Services.

- [Microsoft Learn: Configure Windows authentication on the report server - SSRS](https://learn.microsoft.com/en-us/sql/reporting-services/security/configure-windows-authentication-on-the-report-server?view=sql-server-ver17)
  Covers `RSWindowsNegotiate`, `RSWindowsKerberos`, `RSWindowsNTLM`, and how to force or fall back from Kerberos. Use for SSRS auth tuning.

- [Microsoft TechCommunity: Service Principal Name Attribute Limitations](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/service-principal-name-attribute-limitations/ba-p/257489)
  Explains the ~1200 practical limit on `servicePrincipalName` values per AD object. Use when deciding whether one gMSA can host many SPNs.

## Wisdom (Communities)

- [SQL Server tag on Server Fault](https://serverfault.com/questions/tagged/sql-server)
  High-signal Q&A for operational SQL Server issues including Kerberos and SPNs. Use when a scenario does not match the Microsoft docs exactly.

- [Microsoft Q&A for SQL Server](https://learn.microsoft.com/en-us/answers/tags/191/sql-server)
  Official Microsoft community. Use for questions that may involve product bugs or undocumented behavior.

- [r/SQLServer](https://reddit.com/r/SQLServer)
  General peer discussion. Use sparingly; verify answers against Microsoft documentation.
