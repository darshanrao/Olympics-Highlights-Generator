
def extract_queries_within_time_limit(data, time_limit):
    result = []
    total_time = 0

    # Determine the maximum number of sub-lists
    print("data:",data)
    max_length = max(len(queries) for queries in data)

    # Iterate through each index, taking the ith query from each list
    for i in range(max_length):
        for queries in data:
            if i < len(queries):  # Check if the ith query exists
                query = queries[i]
                start = query['start']
                end = query['end']
                duration = end - start

                # Check if adding this query exceeds the time limit
                if total_time + duration <= time_limit:
                    result.append(query)
                    total_time += duration
                    break  # Move to the next index after taking a valid query
    print(total_time)
    return result


# data = [
#     [
#         {
#             "video_id": "66f1b1e84e302ab9f2e7ef20",
#             "score": 83.42,
#             "start": 0.0,
#             "end": 15.0,
#             "confidence": "high",
#             "metadata": None
#         },
#         {
#             "video_id": "66f1b1e1ae10e5f05781c7a9",
#             "score": 83.22,
#             "start": 89.0,
#             "end": 109.0,
#             "confidence": "high",
#             "metadata": None
#         },
#         {
#             "video_id": "66f1b1e1ae10e5f05781c7a9",
#             "score": 83.1,
#             "start": 9.0,
#             "end": 17.0,
#             "confidence": "high",
#             "metadata": None
#         },
#         {
#             "video_id": "66f1b1e84e302ab9f2e7ef20",
#             "score": 82.03,
#             "start": 59.0,
#             "end": 86.0,
#             "confidence": "medium",
#             "metadata": None
#         },
#         {
#             "video_id": "66f1b1e24e302ab9f2e7ef1e",
#             "score": 80.11,
#             "start": 67.0,
#             "end": 85.0,
#             "confidence": "medium",
#             "metadata": None
#         },
#         {
#             "video_id": "66f1b1e84e302ab9f2e7ef20",
#             "score": 79.53,
#             "start": 111.0,
#             "end": 135.0,
#             "confidence": "medium",
#             "metadata": None
#         },
#         {
#             "video_id": "66f1b1e1ae10e5f05781c7a9",
#             "score": 79.33,
#             "start": 64.0,
#             "end": 72.0,
#             "confidence": "medium",
#             "metadata": None
#         },
#         {
#             "video_id": "66f1b1e9ae10e5f05781c7af",
#             "score": 78.52,
#             "start": 34.0,
#             "end": 52.0,
#             "confidence": "medium",
#             "metadata": None
#         },
#         {
#             "video_id": "66f1b1e24e302ab9f2e7ef1e",
#             "score": 76.47,
#             "start": 176.0,
#             "end": 185.0,
#             "confidence": "medium",
#             "metadata": None
#         },
#         {
#             "video_id": "66f1b1e84e302ab9f2e7ef20",
#             "score": 75.04,
#             "start": 27.0,
#             "end": 37.0,
#             "confidence": "medium",
#             "metadata": None
#         }
#     ]
# ]

# # Call the function with a time limit of 90 seconds
# result = extract_queries_within_time_limit(data, time_limit=90)

# # Print the result
# for query in result:
#     print(query)



        
        