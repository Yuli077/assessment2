"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import matplotlib.pyplot as plt
from process import load_data

def  option_A_in_Visual():
    def plot_reviews_by_park(reviews):
            park_reviews_count = {}

            for review in reviews:
                park_name = review["Branch"]
                if park_name in park_reviews_count:
                    park_reviews_count[park_name] += 1
                else:
                    park_reviews_count[park_name] = 1
            return park_reviews_count
    def plot_pie_chart(data):
            labels = [key for key in data]
            sizes = [data[key] for key in data]

            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            plt.title("Number of Reviews by Park")
            plt.axis('equal')
            plt.show()

    def main():
            reviews = load_data()
            park_reviews_count = plot_reviews_by_park(reviews)
            plot_pie_chart(park_reviews_count)

    if __name__ == "__main__":
        main()


#........................................................................................

def option_B_in_Visual():
    def plot_average_ratings(reviews):
        branch_ratings = {}
        branch_counts = {}

        for review in reviews:
            branch = review["Branch"]
            rating = review["Rating"]

            if branch in branch_ratings:
                branch_ratings[branch] += rating
                branch_counts[branch] += 1
            else:
                branch_ratings[branch] = rating
                branch_counts[branch] = 1

        for branch in branch_ratings:
            branch_ratings[branch] /= branch_counts[branch]


        branches = list(branch_ratings.keys())
        avg_ratings = list(branch_ratings.values())

        plt.bar(branches, avg_ratings, color='green')
        plt.xlabel('Disneyland Branch')
        plt.ylabel('Average Rating')
        plt.title('Average Review Scores for Disneyland Branches')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    if __name__ == '__main__':
        reviews = load_data()
        plot_average_ratings(reviews)

#........................................................................................

def option_C_in_Visual():
    def top_10_locations_by_rating(reviews, park_name):
        park_reviews = [review for review in reviews if review["Branch"] == park_name]

        if not park_reviews:
            print(f"No reviews found for {park_name}.")
            return

        location_ratings = {}
        location_counts = {}

        for review in park_reviews:
            location = review["Reviewer_Location"]
            rating = review["Rating"]

            if location in location_ratings:
                location_ratings[location] += rating
                location_counts[location] += 1
            else:
                location_ratings[location] = rating
                location_counts[location] = 1

        for location in location_ratings:
            location_ratings[location] /= location_counts[location]


        sorted_locations = sorted(location_ratings.items(), key=lambda x: x[1], reverse=True)[:10]
        sorted_locations = dict(sorted_locations)


        locations = list(sorted_locations.keys())
        avg_ratings = list(sorted_locations.values())

        plt.bar(locations, avg_ratings, color='red')
        plt.xlabel('Reviewer Location')
        plt.ylabel('Average Rating')
        plt.title(f'Top 10 Locations with Highest Average Ratings for {park_name}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    if __name__ == '__main__':
        reviews = load_data()
        park_name = input("Enter the Disneyland park ( Disneyland_Paris, Disneyland_California, Disneyland_Hong_Kong): ").strip()
        top_10_locations_by_rating(reviews, park_name)

#........................................................................................


