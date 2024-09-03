import requests

# Send GET request to the API
url = "https://corporatebs-generator.sameerkumar.website/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the generated phrase from the JSON response
    bs_phrase = response.json()["phrase"]

    # Save the phrase to a text file
    with open("corporate_bs.txt", "w") as file:
        file.write(bs_phrase)

    print("Corporate BS phrase saved to corporate_bs.txt")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
