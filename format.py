markup = """
<!DOCTYPE html>

<html>

    <head>
        <title>{0}</title>
    </head>

    <body>
        <h1>{0}</h1>
        <h2>{1}</h2>
        <p>{para}</p>
    </body>
</html>
"""

markup = markup.format('My Format Page', 'Welcome to My Format Page!', para = "I am so glad you made it here! Sorry there's not much here yet.")
print(markup)


# Entering {0} and {1} are placeholders that will insert the 0 index and 1 index arguments in the spot in which they were placed

# The .format method allows values to be given in place of the indices provided (e.g., {0} would be 'My Format Page')