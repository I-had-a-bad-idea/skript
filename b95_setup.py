import os
import webbrowser as wb

def open_dir(path):
    path = os.path.realpath(path)
    os.startfile(path)

if __name__ == '__main__':
    # Open 'PT Dev Course' directory on VS Code
    dev_course_path = 'C:\\Users\\Billy Arante\\Full-time Work\\Zuitt Coding Bootcamp\\Curricula\\PT Dev Courses'
    os.system(f'cd {dev_course_path} && code .')
    # Open 'billy-arante' on Windows Explorer
    open_dir('C:\\Users\\Billy Arante\\Documents\\billy-arante')
    # Open 'csp2/app-server' directory on Sublime Text
    csp2_app_server_path = 'C:\\Users\\Billy Arante\\Documents\\billy-arante\\csp2\\app-server'
    os.system(f'cd {csp2_app_server_path} && subl .')
    # Open the 'billy-csp2-app-client' on Glitch
    app_client_path = 'https://glitch.com/edit/#!/billy-csp2-app-client'
    wb.open(app_client_path)
    # Open the Postman app
    postman_path = 'C:\\Users\\Billy Arante\\AppData\\Local\\Postman\\Postman.exe'
    open_dir(postman_path)