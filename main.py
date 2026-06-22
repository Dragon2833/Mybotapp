from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform
from jnius import autoclass

class RemoteToolApp(App):
    def build(self):
        if platform == 'android':
            self.start_my_service()
        return Label(text="SYSTEM_CORE: ACTIVE\nSTATUS: RUNNING_IN_BACKGROUND")

    def start_my_service(self):
        service = autoclass('org.mybot.mybot.ServiceMybot')
        mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
        context = mActivity.getApplicationContext()
        service_intent = autoclass('android.content.Intent')(context, service)
        context.startService(service_intent)

if __name__ == '__main__':
    RemoteToolApp().run()
