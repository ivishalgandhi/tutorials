# Initial session: Kerberos for SQL Server mission established

The user is responsible for SQL Server in an organization that is deprecating NTLMv2 in favor of Kerberos. Their service account model is a gMSA. Immediate concerns are SPN registration, FQDN/port/AG listener formats, silent NTLM fallback, impact of AD changes and restarts, and Kerberos behavior for linked servers, SSRS, SSAS, and Power BI.

This record sets the baseline: the user understands the business driver (disable NTLMv2) but is not yet confident with SPN mechanics or the operational side effects of AD changes. Future lessons should stay tightly tied to these operational questions rather than abstract protocol theory.
