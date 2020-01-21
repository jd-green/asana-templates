import blog_article
import build_task
import tech_brief
import webinar_wrapup
import whitepaper
import gorilla_guide_express

client_name = input("Client Name: ")
proj_id = input("Project ID: ")
gid = input("Asana Project GID: ")

# # # Create 3 Whitepaper Projects
# for num in range(3):
#     id = whitepaper.create_whitepaper(client_name, str(num+1), "3")
#     print("Whitepaper Created!")
#     print("Asana GID = "+id)
#     url = "https://app.asana.com/0/"+id
#     build_task.build_wp_task(
#         gid, client_name, str(num+1), url, proj_id, id)
#     print("Whitepaper Tracking Task Created!")
#
# # Create 2 Blog Articles
# for num in range(2):
#     id = blog_article.create_article(client_name, str(num+1), "2")
#     print("Blog Article Created!")
#     print("Asana GID = "+id)
#     url = "https://app.asana.com/0/"+id
#     build_task.build_article_task(
#         gid, client_name, str(num+1), url, proj_id, id)
#     print("Article Tracking Task Created!")

# # Create 4 Tech Brief Projects
# for num in range(4):
#     id = tech_brief.create_tech_brief(client_name, str(num+1), "4")
#     print("Tech Brief Created!")
#     print("Asana GID = "+id)
#     url = "https://app.asana.com/0/"+id
#     build_task.build_tb_task(
#         gid, client_name, str(num+1), url, proj_id, id)
#     print("Tech Brief Tracking Task Created!")

# Create 1 Webinar Wrap-Up Paper Projects
# for num in range(1):
#     id = webinar_wrapup.create_wrapup(client_name, str(num+1), "1")
#     print("Webinar Wrap-Up Paper Created!")
#     print("Asana GID = "+id)
#     url = "https://app.asana.com/0/"+id
#     build_task.build_wrapup_task(
#         gid, client_name, str(num+1), url, proj_id, id)
#     print("Webinar Wrap-Up Paper Tracking Task Created!")

# Create 3 Gorilla Guide Express Projects
for num in range(3):
    id = gorilla_guide_express.create_gge(client_name, str(num+1), "3")
    print("Gorilla Guide Express Created!")
    print("Asana GID = "+id)
    url = "https://app.asana.com/0/"+id
    build_task.build_full_gge_task(
        gid, client_name, str(num+1), url, proj_id, id)
    print("GGE Tracking Task Created!")
