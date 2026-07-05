# Notes: Go Pointers

- User is learning Go from first principles; ground every lesson in pass-by-value vs pass-by-reference.
- Lesson 1 uses a task-status updater as the concrete, real-world example.
- Keep the distinction between `*T` as a type and `*p` as a dereference explicit in every lesson.
- Future lessons can cover: standard library pointer APIs (`json.Unmarshal`, `flag`), slices/maps as reference headers, pointer receiver consistency, and common aliasing bugs.
