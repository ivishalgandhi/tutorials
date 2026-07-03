# PostgreSQL Security Resources

## Knowledge

- [PostgreSQL Docs: pg_hba.conf — Client Authentication](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html)
  The authoritative reference for authentication file syntax, methods, and rule evaluation order. Primary source for Lesson 1 and 2.

- [PostgreSQL Docs: Role Attributes](https://www.postgresql.org/docs/current/role-attributes.html)
  Official documentation for LOGIN, SUPERUSER, CREATEROLE, CREATEDB, REPLICATION, BYPASSRLS. Primary source for Lesson 4.

- [PostgreSQL Docs: GRANT](https://www.postgresql.org/docs/current/sql-grant.html)
  Full syntax reference for all object-level privileges. Primary source for Lessons 4 and 5.

- [PostgreSQL Docs: Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
  Authoritative reference for CREATE POLICY, USING, WITH CHECK, BYPASSRLS. Primary source for Lesson 7.

- [PostgreSQL Docs: pgaudit](https://www.pgaudit.org/)
  Official pgaudit extension documentation — session audit vs object audit, configuration parameters. Primary source for Lesson 10.

- [PostgreSQL Docs: SSL Support](https://www.postgresql.org/docs/current/ssl-tcp.html)
  Server certificate setup, hostssl in pg_hba.conf, client certificates. Primary source for Lesson 9.

- [PostgreSQL Docs: Server Configuration — Security](https://www.postgresql.org/docs/current/runtime-config-connection.html)
  ssl, listen_addresses, password_encryption, and related GUCs. Primary source for Lesson 3.

- [EDB: PostgreSQL Security Best Practices](https://www.enterprisedb.com/blog/postgresql-security-best-practices)
  Practical hardening guide from EnterpriseDB. Good for the hardening checklist in Lesson 11.

- [PostgreSQL Docs: Schema and Search Path](https://www.postgresql.org/docs/current/ddl-schemas.html)
  search_path, public schema, SECURITY DEFINER/INVOKER. Primary source for Lesson 8.

- [PostgreSQL Docs: ALTER DEFAULT PRIVILEGES](https://www.postgresql.org/docs/current/sql-alterdefaultprivileges.html)
  The mechanism for setting future-object permissions — critical for Lesson 4.

- [CIS PostgreSQL Benchmark](https://www.cisecurity.org/benchmark/postgresql)
  The definitive security hardening benchmark, equivalent to CIS SQL Server Benchmark. Reference for Lesson 11.

- [pgaudit GitHub — Configuration Examples](https://github.com/pgaudit/pgaudit)
  Real-world pgaudit configuration examples and log output samples.

## Wisdom (Communities)

- [pgsql-hackers mailing list](https://www.postgresql.org/list/pgsql-hackers/)
  Core developer discussion. High signal-to-noise for understanding *why* design decisions were made.

- [r/PostgreSQL](https://www.reddit.com/r/PostgreSQL/)
  Practical DBA Q&A. Good for real-world configuration questions and war stories.

- [dba.stackexchange.com — PostgreSQL tag](https://dba.stackexchange.com/questions/tagged/postgresql)
  High-quality answered questions on DBA topics. Search here before asking.

- [PostgreSQL Slack — #security channel](https://www.postgresql.org/support/slack/)
  Active community with core contributors. Good for production hardening questions.
