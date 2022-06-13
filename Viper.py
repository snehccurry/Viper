import os
import shutil
import time

folder1 = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'
folder2 = 'C:/Users/'+os.getlogin()+'\AppData\Roaming\Microsoft\Windows\Recent'
folder3=  'C:/Windows/Prefetch'
folder4 = 'C:/Users/'+os.getlogin()+'/Downloads'
folder5=  'C:\Windows\Temp'



folders=[folder5,folder1,folder2,folder3,folder4]
deleteFileCount = 0
deleteFolderCount = 0
# location of run command C:\Users\Cipher\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools
for folder in folders:
    try:
        print('clearing'+folder+':')
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            indexNo = file_path.find('\\')
            itemName = file_path[indexNo+1:]
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print( '%s file deleted' % itemName )
                    deleteFileCount = deleteFileCount + 1
                elif os.path.isdir(file_path):
                    if file_path.__contains__('chocolatey'):  continue #chocolatey is used to fix hidden directories problem
                    shutil.rmtree(file_path)
                    print( '%s folder deleted' % itemName )
                    deleteFolderCount = deleteFolderCount + 1

            except Exception as e:
                print('Access Denied, ig the file is in use/was deleted: %s' % itemName )
                time.sleep(0)
        try:
                os.rmdir(folder)
                shutil.rmtree(file_path)
                os.system('cmd /k "cd C:\Windows\Prefetch & del /q C:\Windows\Prefetch\*"')
        except Exception as e:
                print('Access Denied, ig the folder is in use/ folder was deleted: %s' % folder)
    except Exception as e:
                print("Could not delete that directory, IG it doesn't exsist")
                
power_plan_path= os.getcwd()
print(power_plan_path)
#os.system('cmd /k "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"')
#os.system('cmd /k "powercfg -d e9a42b02-d5df-448d-aa00-03f14749eb61"')



print(str(deleteFileCount)+' files and '+ str(deleteFolderCount)+' folders deleted.')
input('Press <any stupid Key> to Exit')
