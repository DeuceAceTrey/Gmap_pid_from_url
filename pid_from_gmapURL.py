import re
import googlemaps

def get_place_id(api_key, google_maps_url):
    gmaps = googlemaps.Client(key=api_key)

    # Extract place ID from URL
    match = re.search(r'placeid=([\w-]+)', google_maps_url)
    if match:
        place_id = match.group(1)
        return place_id

    # If place ID is not found in URL, use Place API to find it
    result = gmaps.find_place(
        input=google_maps_url,
        input_type="textquery",
        fields=["place_id"]
    )

    if result['status'] == 'OK' and 'candidates' in result:
        place_id = result['candidates'][0]['place_id']
        return place_id

    return None

if __name__ == "__main__":
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"
    google_maps_url = "https://www.google.com/maps/place/YOUR_PLACE"
    
    place_id = get_place_id(api_key, google_maps_url)
    
    if place_id:
        print(f"Place ID: {place_id}")
    else:
        print("Failed to retrieve Place ID.")
