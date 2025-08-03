def http_match(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
print(http_match(200))
print(http_match(404))
print(http_match(500))

print(http_match(84848))
print(http_match("jkjdkasd"))