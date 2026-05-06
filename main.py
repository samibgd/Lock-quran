from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform
from kivy.graphics import Color, RoundedRectangle

class ModernLargeButton(Button):
    def __init__(self, bg_color, **kwargs):
        super(ModernLargeButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.font_name = "Roboto"
        self.bold = True
        self.bg_color = bg_color
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        
    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color) 
            RoundedRectangle(pos=self.pos, size=self.size, radius=[14])

class PremiumLockApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=35, spacing=20)
        
        with self.layout.canvas.before:
            Color(0.06, 0.09, 0.15, 1)
            self.rect = RoundedRectangle(pos=self.layout.pos, size=self.layout.size)
        self.layout.bind(pos=self.update_bg, size=self.update_bg)
        
        self.status_label = Label(
            text="APP LOCKER CONTROL", 
            font_size='24sp',
            bold=True,
            color=(0.95, 0.77, 0.06, 1),
            halign='center',
            size_hint_y=None,
            height=90
        )
        self.layout.add_widget(self.status_label)
        
        self.sub_label = Label(
            text="Status: System Idle",
            font_size='15sp',
            color=(0.6, 0.7, 0.8, 1),
            size_hint_y=None,
            height=30
        )
        self.layout.add_widget(self.sub_label)
        
        self.app_input = TextInput(
            text="com.instagram.android", 
            multiline=False,
            font_size='16sp',
            padding=[18, 14, 18, 14],
            background_color=(0.15, 0.20, 0.28, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=55
        )
        self.layout.add_widget(self.app_input)
        
        self.time_input = TextInput(
            text="15", 
            multiline=False,
            font_size='16sp',
            padding=[18, 14, 18, 14],
            background_color=(0.15, 0.20, 0.28, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=55
        )
        self.layout.add_widget(self.time_input)
        
        self.start_btn = ModernLargeButton(
            bg_color=(0.18, 0.80, 0.44, 1),
            text="START TIMER & LOCK", 
            font_size='17sp',
            size_hint_y=None,
            height=65 
        )
        self.start_btn.bind(on_press=self.start_process)
        self.layout.add_widget(self.start_btn)
        
        self.cancel_btn = ModernLargeButton(
            bg_color=(0.92, 0.26, 0.21, 1),
            text="CANCEL & UNLOCK APP", 
            font_size='17sp',
            size_hint_y=None,
            height=65
        )
        self.cancel_btn.bind(on_press=self.cancel_process)
        self.layout.add_widget(self.cancel_btn)
        
        self.time_remaining = 0
        self.target_app = ""
        self.timer_event = None
        
        return self.layout

    def update_bg(self, *args):
        self.rect.pos = self.layout.pos
        self.rect.size = self.layout.size

    def start_process(self, instance):
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            
        self.target_app = self.app_input.text.strip()
        try:
            self.time_remaining = int(self.time_input.text.strip()) * 60
        except ValueError:
            self.sub_label.text = "Status: Invalid time entered!"
            return
            
        if not self.target_app:
            self.sub_label.text = "Status: Please enter a package!"
            return

        self.sub_label.text = f"Status: Locking scheduled..."
        
        # تفعيل الصلاحية فوراً هنا بناءً على ضغطة المستخدم المباشرة
        self.trigger_app_lock()
        
        # بدء العداد التنازلي
        self.timer_event = Clock.schedule_interval(self.timer_tick, 1)

    def cancel_process(self, instance):
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            self.timer_event = None
        self.time_remaining = 0
        self.status_label.text = "APP LOCKER CONTROL"
        self.sub_label.text = "Status: Locked Cancelled / Idle"

    def timer_tick(self, dt):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            mins = self.time_remaining // 60
            secs = self.time_remaining % 60
            self.status_label.text = f"LOCKING IN {mins:02d}:{secs:02d}"
            self.sub_label.text = f"Target: {self.target_app}"
        else:
            self.status_label.text = "TIME EXPIRED!"
            self.sub_label.text = f"Status: {self.target_app} Blocked"
            return False 

    def trigger_app_lock(self):
        if platform == 'android':
            try:
                from jnius import autoclass
                Intent = autoclass('android.content.Intent')
                Settings = autoclass('android.provider.Settings')
                Uri = autoclass('android.net.Uri')
                
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                current_activity = PythonActivity.mActivity
                
                # فتح مباشر عند الضغط
                intent = Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION)
                intent.setData(Uri.parse("package:" + current_activity.getPackageName()))
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                
                current_activity.startActivity(intent)
                self.sub_label.text = "Status: Settings opened!"
            except Exception as e:
                try:
                    intent = Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION)
                    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                    current_activity.startActivity(intent)
                except Exception:
                    self.sub_label.text = "Status: Android execution failed"

if __name__ == '__main__':
    PremiumLockApp().run()
