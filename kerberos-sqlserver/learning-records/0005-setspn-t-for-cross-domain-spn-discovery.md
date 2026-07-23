# Use setspn -T <domain> to scope SPN discovery to one domain

In a multi-domain Active Directory forest, `setspn -X` and `setspn -Q` default to the current logon domain. To discover or audit SPNs in a different domain without running a heavy forest-wide query, use the `-T` switch with the target domain's DNS name.

Examples encountered in production:

```text
# List every SPN registered in the eu.corp.local domain
setspn -T eu.corp.local -Q */*

# Look for duplicate SPNs in a specific domain
setspn -T eu.corp.local -X

# Find every MSSQLSvc SPN in a specific domain
setspn -T eu.corp.local -Q MSSQLSvc/*
```

Compare with the Microsoft-documented forest-wide modifier:

```text
# Query a specific SPN across the entire forest
setspn -F -Q MSSQLSvc/sql01.corp.local:1433

# Search for duplicates across the entire forest (can time out in large forests)
setspn -F -X
```

Key points:
- `-T domain` scopes the query to one domain. This is often faster and less load on the Global Catalog than `-F`.
- `-F` searches the whole forest. Use it when the account or SPN could be anywhere, but be aware it can time out in large environments.
- Both require the usual read rights to the `servicePrincipalName` attribute in the target domain.

This matters because SPNs must be unique across the forest, and duplicates are often created in a different domain than the one the DBA is logged into. Without cross-domain discovery, a duplicate can hide from a simple `setspn -X` run in the local domain.

Sources:
- Microsoft Learn, "Searching for Duplicate SPN's got a little easier": documents `-F`, `-Q`, `-X` switches.
- Field observation: `setspn -T` is the practical switch for scoping discovery to one domain in multi-domain forests.
