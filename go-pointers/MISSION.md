# Mission: Go Pointers — When to Point, When to Copy

## Why
I am new to Go and want to build a solid mental model of pointers, memory, and mutability. I want to stop guessing whether a function should accept `*T` or `T`, and I want to understand why a function sometimes changes the caller's data and sometimes does not.

## Success looks like
- I can explain the difference between value semantics and pointer semantics in Go.
- I can predict whether a function modifies the caller's data or a local copy.
- I can refactor a value-based design to a pointer-based design and explain the trade-offs (memory, aliasing, nil safety).
- I can spot common pointer mistakes: nil pointer dereference, unintended aliasing, and pointer receiver confusion.
- I can make intentional `*T` vs `T` decisions when reading and writing Go code.

## Constraints
- Go beginner (< 6 months) — every non-obvious Go construct must be explained, not just shown.
- Focus on practical understanding, not performance optimization or GC internals.
- Examples use the standard library only.
- Every lesson includes a real-world scenario, a before/after comparison, a short quiz, and a hands-on exercise.

## Out of scope
- The `unsafe` package, `cgo`, or pointer arithmetic.
- Generics combined with pointers.
- Detailed escape analysis or GC tuning.
- Low-level memory layout and CPU cache optimization.
