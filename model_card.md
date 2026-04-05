# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
VibeMatch 1.0 

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---
This model recommends 3 to 5 songs based on a user's preferences such as genre, mood, and energy level.

It assumes that users have consistent taste preferences and that song features like energy and genre can represent a user's musical "vibe".

This system is designed for classroom exploration and learning purposes, not for real-world production use.
----------


## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---
The recommender system uses song features such as genre, mood, and energy to calculate how well each song matches a user's preferences.

The user provides a taste profile including their preferred genre, mood, and energy level.

Each song is compared to the user profile and given a score:
- If the genre matches, the score increases
- If the mood matches, additional points are added
- The closer the song's energy is to the user's preferred energy, the higher the score

After scoring all songs, the system ranks them from highest to lowest score and recommends the top results.
----

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
The dataset contains 18 songs with various genres and moods such as pop, rock, lofi, jazz, and electronic.

Each song includes features like energy, tempo, valence, danceability, and acousticness.

I expanded the dataset by adding more songs to improve diversity.

However, the dataset is still small and does not include all types of music or user preferences, such as lyrics or language.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---
The system works well for users with clear and consistent preferences.

For example:
- High energy pop users receive energetic and upbeat songs
- Chill lofi users receive calm and relaxing songs

The scoring logic captures the "vibe" of music effectively using energy and genre.

The system is also simple and transparent, making it easy to understand how recommendations are generated.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  
----------
The recommender system is biased toward features like genre and energy because they have higher weights in the scoring logic.

For example, pop songs appear frequently in recommendations because multiple songs in the dataset belong to the pop genre.

The system also struggles with conflicting preferences, such as high energy but sad mood. In such cases, it may ignore mood and prioritize energy.

Additionally, the dataset is small, which limits diversity and can create a "filter bubble" where similar songs are repeatedly recommended.
------------

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---
I tested the recommender system using multiple user profiles:

- High Energy Pop
- Chill Lofi
- Intense Rock
- Edge Case (high energy + sad mood)

I observed that the system works well when user preferences are clear and consistent.

For example:
- Chill lofi profile produced calm songs
- Rock profile produced high-energy songs

However, in edge cases with conflicting preferences, the system gave mixed results. Songs with high energy were still recommended even when the mood did not match.

This shows that the system prioritizes strong features like genre and energy over weaker ones like mood.
---
## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---
If I had more time, I would improve the system by:

- Adding more features such as tempo range and lyrical themes
- Increasing dataset size for better diversity
- Improving balance between features to avoid bias
- Adding diversity rules to avoid recommending similar songs repeatedly
- Supporting multiple user profiles or group recommendations
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

--
This project helped me understand how recommendation systems convert user preferences into meaningful predictions.

I learned that even simple scoring rules can produce useful recommendations, but they can also introduce bias.

One interesting observation was how small changes in weights can significantly affect results.

This project changed how I think about apps like Spotify, showing that recommendations are based on structured data and algorithms rather than magic.
--