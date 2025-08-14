from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtWidgets import QAction, QMenu, QMessageBox
class MinimalPlugin:
    def __init__(self, iface) -> None:
        self.iface = iface

    def initGui(self):
        self.menu = QMenu(self.iface.mainWindow())
        
        self.action = QAction(QIcon("testplug:icon.png"),'Test Plugin', self.iface.mainWindow())
        self.action.setObjectName("testAction")
        self.action.setWhatsThis("Configuration for test plugin")
        self.action.setStatusTip("This is a status tip")
        self.action.triggered.connect(self.run)


        self.help_action = QAction(QIcon("testplug:help-icon.png"), "Test Plugin", self.iface.mainWindow())

        # adding our plugin into the plugin menu
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Test Plugin", self.action)

        #adding the help action into the help menu
        self.iface.pluginHelpMenu().add_action(self.help_action)

        self.help_action.triggered.connect(self.show_help)
        self.iface.mapCanvas().renderComplete.connect(self.renderTest)
        
    def unload(self):
        self.iface.removePluginMenu("&Test Plugin",self.action)
        self.iface.removeToolBarIcon(self.action)
        self.iface.mapCanvas().renderComplete.disconnect(self.renderTest)

    def run(self):
        print("Test Plugin: Run is called")
    def renderTest(self, painter):
        print("Test Plugin: Render Test is called")

    def show_help(self):
        QDesktopServices.openUrl(QUrl('https://docs.qgis.org'))
