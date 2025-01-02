
from twelvelabs import TwelveLabs
import json
import requests

class TwelveLabsSearch:
    # Initialize the TwelveLabs client once in the constructor
    def __init__(self):
        self.api_key = "API_KEY"
        self.client = TwelveLabs(api_key=self.api_key)

    @staticmethod
    def save_json(query_results, file_name):
        # Save the data as a list of lists of JSON objects
        with open(file_name, 'w') as json_file:
            json.dump(query_results, json_file, indent=4)

    def query(self, query_text_list, file_name=None):
        all_results = []  # List of lists of dictionaries

        for query_text in query_text_list:
            search_results = self.client.search.query(
                index_id="66f1b1c8163dbc55ba3bb1b6",
                query={"text": query_text},
                
                # query = {
                #     "$not": {
                #         "origin": {
                #             "text": query_text
                #         },
                #         "sub": {
                #             "$or": [
                #                 {
                #                     "text": "News Anchor"
                #                 },
                #                 {
                #                     "text": "Podcast"
                #                 }
                #             ]
                #         }
                #     }
                # },

                options=["visual"]
            )
            
            query_result = []  # List of dictionaries for this query
            while True:
                
                try:
                    # Retrieve each page of search results
                    page_data = next(search_results)
                    for clip in page_data:  # Limiting to 3 results per page
                        query_result.append({
                            "video_id": clip.video_id,
                            "score": clip.score,
                            "start": clip.start,
                            "end": clip.end,
                            "confidence": clip.confidence,
                            "metadata": clip.metadata,
                        })
                except StopIteration:
                    break
            all_results.append(query_result)  # Append this query's results as a list

        if file_name:
            self.save_json(all_results, file_name)

        return all_results  # List of lists of dictionaries
    
    @staticmethod
    def get_video_info(video_id):
        api_key= "API_KEY"
        index_id="66f1b1c8163dbc55ba3bb1b6"
        url = f"https://api.twelvelabs.io/v1.2/indexes/{index_id}/videos/{video_id}"
        headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json",
        }
        
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            video_info = response.json()  # Parse response as JSON
            return video_info
        elif response.status_code == 400:
            print("The request has failed. Check your parameters.")
            return None
        else:
            print(f"Error: Status code {response.status_code}")
            return None

# Example usage
if __name__ == "__main__":
    query_text_list = [
        "Yusuf Dikec, Turkish sharpshooter, known for his casual and unorthodox shooting style",
    ]
    
    file_name = "../data/data.json"
    
    searcher = TwelveLabsSearch()
    # Call with a list of queries and a file name to save the combined results as JSON
    results = searcher.query(query_text_list, file_name=file_name)
    print(results)
    

