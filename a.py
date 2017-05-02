import os 
import pprint
import shutil
path=raw_input("Enter the directory : ")

img_folder=path + "/IMAGES"
music_folder=path+"/MUSIC"
pdf_folder=path+"/PDFS"
doc_folder=path+"/DOCS"
torrent_folder=path+"/TORRENTS"
apps_folder=path+"/Applications or setups"

data=os.listdir(path)

img_list=list()
music_list=list()
pdf_list=list()
torrent_list=list()
docs_list=list()
apps_list=list()

if not os.path.exists(img_folder):
    os.makedirs(img_folder)

if not os.path.exists(music_folder):
    os.makedirs(music_folder)

if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)
	
if not os.path.exists(torrent_folder):
    os.makedirs(torrent_folder)

if not os.path.exists(doc_folder):
    os.makedirs(doc_folder)	
	
if not os.path.exists(apps_folder):
    os.makedirs(apps_folder)	
	
print "total files :", len(data)

#pprint.pprint(data)


for file in data :
    extension=file.split(".")[-1]
    #print extension
    if extension == "jpg" :
        
        img_list.append(file)		
    elif extension == "mp3" :
        
        music_list.append(file)
		
    elif extension =="pdf" :
        pdf_list.append(file)
		
    elif extension =="torrent" :
        torrent_list.append(file)
		
    elif( extension == "docx" or extension == "doc" or extension == "txt") :
	    docs_list.append(file)
		
    elif extension == "exe":
        apps_list.append(file)	
    
print ("#################################################")		
pprint.pprint(img_list)

print ("#################################################")		
pprint.pprint(pdf_list)

print ("##############################3")
pprint.pprint(music_list)

print ("#################################################")
pprint.pprint(torrent_list)

for img in img_list:
    print "Moving ",img,"..."
    try:
        shutil.move(path+'/'+img , img_folder)
    except :
        print "Cannot Move", img	



for song in music_list:
    print "Moving ",song,"..."
    try :
        shutil.move(path+'/'+song , music_folder)
    except :
	    print "Canont move", song

for doc in pdf_list:
    print "moving", doc,"..."
    shutil.move(path+"/"+doc, pdf_folder)
	
for torrent in torrent_list:
    print "moving", torrent, "...."
    try :
        shutil.move(path+"/"+torrent, torrent_folder)
    except:
        print "Cannot move"	
	
	
for doc in docs_list:
    print "moving", doc, "...."
    try :
        shutil.move(path+"/"+doc, doc_folder)
    except:
        print "Cannot move"	
	
	
for app in apps_list:
    print "moving", app, "...."
    try :
        shutil.move(path+"/"+app, apps_folder)
    except:
        print "Cannot move"	
		
#print os.listdir(img_folder)
#print os.listdir(music_folder)
#print os.listdir(pdf_folder)

