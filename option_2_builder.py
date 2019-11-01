import tech_brief
import gg_video
import build_task

client_name = input("Client Name: ")
proj_id = input("Project ID: ")
gid = input("Asana Project GID: ")

for num in range(8):
    id = tech_brief.create_tech_brief(client_name, str(num+1), "8")
    print("Tech Brief Created!")
    print("Asana GID = "+id)
    url = "https://app.asana.com/0/"+id
    build_task.build_tb_task(
        gid, client_name, str(num+1), url, proj_id)
    print("Tech Brief Tracking Task Created!")

for num in range(8):
    id = gg_video.create_gg_video(client_name, str(num+1), "8")
    print("Video Created!")
    print("Asana GID = "+id)
    url = "https://app.asana.com/0/"+id
    build_task.build_gg_video_task(
        gid, client_name, str(num+1), url, proj_id)
    print("Video Tracking Task Created!")

for num in range(2):
    build_task.build_gge_task(gid, client_name, str(num+1),
                              proj_id)
    print("GGE Tracking Task Created!")

build_task.build_gg_task(gid, client_name, proj_id)
print("GG Tracking Task Created!")
