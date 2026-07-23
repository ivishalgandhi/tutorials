# AG listener SPNs require manual registration

An Always On Availability Group listener is a WSFC cluster resource (a Virtual Network Name), but its SPN is **not** auto-registered when the resource comes online, nor does SQL Server register it automatically at startup.

SQL Server's startup auto-registration only handles SPNs for the local instance's own host name and port. For an AG listener, Microsoft documentation explicitly states that a domain administrator must manually register the SPN on the shared SQL Server service account using `setspn`. All replicas must use the same service account for the listener SPN to remain valid across failovers without any SPN change.

This matters because Lesson 2 discussed gMSA self-registration for host/instance SPNs, which could be misread as covering listener SPNs. It does not.

Consequences:
- Do not rely on the cluster Network Name resource or SQL Server startup to create the listener SPN.
- Treat listener SPN registration as a one-time build task (unless the listener name, port, or service account changes).
- For clustered SQL Server, Microsoft even recommends disabling automatic SPN registration for host/instance SPNs, because SPN unregister/register timing can prevent SQL Server from coming online quickly enough for the cluster.

Primary sources:
- Microsoft Learn, "Prerequisites, restrictions, and recommendations for Always On availability groups": the domain administrator needs to manually register an SPN for the VNN of the AG listener.
- Microsoft Learn, "Register a Service Principal Name for Kerberos connections": automatic SPN registration is for the local SQL Server service; listener SPNs are registered manually.
- Microsoft Learn, "Using Kerberos Configuration Manager for SQL Server": in clustered environments, automatic SPN registration is not recommended.

## Required privileges for listener SPN registration

The listener SPN is registered on the shared SQL Server service account (gMSA or domain user), not on the listener's Virtual Computer Object.

Three ways to get the rights to run `setspn -S MSSQLSvc/AgListener.corp.local:1433 CORP\sqlsvc$`:

| Path | Required privilege |
|------|-------------------|
| Domain Admin | Full control over AD objects; can register on any account. |
| Account Operator | Can create/modify computer and user accounts; can run `setspn`. |
| Delegated (preferred) | Grant on the specific service account: `Validated write to service principal name`, `Read servicePrincipalName`, and `Write servicePrincipalName`. |

The Microsoft-recommended minimum for production is delegation on the specific service account rather than granting Domain Admin. The SQL Server service account itself does not need listener-SPN self-registration rights because SQL Server does not auto-register listener SPNs at startup.
