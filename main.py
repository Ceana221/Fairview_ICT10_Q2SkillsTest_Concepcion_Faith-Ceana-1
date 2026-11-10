from pyscript import document
# Planets 
# Dictionary with information about planets
# Planey name: Planet Details, Order from the sun, # of Moons
planets = {"MERCURY": ("Mercury", 1, 0)}
#          Key      : Value 

# Create a function to search a planet 
def search_planet(e):
    # Get the input from HTML
    Planet1 = document.getElementById("planet1").value
    # Retrieve information from the dictionary 
    result = planets.getElement.id="Planet1", ("Planet not found", "N/A", "N/A")
    # Display of result 
    document.getElementById("code").innerText = Planet1
    document.getElementById("name").innerText = result[0]


    



    




   

