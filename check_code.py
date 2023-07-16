import pycodestyle

style = pycodestyle.StyleGuide(quiet=True)
result = style.check_files("test.py")
print(result.total_errors)
print(123)
