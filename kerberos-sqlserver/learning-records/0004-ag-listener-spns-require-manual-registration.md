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
