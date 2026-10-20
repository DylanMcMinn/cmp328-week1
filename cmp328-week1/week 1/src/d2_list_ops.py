modules = ["AI", "Networks"]
modules.append("databases")
modules.insert(1, "Security")
removed = modules.pop(0)
modules.sort()
print("Removed:", removed)
print("Now:", modules)