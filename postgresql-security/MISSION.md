# Mission: PostgreSQL Security — End to End

## Why
I manage a production PostgreSQL environment and need to master its security model completely. I have deep SQL Server DBA expertise and want to map PostgreSQL security onto what I already know — and clearly understand where it diverges — so I can harden our PostgreSQL estate with the same confidence I have in SQL Server.

## Success looks like
- I can write a correct pg_hba.conf from scratch, including LDAP/AD integration, with no misconfigurations
- I can design and implement a full role hierarchy (readonly → readwrite → admin) and CI/CD service account patterns without reaching for superuser
- I can enable and configure pgaudit to produce SQL Server Audit–equivalent output
- I can explain RLS policies, SECURITY DEFINER risks, and search_path hijacking to a junior DBA
- I can run through the hardening checklist against a new PostgreSQL cluster and close every gap
- I can recite the 15 most critical security commands from memory

## Constraints
- Strong SQL Server DBA background (logins, users, roles, SQL Audit, Windows Auth, Always Encrypted awareness)
- New to PostgreSQL security specifics (pg_hba.conf, SCRAM, peer auth, role inheritance model, pgaudit)
- Managing a live production PostgreSQL environment — practical, production-grade guidance over theory
- Wants SQL Server mappings wherever they exist; clear flags where PostgreSQL differs significantly

## Out of scope
- PostgreSQL replication architecture (separate topic)
- Query performance tuning and index strategy
- Backup and recovery procedures
- Application-layer encryption (pgcrypto) beyond SSL/TLS
