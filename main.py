import Carrer_finder
# from Career_finder import find_career_page
website = "https://openai.com"
website2 = "https://www.linkedin.com"
website3 = "https://www.linkedin.com/jobs/"

career_page = Carrer_finder.find_career_page(website2)

print(career_page)