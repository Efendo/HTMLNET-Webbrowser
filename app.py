
def visit():
    try:
        searchBar = Element("searchBar")
        tCanvas = Element("t-canvas")
        website = f"https://{searchBar.value}"
        tCanvas.element.innerHTML = "<iframe class='w-screen h-screen my-150' src=" + website + ">"
    except TypeError as e:
        print(f"An error occurred while visiting the website: {str(e)}")