from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.anchorlayout import AnchorLayout

from screencache import ScreenCache
from page import Page


class SideBarInnerButton(Button):
    def __init__(self, page, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.text = page.name

    def on_click_button(self):
        content = self.parent.parent.parent
        self.parent.parent.parent.parent.top_bar.side_bar_button.state = "normal"
        content.clear_widgets()
        content.add_widget(self.page)


class SideBarBoxLayout(BoxLayout):
    def __init__(self, pages: list[Page], **kwargs):
        super().__init__(**kwargs)
        self.inner_button = []
        for page in pages:
            self.inner_button.append(SideBarInnerButton(page))
            self.add_widget(self.inner_button[-1])


class SideBarScrollView(ScrollView):
    def __init__(self, pages: list[Page], **kwargs):
        """
        init the instance property display them or not
        :param pages: list
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.layout = SideBarBoxLayout(pages=pages)
        self.add_widget(self.layout)


class SideBarButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_state_change(self) -> None:
        """
        Call the methode to display or undisplay the SideBar dependly of the button state
        :return: None
        """
        if self.state == "down":
            self.parent.parent.content.display_side_bar()
        elif self.state == "normal":
            self.parent.parent.content.undisplay_side_bar()


class Content(AnchorLayout):
    def __init__(self, **kwargs):
        """
        init the instance property display them or not
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.side_bar = SideBarScrollView([
            Page("Seance"),
            Page("Machines"),
            Page("Seance Model"),
            Page("Statistique"),
        ])
        self.screen_cache = ScreenCache()
        self.page = Label(text="page_content")
        self.add_widget(self.page)

    def display_side_bar(self) -> None:
        """
        No return it's a callback function
        :return:
        """
        self.add_widget(self.screen_cache)
        self.add_widget(self.side_bar)

    def undisplay_side_bar(self) -> None:
        """
        No return it's a callback function
        :return:
        """
        self.remove_widget(self.screen_cache)
        self.remove_widget(self.side_bar)


class TopBar(BoxLayout):
    def __init__(self, **kwargs):
        """
        init the instance property display them or not
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.side_bar_button = SideBarButton()
        self.add_widget(self.side_bar_button)


class MainContent(BoxLayout):

    def __init__(self, **kwargs):
        """
        init the instance property display them or not
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.top_bar = TopBar()
        self.add_widget(self.top_bar)
        self.content = Content()
        self.add_widget(self.content)


class GymApp(App):

    def build(self):
        return MainContent()


if __name__ == "__main__":
    GymApp().run()
