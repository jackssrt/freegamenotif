import win10toast
x = win10toast.ToastNotifier()
for _ in range(10):
    x.show_toast(
        duration=1,
        threaded=True
    )
