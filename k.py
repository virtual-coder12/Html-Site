from kivy.app import App
from kivy.uix.button import Button


class learn(App):
	def build(self):
		return Button(text = "Hello", pos = (100,500), size =(100,100), size_hint = (0.1,0.1))


if __name__ == "__main__":
	learn().run()
	print("hello")
