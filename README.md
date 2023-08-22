# autodiff

A project to (attempt to) implement autodiff in OCaml, to be the backbone of a larger Torch-like library.

The goals of the project are to:
- Learn how auto-differentiation works
- Learn more advanced OCaml features (and use them to make the library nice)

I'll implement the prototypes in Python to make sure that I've got the main idea right, then I'll try to write up the actual library in OCaml.

## Todo
- [ ] Re-write backward pass to happen as loop over reverse topoligal sort
    - I thought it might work with a recursive implementation, where each node added to the gradient of the child, and evaluate the value of a node on-call, but this doesn't work if the derivative of `a` involves the the value `a()` itself, in which case the `a.grad` begins as `0` and recursively runs evaluation for its children, before `a.grad` can be updated by `a`'s parents
- [ ] Re-write Python prototype to automatically generate computational graph from ordinary functions
- [ ] Implement limited operations in OCaml (Add and Multiply)