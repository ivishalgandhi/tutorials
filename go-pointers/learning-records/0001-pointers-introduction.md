# Pointers Introduction: Values vs Addresses

The user can explain that Go is pass-by-value and can predict when a function modifies the caller's data. They understand the three pointer symbols (`&`, `*T`, `*p`) and can contrast a value receiver with a pointer receiver. They have worked through a real task-status example where the value-based version silently fails and the pointer-based version mutates the caller's struct.

**Evidence:** Completed Lesson 1 quiz and both exercises (fix-the-swap and nil-safe receiver).

**Implications:** Future lessons can build directly on this mental model: slices/maps as reference headers, `json.Unmarshal(&v)`, `flag.String` returning `*string`, and pointer receiver consistency. No need to re-explain `&` and `*` from scratch.
