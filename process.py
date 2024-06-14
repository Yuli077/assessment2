
import csv


def load_data():
  reviews = []

  with open('disneyland_reviews.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
            review = {
                "Review_ID": row[0],
                "Rating": int(row[1]),
                "Year_Month": row[2],
                "Reviewer_Location": row[3],
                "Branch": row[4]
            }
            reviews.append(review)
    return reviews


def View_Reviews_by_Park(reviews, park_name_a):
        print(f"Reviews for {park_name_a}:")
        for review in reviews:
            if review["Branch"] == park_name_a:
                print("Review ID:", review["Review_ID"])
                print("Rating:", review["Rating"])
                print("Year and Month:", review["Year_Month"])
                print("Reviewer Location:", review["Reviewer_Location"])
                print("Branch:", review["Branch"])
                print()


def Number_of_Reviews_by_Park_and_Reviewer_Location(reviews, park_name_b, reviewer_location_b):
                 Number_of_Reviews = 0
                 for review in reviews:
                    if review["Branch"] ==  park_name_b and review["Reviewer_Location"] == reviewer_location_b:
                       Number_of_Reviews += 1    
                 return Number_of_Reviews


def Average_Score_per_year_by_Park(reviews, park_name_c, year_c):
        total_score = 0
        count = 0
    
        for review in reviews:
            review_year = review["Year_Month"].split('-')[0]  
            if review["Branch"] == park_name_c and review_year == year_c:
                total_score += review["Rating"]
                count += 1
        

        if count == 0:
            return None  
        
        return total_score / count







