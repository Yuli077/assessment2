"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""



from process import load_data



def Disneyland_Review_Analyser():
  choice = input("Please enter the letter which corresponds with your desired menu choice: \n[A] View Data \n[B] Visualise Data \n[X] Exit \n").upper()

  if choice == 'A':
    print("\nYou have chosen option A - View Data")

    choice_a = input("\nPlease enter one of the following options:\n[A] View Reviews by Park \n[B] Number of Reviews by Park and Reviewer Location  \n[C] Average Score per year by Park  \n[D] Average Score per Park by Reviewer Location\n").upper()


    if choice_a == 'A' :
       
       from process import View_Reviews_by_Park
       
       park_name_a = input("Enter the name of the park to view reviews: ")
       reviews = load_data()
       View_Reviews_by_Park(reviews, park_name_a)


      
    if choice_a == 'B' :

      from process import Number_of_Reviews_by_Park_and_Reviewer_Location     

      reviews = load_data()

      park_name_b = input("Enter the name of the park: ")
      reviewer_location_b = input("Enter the reviewer location: ")

      Number_of_Reviews_by_Park_and_Reviewer_Location(reviews, park_name_b, reviewer_location_b)
      Number_of_reviews_count = Number_of_Reviews_by_Park_and_Reviewer_Location(reviews, park_name_b, reviewer_location_b)

      print(f"\n Number of Reviews for {park_name_b} by Reviewer Location - {reviewer_location_b}: {Number_of_reviews_count}")
        

        
    if choice_a == 'C' :

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

      from process import count_reviews_by_park
      from visual import plot_pie_chart

      def main():

        reviews = load_data()


        park_reviews_count = count_reviews_by_park(reviews)


        plot_pie_chart(park_reviews_count)

      if __name__ == "__main__":
        main()





    if choice_b == 'B' :
      print("b ")
      
      
    if choice_b == 'C' :
        print("c ")
        
        
    if choice_b == 'D' :
        print("d ")




  if choice == 'X':
      print("\nYou have chosen option X - Exit")




    
