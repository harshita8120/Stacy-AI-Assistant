import requests
import speech

newsapi = "pub_3f0fc47b6ce74728bb1075a5e2b3c8e0"


def newsHeadline():
    try:
        r = requests.get(f"https://newsdata.io/api/1/latest?apikey={newsapi}&language=en")
        data = r.json()
        
        if data.get("status") == "success":
            articles = data.get("results", [])
            speech.speak(f"Here are the top 5 headlines")
        
            seen = set()  # track seen headlines
            count = 0

            for article in articles:
                headline = article.get("title", "No title")
            
                if headline not in seen:  # only speak if not duplicate
                    seen.add(headline)
                    count += 1
                    print(f"{count}. {headline}")
                    speech.speak(headline)
                
                if count == 5:  # stop after 5 unique headlines
                    break

        else:
            speech.speak("Sorry, I couldn't fetch the news right now")
    except Exception as e:
        print(f"News error: {e}")
        speech.speak("Sorry, there was an error fetching the news")
