
class Coordinate:
    def __init__(self):
        self.api_url = "https://zenquotes.io/api/today"
    
    def getCoordinate(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            if data and isinstance(data, list):
                quote = data[0]['q']
                author = data[0]['a']
                return f"\"{quote}\" - {author}"
            else:
                return "No quote found."
        except requests.exceptions.RequestException as e:
            return f"Error fetching quote: {e}"
        
    def coordinateToLoc():
        print("bleh")

# Example usage
    #zen_quotes = QuotesWidget()
    #print(zen_quotes.get_quote())
