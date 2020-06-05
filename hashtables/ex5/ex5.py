# Your code here



def finder(files, queries):
    cache = {}
    for query in queries:
        cache[query] = query

    validFiles = []
    for path in files:
        arr = path.split('/') 
        if arr[len(arr) -1] in cache:
            validFiles.append(path)
    return validFiles









if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
