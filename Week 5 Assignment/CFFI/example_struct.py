from cffi import FFI

ffi = FFI()

# Load the shared library
lib = ffi.dlopen("./libstruct_example.dylib")

# Declare the C structure and function signature
ffi.cdef("""
    struct Point {
        int x;
        int y;
    };

    int distance(struct Point p1, struct Point p2);
""")

# Create two Point instances
point1 = ffi.new("struct Point *", {'x': 1, 'y': 2})
point2 = ffi.new("struct Point *", {'x': 4, 'y': 6})

# Call the distance function
result = lib.distance(point1[0], point2[0])

print(f"Distance squared between points: {result}")