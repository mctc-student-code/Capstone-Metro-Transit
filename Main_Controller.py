import UI
from UI import MainWindow
import tkinter as tk

import API_Manager

def main():
    #start the ui
    # ui = UI




    #instantiate the API_Manager
    # api_manager = API_Manager

    #get the currently running routes
    routes = API_Manager.get_routes()
    main_window.setRoutes(routes)


main()