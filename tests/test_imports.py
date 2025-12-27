def test_import_packages():
    # Smoke test: ensure packages are importable
    import importlib

    modules = ["agents", "audit", "decision", "safety"]
    for m in modules:
        mod = importlib.import_module(m)
        assert mod is not None
