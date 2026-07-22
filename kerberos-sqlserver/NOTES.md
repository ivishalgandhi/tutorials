# Notes

- User is a SQL Server and PostgreSQL administrator whose organization is deprecating NTLMv2.
- Environment uses (or plans to use) a gMSA as the SQL Server service account.
- PostgreSQL Kerberos integration will use a keytab file (KRB5_KTNAME) for GSSAPI authentication.
- Topics of immediate concern: SPN registration, FQDN vs. short name vs. port, AG listener SPNs, AD change impact, linked-server double-hop, SSRS/SSAS/Power BI auth, PostgreSQL keytab setup.
- Teaching style preference to be determined by user feedback.
