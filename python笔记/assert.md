```python
# flask, views.py
assert meth is not None, "Unimplemented method %r" % request.method
# flask, blueprint.py
assert "." not in endpoint, "Blueprint endpoints should not contain dots"
```