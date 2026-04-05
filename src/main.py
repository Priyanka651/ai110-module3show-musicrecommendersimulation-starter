from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Multiple user profiles
    profiles = {
        "High Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.3},
        "Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
        "Edge Case (High Energy + Sad)": {"genre": "pop", "mood": "sad", "energy": 0.95},
    }

    # Loop through each profile
    for profile_name, user_prefs in profiles.items():
        print("\n==============================")
        print(f"Profile: {profile_name}")
        print("==============================\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()