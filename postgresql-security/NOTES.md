# Teaching Notes

## User Profile
- Senior SQL Server DBA (production experience, deep knowledge of logins/users/roles, SQL Audit, Windows Auth/Kerberos, Always On)
- New to PostgreSQL security specifics — knows *what* needs to exist but not *how* PostgreSQL implements it
- Managing live production PostgreSQL — pragmatic, production-grade guidance required
- Explicitly asked for SQL Server mappings and clear flags where PostgreSQL diverges

## Teaching Preferences
- Map every concept to SQL Server equivalent where it exists
- Flag PostgreSQL-specific gotchas that will trip up an MSSQL DBA
- Show exact working syntax with real examples — no pseudocode
- Security focus: top 1–2 DBA mistakes per section
- Quiz options must be identical in length (anti-hint rule)

## Lesson Plan (11 lessons requested)
1. pg_hba.conf — Authentication Configuration
2. LDAP Authentication & Active Directory Integration
3. postgresql.conf Security Parameters
4. Roles & Privileges
5. Custom Roles & Role Composition
6. CI/CD Service Account Patterns
7. Row-Level Security (RLS)
8. Schema Security & search_path Hardening
9. SSL/TLS Configuration
10. Auditing & Logging (pgaudit)
11. Hardening Checklist

## References
- reference/glossary.html — PostgreSQL security terms with SQL Server mappings
- reference/quick-reference.html — 15-command cheat sheet
