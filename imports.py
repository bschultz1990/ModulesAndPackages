modules = ['thing1', 'thing2', 'thing3']
failed_imports = []

for m in modules:
    try:
        import m
    except ImportError:
        failed_imports.append(m)

if failed_imports:
    print("The following modules were not found. Please install them before continuing:")
    for f in failed_imports:
        print(f)


