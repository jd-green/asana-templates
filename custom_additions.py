import blog_article
import build_task

client_name = input("Client Name: ")
proj_id = input("Project ID: ")
gid = input("Asana Project GID: ")

# # Create 3 Blog Articles
# for num in range(3):
#     id = blog_article.create_article(client_name, str(num+1), "3")
#     print("Blog Article Created!")
#     print("Asana GID = "+id)
#     url = "https://app.asana.com/0/"+id
#     build_task.build_article_task(
#         gid, client_name, str(num+1), url, proj_id)
#     print("Article Tracking Task Created!")
