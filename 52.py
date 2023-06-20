flavor=("strawberry","vanila","lemon")

flavor.add("chocolate")
flavor.add("marshmallows")
flavor.add("500")

flavor.update(["cottoncandy","honey","cola"])

print(flavor)
flavor.discard("rose")
del flavor
print(flavor)