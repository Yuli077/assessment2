

from process import load_data

def Disneyland_Review_Analyser():
  choice = input("Please enter the letter which corresponds with your desired menu choice: \n[A] View Data \n[B] Visualise Data \n[X] Exit \n").upper()

  if choice == 'A':
    print("\nYou have chosen option A - View Data")

    choice_a = input("\nPlease enter one of the following options:\n[A] View Reviews by Park \n[B] Number of Reviews by Park and Reviewer Location  \n[C] Average Score per year by Park  \n[D] Average Score per Park by Reviewer Location\n").upper()


    if choice_a == 'A' :
       print("\nYou have chosen option A - View Reviews by Park\n")
       
       from process import View_Reviews_by_Park
       
       park_name_a = input("Enter the name of the park to view reviews: ")
       reviews = load_data()
       View_Reviews_by_Park(reviews, park_name_a)


      
    if choice_a == 'B' :
      print("\nYou have chosen option B - Number of Reviews by Park and Reviewer Location \n")

      from process import Number_of_Reviews_by_Park_and_Reviewer_Location     

      reviews = load_data()

      park_name_b = input("Enter the name of the park: ")
      reviewer_location_b = input("Enter the reviewer location: ")

      Number_of_Reviews_by_Park_and_Reviewer_Location(reviews, park_name_b, reviewer_location_b)
      Number_of_reviews_count = Number_of_Reviews_by_Park_and_Reviewer_Location(reviews, park_name_b, reviewer_location_b)

      print(f"\n Number of Reviews for {park_name_b} by Reviewer Location - {reviewer_location_b}: {Number_of_reviews_count}")
        

        
    if choice_a == 'C' :
      print("\nYou have chosen option C - Average Score per year by Park \n")

      from process import Average_Score_per_year_by_Park     

      reviews = load_data()

      park_name_c = input("Enter the name of the park: ")
      year_c = input("Enter a year: ")

      average_score = Average_Score_per_year_by_Park (reviews, park_name_c, year_c)

      if average_score is None:
        print(f"\nNo reviews found for {park_name_c} in {year_c}.")
      else:
        print(f"\nThe average rating for {park_name_c} in {year_c}: {average_score:.2f}")



    if choice_a == 'D' :
      print(" d")

#........................................................................................


  if choice == 'B':
    print("\nYou have chosen option B - Visualise Data")

    choice_b = input("\nPlease enter one of the following options:\n[A] Most Reviewed Parks \n[B] Average Scores \n[C] Park Ranking by Nationality \n[D] Most Popular Month by Park\n").upper()
    
    
    if choice_b == 'A' :
        print("\nYou have chosen option A - Most Reviewed Parks\n")

        from visual import option_A_in_Visual
        option_A_in_Visual()

    if choice_b == 'B' :
        print("\nYou have chosen option B - Average Scores\n")
      
      
    if choice_b == 'C' :
        print("\nYou have chosen option C - Park Ranking by Nationality\n")
        
        
    if choice_b == 'D' :
        print("\nYou have chosen option D - Most Popular Month by Park\n")




  if choice == 'X':
      print("\nYou have chosen option X - Exit")




    
