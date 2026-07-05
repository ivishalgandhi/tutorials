# Go Pointers — Resources

## Knowledge

### Pointers — Primary Sources

- [Go by Example: Pointers](https://gobyexample.com/pointers)  
  The canonical side-by-side comparison of `zeroval` (value) and `zeroptr` (pointer). Best first read for anyone new to `&` and `*` in Go.

- [A Tour of Go: Pointers](https://go.dev/tour/moretypes/1)  
  Official language tour. Explains the `*T` type, `&` address-of, and `*` dereference with the `Vertex` example.

- [Go by Example: Structs](https://gobyexample.com/structs)  
  Shows how `&` yields a struct pointer, and that Go automatically dereferences struct pointer fields (`sp.age`).

- [Go by Example: Methods](https://gobyexample.com/methods)  
  Contrasts value receivers (`perim`) and pointer receivers (`area`). Explains automatic `&`/`*` conversion for method calls.

- [Go by Example: Command-Line Flags](https://gobyexample.com/command-line-flags)  
  A practical pointer example from the standard library: `flag.String` returns `*string`, and `flag.StringVar` takes `&svar`.

- [Go Wiki: Code Review Comments — Receiver Type](https://go.dev/wiki/CodeReviewComments#receiver-type)  
  The official guideline for choosing value vs pointer receivers. Lists the concrete cases where a pointer is required (mutation, mutexes, large structs, shared state).

- [Go Wiki: MethodSets](https://go.dev/wiki/MethodSets)  
  Explains the method-set rules that make pointer-receiver methods unavailable on non-addressable values and interface values.

- [Go Blog: Arrays, slices (and strings): The mechanics of 'append'](https://go.dev/blog/slices)  
  Not strictly about pointers, but the section on pointers to slices and method receivers clarifies when a method must reslice in place.

### Pointers — Videos

- [TomDoesTech — A Practical Guide to Pointers in Go](https://www.youtube.com/watch?v=PR4BwsZaJY0)  
  ~10 min. Focuses on *when and why* to use pointers, with memory-address visuals. Best video for this course.

- [freeCodeCamp / boot.dev — Go Programming Course, Chapter 11: Pointers](https://www.youtube.com/watch?v=un6ZyFkqFKo)  
  Comprehensive beginner course. Jump to the pointers chapter for a slower, exercise-driven walkthrough.

## Skills

- Declaring and dereferencing pointers: `var p *int`, `*p = 42`, `p := &x`.
- Reading the `flag` package's pointer-returning API.
- Predicting value vs pointer behavior in function arguments and method receivers.
- Refactoring a value-based function to a pointer-based one without breaking callers.
- Writing nil-safe pointer-receiver methods.

## Wisdom (Communities)

- [r/golang](https://reddit.com/r/golang) — strong community for "is this idiomatic?" questions.
- [Go Forum](https://forum.golangbridge.org/) — beginner-friendly, moderated.
- [Gophers Slack](https://invite.slack.golangbridge.org/) — `#golang` and `#newbies` channels for real-time help.

## Gaps

- Most beginner tutorials stop at `*int` and do not connect pointers to real APIs like `flag.String` or `json.Unmarshal`.
- Receiver-type advice is scattered across the Wiki, the Go Blog, and method-set docs. This course consolidates it into a single decision table.
- The "when and why" of pointers is best learned by comparing working and broken versions of the same real program.
