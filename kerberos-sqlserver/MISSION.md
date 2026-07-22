# Mission: Kerberos for SQL Server and PostgreSQL Operations

## Why
The user's organization is moving from NTLMv2 to Kerberos. As the person responsible for SQL Server and PostgreSQL, they need to keep Database Engine, SSRS, SSAS, Power BI, and PostgreSQL authenticating correctly via Kerberos, detect and eliminate silent NTLM fallback, manage SPNs and PostgreSQL keytabs with a gMSA, and make AD-side changes without surprising application owners or linked-server consumers.

## Success looks like
- Can explain how Kerberos authentication works for SQL Server and PostgreSQL and verify Kerberos is actually being used.
- Can register, verify, and troubleshoot SPNs for default instances, named instances, Always On availability group listeners, SSRS, SSAS, and PostgreSQL using `setspn` and `klist`/`krb5` tooling.
- Can configure SQL Server services to run under a gMSA and delegate only the minimum SPN permissions required.
- Can configure PostgreSQL GSSAPI/Kerberos authentication with a keytab file and verify it via logs and `pg_stat_activity`.
- Can predict the impact of AD/SPN/keytab changes and SQL/PostgreSQL service restarts on existing applications, linked servers, and delegation.
- Can diagnose and resolve double-hop linked-server delegation failures.

## Constraints
- NTLMv2 is being deprecated; silent NTLM fallback must be detected and treated as a misconfiguration.
- Prefer gMSA over plain domain user accounts; avoid shared service accounts and standing domain-admin rights.
- PostgreSQL should use GSSAPI/Kerberos (`gss` or `sspi`) where AD integration is required, with keytab files rather than stored passwords.
- Changes must not cause unplanned application downtime.

## Out of scope
- Deep cryptographic internals of Kerberos (encryption suites, ASN.1 encoding).
- Kerberos configuration for non-Microsoft databases or generic web applications.
- Building custom monitoring tools beyond DMVs, PostgreSQL logs, SQL error logs, event logs, and Microsoft Kerberos Configuration Manager.
