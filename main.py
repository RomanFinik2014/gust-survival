from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivy.clock import Clock

class WebViewWidget(Widget):
    pass

class GustSurvivalApp(App):
    def build(self):
        if platform == 'android':
            from jnius import autoclass
            from android.runnable import run_on_ui_thread
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity

            @run_on_ui_thread
            def create_webview():
                webview = WebView(activity)
                webview.getSettings().setJavaScriptEnabled(True)
                webview.getSettings().setDomStorageEnabled(True)
                webview.getSettings().setAllowFileAccess(True)
                webview.setWebViewClient(WebViewClient())
                webview.loadUrl('file:///android_asset/index.html')
                activity.setContentView(webview)

            Clock.schedule_once(lambda dt: create_webview(), 0)

        return WebViewWidget()

if __name__ == '__main__':
    GustSurvivalApp().run()
