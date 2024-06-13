"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import matplotlib.pyplot as plt
from process import load_data

def pie_chart():
    def count_reviews_by_park(reviews):
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
            plt.figure(figsize=(10, 7))
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            plt.title("Number of Reviews by Park")
            plt.axis('equal')
            plt.show()

    def main():
            reviews = load_data()
            park_reviews_count = count_reviews_by_park(reviews)
            plot_pie_chart(park_reviews_count)

    if __name__ == "__main__":
        main()


#........................................................................................

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

    plt.figure(figsize=(10, 6))
    plt.bar(branches, avg_ratings, color='skyblue')
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


